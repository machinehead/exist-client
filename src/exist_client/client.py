import itertools
from typing import Optional

from .exist_io_client import AuthenticatedClient
from .exist_io_client.api.default import get_attributes, get_profile

EXIST_IO_BASE_URL = "https://exist.io"


class ExistClient:
    def __init__(self, *, token: str):
        self.client = AuthenticatedClient(
            EXIST_IO_BASE_URL,
            token,
            raise_on_unexpected_status=True,
            follow_redirects=True,
        )

    def get_profile(self):
        return get_profile.sync_detailed(client=self.client)

    def get_attributes(
        self,
        *,
        attributes: Optional[list[str]] = None,
        groups: Optional[list[str]] = None,
        manual: Optional[bool] = None,
        owned: Optional[bool] = None
    ):
        result = []
        for page in itertools.count(start=1):
            resp = get_attributes.sync(
                client=self.client,
                attributes=",".join(attributes) if attributes is not None else None,
                groups=",".join(groups) if groups is not None else None,
                manual=manual,
                owned=owned,
                page=page,
            ).to_dict()
            result.extend(resp["results"])
            if resp["next"] is None:
                break
        return result
