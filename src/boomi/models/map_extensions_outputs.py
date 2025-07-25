
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_output import MapExtensionsOutput


@JsonMap({"output": "Output"})
class MapExtensionsOutputs(BaseModel):
    """Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. See the following row for more information. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.

     The maximum number of inputs or outputs is 100.

    :param output: output, defaults to None
    :type output: List[MapExtensionsOutput], optional
    """

    def __init__(self, output: List[MapExtensionsOutput] = SENTINEL, **kwargs):
        """Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. See the following row for more information. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.

         The maximum number of inputs or outputs is 100.

        :param output: output, defaults to None
        :type output: List[MapExtensionsOutput], optional
        """
        if output is not SENTINEL:
            self.output = self._define_list(output, MapExtensionsOutput)
        self._kwargs = kwargs
