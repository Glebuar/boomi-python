
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .override_process_property import OverrideProcessProperty


@JsonMap({"process_property": "ProcessProperty"})
class OverrideProcessProperties(BaseModel):
    """OverrideProcessProperties

    :param process_property: process_property, defaults to None
    :type process_property: List[OverrideProcessProperty], optional
    """

    def __init__(
        self, process_property: List[OverrideProcessProperty] = SENTINEL, **kwargs
    ):
        """OverrideProcessProperties

        :param process_property: process_property, defaults to None
        :type process_property: List[OverrideProcessProperty], optional
        """
        if process_property is not SENTINEL:
            self.process_property = self._define_list(
                process_property, OverrideProcessProperty
            )
        self._kwargs = kwargs
