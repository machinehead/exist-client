from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attribute_value import AttributeValue
    from ..models.attributes_update_result_failed_item import (
        AttributesUpdateResultFailedItem,
    )


T = TypeVar("T", bound="AttributesUpdateResult")


@_attrs_define
class AttributesUpdateResult:
    """
    Attributes:
        success (List['AttributeValue']):
        failed (List['AttributesUpdateResultFailedItem']):
    """

    success: List["AttributeValue"]
    failed: List["AttributesUpdateResultFailedItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = []
        for success_item_data in self.success:
            success_item = success_item_data.to_dict()

            success.append(success_item)

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()

            failed.append(failed_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_value import AttributeValue
        from ..models.attributes_update_result_failed_item import (
            AttributesUpdateResultFailedItem,
        )

        d = src_dict.copy()
        success = []
        _success = d.pop("success")
        for success_item_data in _success:
            success_item = AttributeValue.from_dict(success_item_data)

            success.append(success_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = AttributesUpdateResultFailedItem.from_dict(failed_item_data)

            failed.append(failed_item)

        attributes_update_result = cls(
            success=success,
            failed=failed,
        )

        attributes_update_result.additional_properties = d
        return attributes_update_result

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
