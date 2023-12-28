import httpx

from exist_client.exist_io_client.api.default import get_profile
from exist_client.exist_io_client.client import AuthenticatedClient

EXIST_IO_BASE_URL = "https://exist.io"


def test_client(exist_api_mock):
    client = AuthenticatedClient(EXIST_IO_BASE_URL, "")
    exist_api_mock.get("/api/2/accounts/profile/").return_value = httpx.Response(
        200,
        json={
            "timezone": "America/Chicago",
        },
    )
    get_profile.sync_detailed(client=client)
