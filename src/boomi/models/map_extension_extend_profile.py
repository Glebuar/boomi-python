
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_extended_node import MapExtensionsExtendedNode


@JsonMap({"node": "Node"})
class MapExtensionExtendProfile(BaseModel):
    """Contains the user-defined custom fields for the source or destination profile. Applicable only to Flat File profiles. Represents the field and value configuration settings manually specified in the source or destination profile's Data Element tab. For more information, refer to [Customizing Profiles](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension).

    :param node: node, defaults to None
    :type node: List[MapExtensionsExtendedNode], optional
    """

    def __init__(self, node: List[MapExtensionsExtendedNode] = SENTINEL, **kwargs):
        """Contains the user-defined custom fields for the source or destination profile. Applicable only to Flat File profiles. Represents the field and value configuration settings manually specified in the source or destination profile's Data Element tab. For more information, refer to [Customizing Profiles](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension).

        :param node: node, defaults to None
        :type node: List[MapExtensionsExtendedNode], optional
        """
        if node is not SENTINEL:
            self.node = self._define_list(node, MapExtensionsExtendedNode)
        self._kwargs = kwargs
