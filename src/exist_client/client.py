import itertools
from typing import Any, Callable, Iterable, Optional, Protocol, TypeVar

from ._exist_io_client import AuthenticatedClient
from ._exist_io_client.api.default import (
    accounts_profile,
    attribute_values_get,
    attributes_acquire,
    attributes_get,
    attributes_update,
)

# TODO: move to .models
from ._exist_io_client.models import (
    AttributeByName,
    AttributeByTemplate,
    AttributesAcquireResult,
    AttributesUpdateResult,
    DateValue,
    UserProfile,
)
from .models import Attribute, AttributeValue

EXIST_IO_BASE_URL = "https://exist.io"

T = TypeVar("T")


class PaginatedResponse(Protocol[T]):
    results: list[T]
    next_: Optional[str]


PaginatedApi = Callable[..., Optional[PaginatedResponse[T]]]


class ExistClient:
    def __init__(self, *, token: str, base_url: str = EXIST_IO_BASE_URL):
        self.client = AuthenticatedClient(
            base_url,
            token,
            raise_on_unexpected_status=True,
            follow_redirects=True,
        )

    def get_profile(self) -> Optional[UserProfile]:
        return accounts_profile.sync(client=self.client)

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
                attributes_get.sync,
                attributes=",".join(attributes) if attributes is not None else None,
                groups=",".join(groups) if groups is not None else None,
                manual=manual,
                owned=owned,
            )
        )

    def get_attribute_values(self, *, attribute: str) -> list[DateValue]:
        return list(self._paginate(attribute_values_get.sync, attribute=attribute))

    def acquire_attributes(
        self,
        *,
        acquisitions: list[AttributeByName | AttributeByTemplate],
    ) -> Optional[AttributesAcquireResult]:
        return attributes_acquire.sync(client=self.client, json_body=acquisitions)

    def update_attributes(
        self, *, updates: list[AttributeValue]
    ) -> Optional[AttributesUpdateResult]:
        return attributes_update.sync(client=self.client, json_body=updates)
