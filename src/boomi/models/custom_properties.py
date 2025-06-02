
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .property_pair import PropertyPair


@JsonMap({})
class CustomProperties(BaseModel):
    """CustomProperties

    :param properties: properties, defaults to None
    :type properties: List[PropertyPair], optional
    """

    def __init__(self, properties: List[PropertyPair] = SENTINEL, **kwargs):
        """CustomProperties

        :param properties: properties, defaults to None
        :type properties: List[PropertyPair], optional
        """
        if properties is not SENTINEL:
            self.properties = self._define_list(properties, PropertyPair)
        self._kwargs = kwargs
