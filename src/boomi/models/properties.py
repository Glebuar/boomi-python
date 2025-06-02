
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .property import Property


@JsonMap({})
class Properties(BaseModel):
    """Properties

    :param property: property, defaults to None
    :type property: List[Property], optional
    """

    def __init__(self, property: List[Property] = SENTINEL, **kwargs):
        """Properties

        :param property: property, defaults to None
        :type property: List[Property], optional
        """
        if property is not SENTINEL:
            self.property = self._define_list(property, Property)
        self._kwargs = kwargs
