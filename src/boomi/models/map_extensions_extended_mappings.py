
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_mapping import MapExtensionsMapping


@JsonMap({"mapping": "Mapping"})
class MapExtensionsExtendedMappings(BaseModel):
    """Represents the field mappings between profiles, functions or both. You can use the following attributes:

    - fromXPath - represents the source profile's field path or the function's output key from which you are mapping.
    - toXPath - represents the destination profile's field path or the function's input key to which you are mapping.
    - toFunction - represents the function ID from which you are mapping.
    - fromFunction - represents the function ID to which you are mapping.

    To properly define each of these attributes, see the section [How to configure ExtendedMappings](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension#how-to-configure-extendedmappings)

    :param mapping: mapping, defaults to None
    :type mapping: List[MapExtensionsMapping], optional
    """

    def __init__(self, mapping: List[MapExtensionsMapping] = SENTINEL, **kwargs):
        """Represents the field mappings between profiles, functions or both. You can use the following attributes:

        - fromXPath - represents the source profile's field path or the function's output key from which you are mapping.
        - toXPath - represents the destination profile's field path or the function's input key to which you are mapping.
        - toFunction - represents the function ID from which you are mapping.
        - fromFunction - represents the function ID to which you are mapping.

        To properly define each of these attributes, see the section [How to configure ExtendedMappings](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension#how-to-configure-extendedmappings)

        :param mapping: mapping, defaults to None
        :type mapping: List[MapExtensionsMapping], optional
        """
        if mapping is not SENTINEL:
            self.mapping = self._define_list(mapping, MapExtensionsMapping)
        self._kwargs = kwargs
