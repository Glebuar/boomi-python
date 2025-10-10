
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .scripting_parameter import ScriptingParameter


@JsonMap({"input": "Input"})
class ScriptingInputs(BaseModel):
    """ScriptingInputs

    :param input: input, defaults to None
    :type input: List[ScriptingParameter], optional
    """

    def __init__(self, input: List[ScriptingParameter] = SENTINEL, **kwargs):
        """ScriptingInputs

        :param input: input, defaults to None
        :type input: List[ScriptingParameter], optional
        """
        if input is not SENTINEL:
            self.input = self._define_list(input, ScriptingParameter)
        self._kwargs = kwargs
