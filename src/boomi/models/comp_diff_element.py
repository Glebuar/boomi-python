
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .comp_diff_attribute import CompDiffAttribute


@JsonMap({"comp_diff_attribute": "CompDiffAttribute"})
class CompDiffElement(BaseModel):
    """CompDiffElement

    :param comp_diff_attribute: comp_diff_attribute, defaults to None
    :type comp_diff_attribute: List[CompDiffAttribute], optional
    :param ignored: ignored, defaults to None
    :type ignored: bool, optional
    :param name: The tag name of the element that you want to target for the comparative diff results., defaults to None
    :type name: str, optional
    :param ordered: ordered, defaults to None
    :type ordered: bool, optional
    :param parent: The parent element for the element that you want to configure for the comparative diff results., defaults to None
    :type parent: str, optional
    """

    def __init__(
        self,
        comp_diff_attribute: List[CompDiffAttribute] = SENTINEL,
        ignored: bool = SENTINEL,
        name: str = SENTINEL,
        ordered: bool = SENTINEL,
        parent: str = SENTINEL,
        **kwargs,
    ):
        """CompDiffElement

        :param comp_diff_attribute: comp_diff_attribute, defaults to None
        :type comp_diff_attribute: List[CompDiffAttribute], optional
        :param ignored: ignored, defaults to None
        :type ignored: bool, optional
        :param name: The tag name of the element that you want to target for the comparative diff results., defaults to None
        :type name: str, optional
        :param ordered: ordered, defaults to None
        :type ordered: bool, optional
        :param parent: The parent element for the element that you want to configure for the comparative diff results., defaults to None
        :type parent: str, optional
        """
        if comp_diff_attribute is not SENTINEL:
            self.comp_diff_attribute = self._define_list(
                comp_diff_attribute, CompDiffAttribute
            )
        if ignored is not SENTINEL:
            self.ignored = ignored
        if name is not SENTINEL:
            self.name = name
        if ordered is not SENTINEL:
            self.ordered = ordered
        if parent is not SENTINEL:
            self.parent = parent
        self._kwargs = kwargs
