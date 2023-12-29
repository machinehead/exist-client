from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attributes_get_result import AttributesGetResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owned: Union[Unset, None, bool] = UNSET,
    include_low_priority: Union[Unset, None, bool] = UNSET,
    include_inactive: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    manual: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["owned"] = owned

    params["include_low_priority"] = include_low_priority

    params["include_inactive"] = include_inactive

    params["limit"] = limit

    params["groups"] = groups

    params["attributes"] = attributes

    params["manual"] = manual

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/2/attributes/",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AttributesGetResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AttributesGetResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AttributesGetResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    owned: Union[Unset, None, bool] = UNSET,
    include_low_priority: Union[Unset, None, bool] = UNSET,
    include_inactive: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    manual: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
) -> Response[AttributesGetResult]:
    """
    Args:
        owned (Union[Unset, None, bool]):
        include_low_priority (Union[Unset, None, bool]):
        include_inactive (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        groups (Union[Unset, None, str]):
        attributes (Union[Unset, None, str]):
        manual (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributesGetResult]
    """

    kwargs = _get_kwargs(
        owned=owned,
        include_low_priority=include_low_priority,
        include_inactive=include_inactive,
        limit=limit,
        groups=groups,
        attributes=attributes,
        manual=manual,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    owned: Union[Unset, None, bool] = UNSET,
    include_low_priority: Union[Unset, None, bool] = UNSET,
    include_inactive: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    manual: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
) -> Optional[AttributesGetResult]:
    """
    Args:
        owned (Union[Unset, None, bool]):
        include_low_priority (Union[Unset, None, bool]):
        include_inactive (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        groups (Union[Unset, None, str]):
        attributes (Union[Unset, None, str]):
        manual (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributesGetResult
    """

    return sync_detailed(
        client=client,
        owned=owned,
        include_low_priority=include_low_priority,
        include_inactive=include_inactive,
        limit=limit,
        groups=groups,
        attributes=attributes,
        manual=manual,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    owned: Union[Unset, None, bool] = UNSET,
    include_low_priority: Union[Unset, None, bool] = UNSET,
    include_inactive: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    manual: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
) -> Response[AttributesGetResult]:
    """
    Args:
        owned (Union[Unset, None, bool]):
        include_low_priority (Union[Unset, None, bool]):
        include_inactive (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        groups (Union[Unset, None, str]):
        attributes (Union[Unset, None, str]):
        manual (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributesGetResult]
    """

    kwargs = _get_kwargs(
        owned=owned,
        include_low_priority=include_low_priority,
        include_inactive=include_inactive,
        limit=limit,
        groups=groups,
        attributes=attributes,
        manual=manual,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    owned: Union[Unset, None, bool] = UNSET,
    include_low_priority: Union[Unset, None, bool] = UNSET,
    include_inactive: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    groups: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    manual: Union[Unset, None, bool] = UNSET,
    page: Union[Unset, None, int] = UNSET,
) -> Optional[AttributesGetResult]:
    """
    Args:
        owned (Union[Unset, None, bool]):
        include_low_priority (Union[Unset, None, bool]):
        include_inactive (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        groups (Union[Unset, None, str]):
        attributes (Union[Unset, None, str]):
        manual (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributesGetResult
    """

    return (
        await asyncio_detailed(
            client=client,
            owned=owned,
            include_low_priority=include_low_priority,
            include_inactive=include_inactive,
            limit=limit,
            groups=groups,
            attributes=attributes,
            manual=manual,
            page=page,
        )
    ).parsed
