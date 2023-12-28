from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_attributes_response_200_results_item import (
        GetAttributesResponse200ResultsItem,
    )


T = TypeVar("T", bound="GetAttributesResponse200")


@_attrs_define
class GetAttributesResponse200:
    """
    Attributes:
        count (int):
        results (List['GetAttributesResponse200ResultsItem']):
        next_ (Optional[str]):
        previous (Optional[str]):
    """

    count: int
    results: List["GetAttributesResponse200ResultsItem"]
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
        from ..models.get_attributes_response_200_results_item import (
            GetAttributesResponse200ResultsItem,
        )

        d = src_dict.copy()
        count = d.pop("count")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = GetAttributesResponse200ResultsItem.from_dict(
                results_item_data
            )

            results.append(results_item)

        next_ = d.pop("next")

        previous = d.pop("previous")

        get_attributes_response_200 = cls(
            count=count,
            results=results,
            next_=next_,
            previous=previous,
        )

        get_attributes_response_200.additional_properties = d
        return get_attributes_response_200

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
