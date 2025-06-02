
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .process_property_value import ProcessPropertyValue


@JsonMap(
    {"process_property_value": "ProcessPropertyValue", "component_id": "componentId"}
)
class ProcessProperty(BaseModel):
    """ProcessProperty

    :param process_property_value: process_property_value, defaults to None
    :type process_property_value: List[ProcessPropertyValue], optional
    :param component_id: component_id, defaults to None
    :type component_id: str, optional
    """

    def __init__(
        self,
        process_property_value: List[ProcessPropertyValue] = SENTINEL,
        component_id: str = SENTINEL,
        **kwargs,
    ):
        """ProcessProperty

        :param process_property_value: process_property_value, defaults to None
        :type process_property_value: List[ProcessPropertyValue], optional
        :param component_id: component_id, defaults to None
        :type component_id: str, optional
        """
        if process_property_value is not SENTINEL:
            self.process_property_value = self._define_list(
                process_property_value, ProcessPropertyValue
            )
        if component_id is not SENTINEL:
            self.component_id = component_id
        self._kwargs = kwargs
