from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attribute import Attribute


T = TypeVar("T", bound="AttributesGetResult")


@_attrs_define
class AttributesGetResult:
    """
    Attributes:
        count (int):
        results (List['Attribute']):
        next_ (Optional[str]):
        previous (Optional[str]):
    """

    count: int
    results: List["Attribute"]
    next_: Optional[str]
    previous: Optional[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        next_ = self.next_
        previous = self.previous

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "results": results,
                "next": next_,
                "previous": previous,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute import Attribute

        d = src_dict.copy()
        count = d.pop("count")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = Attribute.from_dict(results_item_data)

            results.append(results_item)

        next_ = d.pop("next")

        previous = d.pop("previous")

        attributes_get_result = cls(
            count=count,
            results=results,
            next_=next_,
            previous=previous,
        )

        attributes_get_result.additional_properties = d
        return attributes_get_result

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
