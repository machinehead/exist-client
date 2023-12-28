from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Tokens")


@_attrs_define
class Tokens:
    """
    Attributes:
        access_token (str):
        token_type (str):
        expires_in (int):
        scope (str):
        refresh_token (str):
    """

    access_token: str
    token_type: str
    expires_in: int
    scope: str
    refresh_token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        token_type = self.token_type
        expires_in = self.expires_in
        scope = self.scope
        refresh_token = self.refresh_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "token_type": token_type,
                "expires_in": expires_in,
                "scope": scope,
                "refresh_token": refresh_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token")

        token_type = d.pop("token_type")

        expires_in = d.pop("expires_in")

        scope = d.pop("scope")

        refresh_token = d.pop("refresh_token")

        tokens = cls(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            scope=scope,
            refresh_token=refresh_token,
        )

        tokens.additional_properties = d
        return tokens

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
