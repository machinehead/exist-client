import httpx

from exist_client import ExistClient


def test_get_profile(exist_api_mock):
    client = ExistClient(token="token")
    exist_api_mock.get("/api/2/accounts/profile/").return_value = httpx.Response(
        200,
        json={
            "timezone": "America/Chicago",
        },
    )
    client.get_profile()


def test_get_attributes(exist_api_mock):
    client = ExistClient(token="token")
    exist_api_mock.get("/api/2/attributes/").return_value = httpx.Response(
        200,
        json={
            "count": 0,
            "results": [],
            "next": None,
            "previous": None,
        },
    )
    client.get_attributes()
