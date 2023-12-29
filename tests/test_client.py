import httpx

from exist_client import ExistClient
from exist_client._exist_io_client.models import AttributeAcquisitionType1
from exist_client.models import AttributeUpdate


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
            "count": 1,
            "results": [
                {
                    "name": "attr",
                    "label": "Attr",
                    "group": {"name": "group", "label": "Group"},
                    "value_type_description": "Integer",
                    "template": None,
                },
            ],
            "next": None,
            "previous": None,
        },
    )
    client.get_attributes()


def test_get_attribute_values(exist_api_mock):
    client = ExistClient(token="token")
    exist_api_mock.get("/api/2/attributes/values/").return_value = httpx.Response(
        200,
        json={
            "count": 1,
            "results": [{"date": "2023-12-29", "value": 50}],
            "next": None,
            "previous": None,
        },
    )
    client.get_attribute_values(attribute="attribute")


def test_acquire_attributes(exist_api_mock):
    client = ExistClient(token="token")
    exist_api_mock.post("/api/2/attributes/acquire/").return_value = httpx.Response(
        200,
        json={
            "success": [{"name": "attr"}],
            "failed": [
                {
                    "name": "steps",
                    "error": "No permission to write to attributes in group 'activity'",
                    "error_code": "not_allowed",
                    "template": None,
                }
            ],
        },
    )
    client.acquire_attributes(acquisitions=[AttributeAcquisitionType1(name="steps")])


def test_update_attributes(exist_api_mock):
    client = ExistClient(token="token")
    exist_api_mock.post("/api/2/attributes/update/").return_value = httpx.Response(
        200,
        json={
            "success": [
                {
                    "name": "attr",
                    "date": "2023-12-29",
                    "value": 50,
                }
            ],
            "failed": [
                {
                    "name": "attr",
                    "date": "2023-12-29",
                    "error": "Attribute 'attr' does not belong to this service",
                    "error_code": "unauthorised",
                    "value": 57,
                },
            ],
        },
    )
    client.update_attributes(
        updates=[AttributeUpdate(name="attr", date="2023-12-29", value=50)]
    )
