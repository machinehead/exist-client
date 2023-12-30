from contextlib import nullcontext as does_not_raise
from typing import Any, Generator, Optional, TypeVar, Union

import pytest
import respx
from _pytest.python_api import RaisesContext
from flask import Flask, request
from flask_httpauth import HTTPTokenAuth
from respx import MockRouter, WSGIHandler
from syrupy.assertion import SnapshotAssertion

from exist_client import ExistClient
from exist_client._exist_io_client.errors import UnexpectedStatus
from exist_client._exist_io_client.models import (
    Attribute,
    AttributeByName,
    AttributeGroup,
    AttributesAcquireResult,
    AttributesAcquireResultFailedItem,
    AttributesAcquireResultSuccessItem,
    AttributesGetResult,
    AttributesUpdateResult,
    AttributesUpdateResultFailedItem,
    AttributeValue,
)
from exist_client.client import EXIST_IO_BASE_URL

INVALID_TOKEN_RESPONSE_CONTENT = b'{"detail": "Invalid token"}'

_T = TypeVar("_T")

# TODO: support status 401
TOKEN_EXPECTATION_PARAMS = (
    "token,expectation",
    [
        ("known-token", does_not_raise()),
        (
            "unknown-token",
            pytest.raises(
                UnexpectedStatus,
                match=f"Unexpected status code: 401, content: {INVALID_TOKEN_RESPONSE_CONTENT!r}",
            ),
        ),
    ],
)


# https://docs.pytest.org/en/7.1.x/example/parametrize.html#parametrizing-conditional-raising
@pytest.mark.parametrize(*TOKEN_EXPECTATION_PARAMS)
def test_get_attributes(
    token: str,
    expectation: Union[does_not_raise[_T] | RaisesContext[Exception]],
    exist_api_simulator: MockRouter,
    snapshot: SnapshotAssertion,
) -> None:
    client = ExistClient(token=token)
    with expectation:
        assert client.get_attributes() == snapshot


@pytest.mark.parametrize(*TOKEN_EXPECTATION_PARAMS)
def test_update_attributes(
    token: str,
    expectation: Union[does_not_raise[_T] | RaisesContext[Exception]],
    exist_api_simulator: MockRouter,
    snapshot: SnapshotAssertion,
) -> None:
    client = ExistClient(token=token)
    with expectation:
        assert client.update_attributes(
            updates=[
                AttributeValue(name="nonexistent", date="2023-12-29", value=480),
            ]
        ) == snapshot(name="nonexistent")
        myair_score_update = AttributeValue(
            name="myair_score", date="2023-12-29", value=57
        )
        assert client.update_attributes(
            updates=[
                myair_score_update,
            ]
        ) == snapshot(name="unauthorised")
        assert (
            client.acquire_attributes(
                acquisitions=[AttributeByName(name="myair_score")]
            )
        ) == snapshot(name="acquire_myair_score")
        assert client.update_attributes(
            updates=[
                myair_score_update,
            ]
        ) == snapshot(name="retry_myair_score")


@pytest.fixture
def exist_api_simulator() -> Generator[MockRouter, None, None]:
    app = Flask("foobar")
    auth = HTTPTokenAuth(scheme="Bearer")

    tokens = {"known-token": "accepted"}

    @auth.verify_token
    def verify_token(token: str) -> Optional[str]:
        return tokens.get(token)

    @auth.error_handler
    def auth_error(status: int) -> tuple[bytes, int]:
        return INVALID_TOKEN_RESPONSE_CONTENT, status

    # {"template":"sleep","name":"sleep","label":"Time asleep","group":{"name":"sleep","label":"Sleep","priority":3},
    # "service":{"name":"garmin","label":"Garmin"},"active":true,"priority":1,"manual":false,"value_type":3,
    # "value_type_description":"Period (min)","available_services":[{"name":"garmin","label":"Garmin"}]}

    sleep_group = AttributeGroup(
        name="sleep",
        label="Sleep",
    )

    attributes: list[Attribute] = [
        Attribute(
            name="sleep",
            label="Time asleep",
            group=sleep_group,
            value_type_description="Period (min)",
            template="sleep",
        ),
        Attribute(
            name="myair_score",
            label="myAir score",
            group=sleep_group,
            value_type_description="Percentage",
            template=None,
        ),
    ]

    attribute_owned = {attr.name: False for attr in attributes}

    @app.get("/api/2/attributes/")
    @auth.login_required
    def get_attributes() -> dict[str, Any]:
        return AttributesGetResult(
            count=len(attributes),
            # TODO: filter by groups the client has access to
            results=attributes,
            # TODO: add pagination
            next_=None,
            previous=None,
        ).to_dict()

    @app.post("/api/2/attributes/update/")
    @auth.login_required
    def update_attributes() -> dict[str, Any]:
        request_json = request.json
        assert request_json is not None
        success = []
        failed = []
        for item in request_json:
            value = AttributeValue.from_dict(item)
            owned = attribute_owned.get(value.name)
            if owned is None:
                failed.append(
                    AttributesUpdateResultFailedItem(
                        error=f"User doesn't have an attribute named '{value.name}'",
                        error_code="not_found",
                        **value.to_dict(),
                    )
                )
            elif not owned:
                failed.append(
                    AttributesUpdateResultFailedItem(
                        error=f"Attribute '{value.name}' does not belong to this service",
                        error_code="unauthorised",
                        **value.to_dict(),
                    )
                )
            else:
                # TODO: data validation
                #  'value_type': 5, 'value_type_description': 'Percentage':
                #    AttributesUpdateResultFailedItem(
                #       error='Value must be a float between 0 and 1',
                #       error_code='validation',
                #       date='2023-12-29',
                #       value=57,
                #       name='myair_score',
                #       additional_properties={}
                #    )
                success.append(value)
        return AttributesUpdateResult(success=success, failed=failed).to_dict()

    @app.post("/api/2/attributes/acquire/")
    @auth.login_required
    def acquire_attributes() -> dict[str, Any]:
        request_json = request.json
        assert request_json is not None
        success = []
        failed = []
        for item in request_json:
            # TODO: support AttributeByTemplate, currently only AttributeByName is supported
            attribute = AttributeByName.from_dict(item)
            owned = attribute_owned.get(attribute.name)
            if owned is None:
                failed.append(
                    AttributesAcquireResultFailedItem(
                        error="Attribute matching query does not exist.",
                        error_code="not_found",
                        **attribute.to_dict(),
                    )
                )
            # TODO: support groups the client doesn't have access to, e.g.:
            #  AttributesAcquireResultFailedItem(
            #    error="No permission to write to attributes in group 'activity'",
            #    error_code='not_allowed',
            #    name='steps',
            #    additional_properties={}
            #  )
            else:
                # Doesn't matter owned or not owned, same response
                attribute_owned[attribute.name] = True
                success.append(
                    AttributesAcquireResultSuccessItem(
                        **attribute.to_dict(),
                    )
                )
        return AttributesAcquireResult(
            success=success,
            failed=failed,
        ).to_dict()

    with respx.mock(base_url=EXIST_IO_BASE_URL) as respx_mock:
        respx_mock.route().mock(side_effect=WSGIHandler(app))
        yield respx_mock
