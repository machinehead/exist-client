import itertools
from typing import Any, Callable, Iterable, Optional, Protocol, TypeVar

from loguru import logger

from ._exist_io_client import AuthenticatedClient
from ._exist_io_client.api.default import (
    acquire_attributes,
    get_attribute_values,
    get_attributes,
    get_profile,
    update_attributes,
)
from ._exist_io_client.errors import UnexpectedStatus

# TODO: move to .models
from ._exist_io_client.models import (
    AttributeAcquisitionResponse,
    AttributeAcquisitionType0,
    AttributeAcquisitionType1,
    AttributesUpdateResponse,
    GetAttributeValuesResponseResultsItem,
    UserProfile,
)
from .models import Attribute, AttributeUpdate

EXIST_IO_BASE_URL = "https://exist.io"

T = TypeVar("T")


class PaginatedResponse(Protocol[T]):
    results: list[T]
    next_: Optional[str]


PaginatedApi = Callable[..., Optional[PaginatedResponse[T]]]


class ExistClient:
    def __init__(self, *, token: str):
        self.client = AuthenticatedClient(
            EXIST_IO_BASE_URL,
            token,
            raise_on_unexpected_status=True,
            follow_redirects=True,
        )

    def get_profile(self) -> Optional[UserProfile]:
        return get_profile.sync(client=self.client)

    def _paginate(self, api: PaginatedApi[T], **kwargs: Any) -> Iterable[T]:
        for page in itertools.count(start=1):
            args = kwargs | dict(
                client=self.client,
                page=page,
            )
            resp = api(**args)
            assert resp is not None
            yield from resp.results
            if resp.next_ is None:
                break

    def get_attributes(
        self,
        *,
        attributes: Optional[list[str]] = None,
        groups: Optional[list[str]] = None,
        manual: Optional[bool] = None,
        owned: Optional[bool] = None,
    ) -> list[Attribute]:
        return list(
            self._paginate(
                get_attributes.sync,
                attributes=",".join(attributes) if attributes is not None else None,
                groups=",".join(groups) if groups is not None else None,
                manual=manual,
                owned=owned,
            )
        )

    def get_attribute_values(
        self, *, attribute: str
    ) -> list[GetAttributeValuesResponseResultsItem]:
        return list(self._paginate(get_attribute_values.sync, attribute=attribute))

    def acquire_attributes(
        self,
        *,
        acquisitions: list[AttributeAcquisitionType0 | AttributeAcquisitionType1],
    ) -> Optional[AttributeAcquisitionResponse]:
        return acquire_attributes.sync(client=self.client, json_body=acquisitions)

    def update_attributes(
        self, *, updates: list[AttributeUpdate]
    ) -> Optional[AttributesUpdateResponse]:
        try:
            return update_attributes.sync(client=self.client, json_body=updates)
        except UnexpectedStatus as e:
            # TODO: put this into a template for generated code?
            logger.error(
                f"Got unexpected status code: {e.status_code}, response content: {e.content}"
            )
            raise
