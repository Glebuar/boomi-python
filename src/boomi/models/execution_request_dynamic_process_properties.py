
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .dynamic_process_property import DynamicProcessProperty


@JsonMap({"dynamic_process_property": "DynamicProcessProperty"})
class ExecutionRequestDynamicProcessProperties(BaseModel):
    """The full list of Dynamic Process properties within the specified Runtime, Runtime cluster, or cloud, where each property is defined by their name and value.

    :param dynamic_process_property: dynamic_process_property, defaults to None
    :type dynamic_process_property: List[DynamicProcessProperty], optional
    """

    def __init__(
        self,
        dynamic_process_property: List[DynamicProcessProperty] = SENTINEL,
        **kwargs,
    ):
        """The full list of Dynamic Process properties within the specified Runtime, Runtime cluster, or cloud, where each property is defined by their name and value.

        :param dynamic_process_property: dynamic_process_property, defaults to None
        :type dynamic_process_property: List[DynamicProcessProperty], optional
        """
        if dynamic_process_property is not SENTINEL:
            self.dynamic_process_property = self._define_list(
                dynamic_process_property, DynamicProcessProperty
            )
        self._kwargs = kwargs
