from typing import Generator

import pytest
import respx
from respx import MockRouter


@pytest.fixture
def exist_api_mock() -> Generator[MockRouter, None, None]:
    with respx.mock(base_url="https://exist.io") as respx_mock:
        yield respx_mock
