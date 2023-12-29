from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeAcquisitionResponseFailedItem")


@_attrs_define
class AttributeAcquisitionResponseFailedItem:
    """
    Attributes:
        name (str):
        error (str):
        error_code (str):
        template (Union[Unset, str]):
    """

    name: str
    error: str
    error_code: str
    template: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        error = self.error
        error_code = self.error_code
        template = self.template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "error": error,
                "error_code": error_code,
            }
        )
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        error = d.pop("error")

        error_code = d.pop("error_code")

        template = d.pop("template", UNSET)

        attribute_acquisition_response_failed_item = cls(
            name=name,
            error=error,
            error_code=error_code,
            template=template,
        )

        attribute_acquisition_response_failed_item.additional_properties = d
        return attribute_acquisition_response_failed_item

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
