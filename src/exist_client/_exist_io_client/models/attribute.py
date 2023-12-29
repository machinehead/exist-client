from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attribute_group import AttributeGroup


T = TypeVar("T", bound="Attribute")


@_attrs_define
class Attribute:
    """
    Attributes:
        name (str):
        label (str):
        group (AttributeGroup):
        value_type_description (str):
        template (Optional[str]):
    """

    name: str
    label: str
    group: "AttributeGroup"
    value_type_description: str
    template: Optional[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        label = self.label
        group = self.group.to_dict()

        value_type_description = self.value_type_description
        template = self.template

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "label": label,
                "group": group,
                "value_type_description": value_type_description,
                "template": template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute_group import AttributeGroup

        d = src_dict.copy()
        name = d.pop("name")

        label = d.pop("label")

        group = AttributeGroup.from_dict(d.pop("group"))

        value_type_description = d.pop("value_type_description")

        template = d.pop("template")

        attribute = cls(
            name=name,
            label=label,
            group=group,
            value_type_description=value_type_description,
            template=template,
        )

        attribute.additional_properties = d
        return attribute

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
