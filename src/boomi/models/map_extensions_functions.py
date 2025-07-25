
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_function import MapExtensionsFunction


@JsonMap({"function": "Function"})
class MapExtensionsFunctions(BaseModel):
    """The definition of Map function steps used in the Map component. For detailed information about how to define Map functions in a request or response, see the topic [Environment Map Extension functions](/docs/APIs/PlatformAPI/Environment_Map_Extension_functions). You can use the Extended Functions attribute to define the following extensible map functions (supports standard and user-defined function types):

    - User Defined
    - Connector
    - Lookup
    - Date
    - Numeric
    - String
    - Custom Scripting
    - Property

    :param function: function, defaults to None
    :type function: List[MapExtensionsFunction], optional
    """

    def __init__(self, function: List[MapExtensionsFunction] = SENTINEL, **kwargs):
        """The definition of Map function steps used in the Map component. For detailed information about how to define Map functions in a request or response, see the topic [Environment Map Extension functions](/docs/APIs/PlatformAPI/Environment_Map_Extension_functions). You can use the Extended Functions attribute to define the following extensible map functions (supports standard and user-defined function types):

        - User Defined
        - Connector
        - Lookup
        - Date
        - Numeric
        - String
        - Custom Scripting
        - Property

        :param function: function, defaults to None
        :type function: List[MapExtensionsFunction], optional
        """
        if function is not SENTINEL:
            self.function = self._define_list(function, MapExtensionsFunction)
        self._kwargs = kwargs
