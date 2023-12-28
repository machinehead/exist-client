from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeUpdate")


@_attrs_define
class AttributeUpdate:
    """
    Attributes:
        name (str):
        date (Union[Unset, str]):
        value (Union[Unset, float, int, str]):
    """

    name: str
    date: Union[Unset, str] = UNSET
    value: Union[Unset, float, int, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        date = self.date
        value: Union[Unset, float, int, str]
        if isinstance(self.value, Unset):
            value = UNSET

        else:
            value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        date = d.pop("date", UNSET)

        def _parse_value(data: object) -> Union[Unset, float, int, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, int, str], data)

        value = _parse_value(d.pop("value", UNSET))

        attribute_update = cls(
            name=name,
            date=date,
            value=value,
        )

        attribute_update.additional_properties = d
        return attribute_update

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
