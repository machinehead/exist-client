import pytest
import respx


@pytest.fixture(autouse=True)
def exist_api_mock():
    with respx.mock(base_url="https://exist.io") as respx_mock:
        yield respx_mock
