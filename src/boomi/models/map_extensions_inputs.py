
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_input import MapExtensionsInput


@JsonMap({"input": "Input"})
class MapExtensionsInputs(BaseModel):
    """Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.

     The maximum number of inputs or outputs is 100.

    :param input: input, defaults to None
    :type input: List[MapExtensionsInput], optional
    """

    def __init__(self, input: List[MapExtensionsInput] = SENTINEL, **kwargs):
        """Lists the function's input and outputs according to their user-given names and keys. You must list inputs and outputs sequentially in order according to their key values. When creating or updating functions, it requires all input and output values in the request regardless if they are to be mapped or populated with a default value.

         The maximum number of inputs or outputs is 100.

        :param input: input, defaults to None
        :type input: List[MapExtensionsInput], optional
        """
        if input is not SENTINEL:
            self.input = self._define_list(input, MapExtensionsInput)
        self._kwargs = kwargs
