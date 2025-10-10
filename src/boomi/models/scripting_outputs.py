
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .scripting_parameter import ScriptingParameter


@JsonMap({"output": "Output"})
class ScriptingOutputs(BaseModel):
    """ScriptingOutputs

    :param output: output, defaults to None
    :type output: List[ScriptingParameter], optional
    """

    def __init__(self, output: List[ScriptingParameter] = SENTINEL, **kwargs):
        """ScriptingOutputs

        :param output: output, defaults to None
        :type output: List[ScriptingParameter], optional
        """
        if output is not SENTINEL:
            self.output = self._define_list(output, ScriptingParameter)
        self._kwargs = kwargs
