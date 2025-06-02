
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extension import MapExtension


@JsonMap(
    {
        "map": "Map",
        "environment_id": "environmentId",
        "extension_group_id": "extensionGroupId",
        "id_": "id",
        "map_id": "mapId",
        "process_id": "processId",
    }
)
class EnvironmentMapExtension(BaseModel):
    """EnvironmentMapExtension

    :param map: map, defaults to None
    :type map: MapExtension, optional
    :param environment_id: The ID of the environment., defaults to None
    :type environment_id: str, optional
    :param extension_group_id: The ID of the multi-install integration pack to which the extensible map applies, if applicable., defaults to None
    :type extension_group_id: str, optional
    :param id_: The ID of the object. This is a conceptual ID synthesized from the IDs of the Map, Process, Multi-install integration pack \(extensionGroupId\), and, if applicable Environment. After obtaining this value with a QUERY operation on the [Environment Map Extensions Summary object](/api/platformapi#tag/EnvironmentMapExtensionsSummary), you can retrieve or update the extensible map by specifying the ID in a GET or UPDATE operation on this object, defaults to None
    :type id_: str, optional
    :param map_id: The ID of the extensible map., defaults to None
    :type map_id: str, optional
    :param name: The name of the extensible map. This variable includes the source object definition name and the destination object definition name, separated by a hyphen., defaults to None
    :type name: str, optional
    :param process_id: The ID of the process., defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        map: MapExtension = SENTINEL,
        environment_id: str = SENTINEL,
        extension_group_id: str = SENTINEL,
        id_: str = SENTINEL,
        map_id: str = SENTINEL,
        name: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtension

        :param map: map, defaults to None
        :type map: MapExtension, optional
        :param environment_id: The ID of the environment., defaults to None
        :type environment_id: str, optional
        :param extension_group_id: The ID of the multi-install integration pack to which the extensible map applies, if applicable., defaults to None
        :type extension_group_id: str, optional
        :param id_: The ID of the object. This is a conceptual ID synthesized from the IDs of the Map, Process, Multi-install integration pack \(extensionGroupId\), and, if applicable Environment. After obtaining this value with a QUERY operation on the [Environment Map Extensions Summary object](/api/platformapi#tag/EnvironmentMapExtensionsSummary), you can retrieve or update the extensible map by specifying the ID in a GET or UPDATE operation on this object, defaults to None
        :type id_: str, optional
        :param map_id: The ID of the extensible map., defaults to None
        :type map_id: str, optional
        :param name: The name of the extensible map. This variable includes the source object definition name and the destination object definition name, separated by a hyphen., defaults to None
        :type name: str, optional
        :param process_id: The ID of the process., defaults to None
        :type process_id: str, optional
        """
        if map is not SENTINEL:
            self.map = self._define_object(map, MapExtension)
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if extension_group_id is not SENTINEL:
            self.extension_group_id = extension_group_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if map_id is not SENTINEL:
            self.map_id = map_id
        if name is not SENTINEL:
            self.name = name
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
