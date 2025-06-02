
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .process_property_value import ProcessPropertyValue


@JsonMap({"process_property_value": "ProcessPropertyValue", "id_": "id"})
class OverrideProcessProperty(BaseModel):
    """OverrideProcessProperty

    :param process_property_value: process_property_value, defaults to None
    :type process_property_value: List[ProcessPropertyValue], optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        process_property_value: List[ProcessPropertyValue] = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        **kwargs,
    ):
        """OverrideProcessProperty

        :param process_property_value: process_property_value, defaults to None
        :type process_property_value: List[ProcessPropertyValue], optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if process_property_value is not SENTINEL:
            self.process_property_value = self._define_list(
                process_property_value, ProcessPropertyValue
            )
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
