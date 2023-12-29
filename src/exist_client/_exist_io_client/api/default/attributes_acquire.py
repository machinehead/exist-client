from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attribute_by_name import AttributeByName
from ...models.attribute_by_template import AttributeByTemplate
from ...models.attributes_acquire_result import AttributesAcquireResult
from ...types import Response


def _get_kwargs(
    *,
    json_body: List[Union["AttributeByName", "AttributeByTemplate"]],
) -> Dict[str, Any]:
    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item: Dict[str, Any]

        if isinstance(json_body_item_data, AttributeByTemplate):
            json_body_item = json_body_item_data.to_dict()

        else:
            json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "post",
        "url": "/api/2/attributes/acquire/",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AttributesAcquireResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AttributesAcquireResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = AttributesAcquireResult.from_dict(response.json())

        return response_202
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AttributesAcquireResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: List[Union["AttributeByName", "AttributeByTemplate"]],
) -> Response[AttributesAcquireResult]:
    """
    Args:
        json_body (List[Union['AttributeByName', 'AttributeByTemplate']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributesAcquireResult]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: List[Union["AttributeByName", "AttributeByTemplate"]],
) -> Optional[AttributesAcquireResult]:
    """
    Args:
        json_body (List[Union['AttributeByName', 'AttributeByTemplate']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributesAcquireResult
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: List[Union["AttributeByName", "AttributeByTemplate"]],
) -> Response[AttributesAcquireResult]:
    """
    Args:
        json_body (List[Union['AttributeByName', 'AttributeByTemplate']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributesAcquireResult]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: List[Union["AttributeByName", "AttributeByTemplate"]],
) -> Optional[AttributesAcquireResult]:
    """
    Args:
        json_body (List[Union['AttributeByName', 'AttributeByTemplate']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributesAcquireResult
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
