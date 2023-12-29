from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccessTokenData")


@_attrs_define
class AccessTokenData:
    """
    Attributes:
        grant_type (str):
        code (str):
        client_id (str):
        client_secret (str):
    """

    grant_type: str
    code: str
    client_id: str
    client_secret: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type
        code = self.code
        client_id = self.client_id
        client_secret = self.client_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
                "code": code,
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_type = d.pop("grant_type")

        code = d.pop("code")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        access_token_data = cls(
            grant_type=grant_type,
            code=code,
            client_id=client_id,
            client_secret=client_secret,
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
