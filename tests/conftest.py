from typing import Generator

import pytest
import respx
from respx import MockRouter

from exist_client.client import EXIST_IO_BASE_URL


@pytest.fixture
def exist_api_mock() -> Generator[MockRouter, None, None]:
    with respx.mock(base_url=EXIST_IO_BASE_URL) as respx_mock:
        yield respx_mock
