from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attribute_acquisition_response_failed_item import (
        AttributeAcquisitionResponseFailedItem,
    )
    from ..models.attribute_acquisition_response_success_item import (
        AttributeAcquisitionResponseSuccessItem,
    )


T = TypeVar("T", bound="AttributeAcquisitionResponse")


@_attrs_define
class AttributeAcquisitionResponse:
    """
    Attributes:
        success (List['AttributeAcquisitionResponseSuccessItem']):
        failed (List['AttributeAcquisitionResponseFailedItem']):
    """

    success: List["AttributeAcquisitionResponseSuccessItem"]
    failed: List["AttributeAcquisitionResponseFailedItem"]
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
        from ..models.attribute_acquisition_response_failed_item import (
            AttributeAcquisitionResponseFailedItem,
        )
        from ..models.attribute_acquisition_response_success_item import (
            AttributeAcquisitionResponseSuccessItem,
        )

        d = src_dict.copy()
        success = []
        _success = d.pop("success")
        for success_item_data in _success:
            success_item = AttributeAcquisitionResponseSuccessItem.from_dict(
                success_item_data
            )

            success.append(success_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = AttributeAcquisitionResponseFailedItem.from_dict(
                failed_item_data
            )

            failed.append(failed_item)

        attribute_acquisition_response = cls(
            success=success,
            failed=failed,
        )

        attribute_acquisition_response.additional_properties = d
        return attribute_acquisition_response

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
