from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttributesUpdateResponseFailedItem")


@_attrs_define
class AttributesUpdateResponseFailedItem:
    """
    Attributes:
        name (str):
        date (str):
        error (str):
        error_code (str):
    """

    name: str
    date: str
    error: str
    error_code: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        date = self.date
        error = self.error
        error_code = self.error_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "date": date,
                "error": error,
                "error_code": error_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        date = d.pop("date")

        error = d.pop("error")

        error_code = d.pop("error_code")

        attributes_update_response_failed_item = cls(
            name=name,
            date=date,
            error=error,
            error_code=error_code,
        )

        attributes_update_response_failed_item.additional_properties = d
        return attributes_update_response_failed_item

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
