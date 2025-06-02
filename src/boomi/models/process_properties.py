
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .process_property import ProcessProperty


@JsonMap({"process_property": "ProcessProperty"})
class ProcessProperties(BaseModel):
    """The complete list of Persisted Process properties within the specified Runtime, Runtime cluster, or cloud, where the definition of each property is by its name and value.

    :param process_property: process_property, defaults to None
    :type process_property: List[ProcessProperty], optional
    """

    def __init__(self, process_property: List[ProcessProperty] = SENTINEL, **kwargs):
        """The complete list of Persisted Process properties within the specified Runtime, Runtime cluster, or cloud, where the definition of each property is by its name and value.

        :param process_property: process_property, defaults to None
        :type process_property: List[ProcessProperty], optional
        """
        if process_property is not SENTINEL:
            self.process_property = self._define_list(process_property, ProcessProperty)
        self._kwargs = kwargs
