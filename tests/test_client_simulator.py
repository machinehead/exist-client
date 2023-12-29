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
    AttributeGroup,
    AttributesGetResult,
    AttributesUpdateResult,
    AttributeValue,
)
from exist_client.client import EXIST_IO_BASE_URL

INVALID_TOKEN_RESPONSE_CONTENT = b'{"detail": "Invalid token"}'

_T = TypeVar("_T")

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
        assert (
            client.update_attributes(
                updates=[
                    AttributeValue(name="myair_score", date="2023-12-29", value=57),
                ]
            )
            == snapshot
        )


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

    attributes: list[Attribute] = [
        Attribute(
            name="sleep",
            label="Time asleep",
            group=AttributeGroup(
                name="sleep",
                label="Sleep",
            ),
            value_type_description="Period (min)",
            template="sleep",
        ),
    ]

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
        # TODO: check ownership
        request_json = request.json
        assert request_json is not None
        input_values = [AttributeValue.from_dict(value) for value in request_json]
        return AttributesUpdateResult(success=input_values, failed=[]).to_dict()

    with respx.mock(base_url=EXIST_IO_BASE_URL) as respx_mock:
        respx_mock.route().mock(side_effect=WSGIHandler(app))
        yield respx_mock
