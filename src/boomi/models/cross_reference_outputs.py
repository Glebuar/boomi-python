
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cross_reference_parameter import CrossReferenceParameter


@JsonMap({"output": "Output"})
class CrossReferenceOutputs(BaseModel):
    """CrossReferenceOutputs

    :param output: output, defaults to None
    :type output: List[CrossReferenceParameter], optional
    """

    def __init__(self, output: List[CrossReferenceParameter] = SENTINEL, **kwargs):
        """CrossReferenceOutputs

        :param output: output, defaults to None
        :type output: List[CrossReferenceParameter], optional
        """
        if output is not SENTINEL:
            self.output = self._define_list(output, CrossReferenceParameter)
        self._kwargs = kwargs
