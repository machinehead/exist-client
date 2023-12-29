from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttributesUpdateResponseSuccessItem")


@_attrs_define
class AttributesUpdateResponseSuccessItem:
    """
    Attributes:
        name (str):
        date (str):
        value (Union[float, int, str]):
    """

    name: str
    date: str
    value: Union[float, int, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        date = self.date
        value: Union[float, int, str]

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "date": date,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        date = d.pop("date")

        def _parse_value(data: object) -> Union[float, int, str]:
            return cast(Union[float, int, str], data)

        value = _parse_value(d.pop("value"))

        attributes_update_response_success_item = cls(
            name=name,
            date=date,
            value=value,
        )

        attributes_update_response_success_item.additional_properties = d
        return attributes_update_response_success_item

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
