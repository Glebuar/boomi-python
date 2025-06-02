
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_function_mapping import MapExtensionsFunctionMapping


@JsonMap({"mapping": "Mapping"})
class MapExtensionsFunctionMappings(BaseModel):
    """Defines the mapping of inputs and outputs for the user-defined function and each function step. It uses the following attributes:

     1. fromFunction - represents the function ID from which you are mapping.
     2. fromKey - represents the function's output key from which you are mapping.
     3. toFunction - represents the function ID to which you are mapping.
     4. toKey - represents the function's input key to which you are mapping.

    :param mapping: mapping, defaults to None
    :type mapping: List[MapExtensionsFunctionMapping], optional
    """

    def __init__(
        self, mapping: List[MapExtensionsFunctionMapping] = SENTINEL, **kwargs
    ):
        """Defines the mapping of inputs and outputs for the user-defined function and each function step. It uses the following attributes:

         1. fromFunction - represents the function ID from which you are mapping.
         2. fromKey - represents the function's output key from which you are mapping.
         3. toFunction - represents the function ID to which you are mapping.
         4. toKey - represents the function's input key to which you are mapping.

        :param mapping: mapping, defaults to None
        :type mapping: List[MapExtensionsFunctionMapping], optional
        """
        if mapping is not SENTINEL:
            self.mapping = self._define_list(mapping, MapExtensionsFunctionMapping)
        self._kwargs = kwargs
