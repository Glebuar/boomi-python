
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cross_reference import CrossReference


@JsonMap({"cross_reference": "crossReference"})
class CrossReferences(BaseModel):
    """CrossReferences

    :param cross_reference: cross_reference, defaults to None
    :type cross_reference: List[CrossReference], optional
    """

    def __init__(self, cross_reference: List[CrossReference] = SENTINEL, **kwargs):
        """CrossReferences

        :param cross_reference: cross_reference, defaults to None
        :type cross_reference: List[CrossReference], optional
        """
        if cross_reference is not SENTINEL:
            self.cross_reference = self._define_list(cross_reference, CrossReference)
        self._kwargs = kwargs
