
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .property import Property


@JsonMap({"property": "Property", "id_": "id"})
class AtomStartupProperties(BaseModel):
    """AtomStartupProperties

    :param property: property, defaults to None
    :type property: List[Property], optional
    :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud. (This API is not applicable for runtimes attached to clouds)., defaults to None
    :type id_: str, optional
    """

    def __init__(
        self, property: List[Property] = SENTINEL, id_: str = SENTINEL, **kwargs
    ):
        """AtomStartupProperties

        :param property: property, defaults to None
        :type property: List[Property], optional
        :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud. (This API is not applicable for runtimes attached to clouds)., defaults to None
        :type id_: str, optional
        """
        if property is not SENTINEL:
            self.property = self._define_list(property, Property)
        if id_ is not SENTINEL:
            self.id_ = id_
        self._kwargs = kwargs
