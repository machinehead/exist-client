from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttributeValue")


@_attrs_define
class AttributeValue:
    """
    Attributes:
        date (str):
        value (Union[float, int, str]):
        name (str):
    """

    date: str
    value: Union[float, int, str]
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        value: Union[float, int, str]

        value = self.value

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "value": value,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date")

        def _parse_value(data: object) -> Union[float, int, str]:
            return cast(Union[float, int, str], data)

        value = _parse_value(d.pop("value"))

        name = d.pop("name")

        attribute_value = cls(
            date=date,
            value=value,
            name=name,
        )

        attribute_value.additional_properties = d
        return attribute_value

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
