from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_attributes_response_200 import GetAttributesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owned: Union[Unset, None, str] = UNSET,
    include_low_priority: Union[Unset, None, str] = UNSET,
    include_inactive: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["owned"] = owned

    params["include_low_priority"] = include_low_priority

    params["include_inactive"] = include_inactive

    params["limit"] = limit

    params["groups"] = groups

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/2/attributes/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAttributesResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAttributesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAttributesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    owned: Union[Unset, None, str] = UNSET,
    include_low_priority: Union[Unset, None, str] = UNSET,
    include_inactive: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
) -> Response[GetAttributesResponse200]:
    """
    Args:
        owned (Union[Unset, None, str]):
        include_low_priority (Union[Unset, None, str]):
        include_inactive (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        groups (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAttributesResponse200]
    """

    kwargs = _get_kwargs(
        owned=owned,
        include_low_priority=include_low_priority,
        include_inactive=include_inactive,
        limit=limit,
        groups=groups,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    owned: Union[Unset, None, str] = UNSET,
    include_low_priority: Union[Unset, None, str] = UNSET,
    include_inactive: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
) -> Optional[GetAttributesResponse200]:
    """
    Args:
        owned (Union[Unset, None, str]):
        include_low_priority (Union[Unset, None, str]):
        include_inactive (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        groups (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAttributesResponse200
    """

    return sync_detailed(
        client=client,
        owned=owned,
        include_low_priority=include_low_priority,
        include_inactive=include_inactive,
        limit=limit,
        groups=groups,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    owned: Union[Unset, None, str] = UNSET,
    include_low_priority: Union[Unset, None, str] = UNSET,
    include_inactive: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
) -> Response[GetAttributesResponse200]:
    """
    Args:
        owned (Union[Unset, None, str]):
        include_low_priority (Union[Unset, None, str]):
        include_inactive (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        groups (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAttributesResponse200]
    """

    kwargs = _get_kwargs(
        owned=owned,
        include_low_priority=include_low_priority,
        include_inactive=include_inactive,
        limit=limit,
        groups=groups,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    owned: Union[Unset, None, str] = UNSET,
    include_low_priority: Union[Unset, None, str] = UNSET,
    include_inactive: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
) -> Optional[GetAttributesResponse200]:
    """
    Args:
        owned (Union[Unset, None, str]):
        include_low_priority (Union[Unset, None, str]):
        include_inactive (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        groups (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAttributesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            owned=owned,
            include_low_priority=include_low_priority,
            include_inactive=include_inactive,
            limit=limit,
            groups=groups,
        )
    ).parsed
