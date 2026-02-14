from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessTokenData")


@_attrs_define
class AccessTokenData:
    """
    Attributes:
        grant_type (str): Either 'authorization_code' or 'refresh_token'
        client_id (str):
        client_secret (str):
        code (Union[Unset, str]): Required when grant_type is 'authorization_code'
        redirect_uri (Union[Unset, str]): Required when grant_type is 'authorization_code'
        refresh_token (Union[Unset, str]): Required when grant_type is 'refresh_token'
    """

    grant_type: str
    client_id: str
    client_secret: str
    code: Union[Unset, str] = UNSET
    redirect_uri: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type
        client_id = self.client_id
        client_secret = self.client_secret
        code = self.code
        redirect_uri = self.redirect_uri
        refresh_token = self.refresh_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_type = d.pop("grant_type")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        code = d.pop("code", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        access_token_data = cls(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
        )

        access_token_data.additional_properties = d
        return access_token_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
