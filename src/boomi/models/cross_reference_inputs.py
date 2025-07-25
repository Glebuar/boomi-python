
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cross_reference_parameter import CrossReferenceParameter


@JsonMap({"input": "Input"})
class CrossReferenceInputs(BaseModel):
    """CrossReferenceInputs

    :param input: input, defaults to None
    :type input: List[CrossReferenceParameter], optional
    """

    def __init__(self, input: List[CrossReferenceParameter] = SENTINEL, **kwargs):
        """CrossReferenceInputs

        :param input: input, defaults to None
        :type input: List[CrossReferenceParameter], optional
        """
        if input is not SENTINEL:
            self.input = self._define_list(input, CrossReferenceParameter)
        self._kwargs = kwargs
