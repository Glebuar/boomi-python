
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extension_browse_data import MapExtensionBrowseData


@JsonMap(
    {
        "destination_field_set": "DestinationFieldSet",
        "source_field_set": "SourceFieldSet",
        "environment_id": "environmentId",
        "extension_group_id": "extensionGroupId",
        "id_": "id",
        "map_id": "mapId",
        "process_id": "processId",
    }
)
class EnvironmentMapExtensionsSummary(BaseModel):
    """EnvironmentMapExtensionsSummary

    :param destination_field_set: Fields defining the credentials for connecting to the external service for the purpose of reimporting the source of destination profile to retrieve custom fields. You use these fields in the Environment Map Extension object's EXECUTE action.
    :type destination_field_set: MapExtensionBrowseData
    :param source_field_set: Fields defining the credentials for connecting to the external service for the purpose of reimporting the source of destination profile to retrieve custom fields. You use these fields in the Environment Map Extension object's EXECUTE action.
    :type source_field_set: MapExtensionBrowseData
    :param environment_id: The ID of the environment., defaults to None
    :type environment_id: str, optional
    :param extension_group_id: If applicable, the ID of the multi-install integration pack to which the extensible map applies., defaults to None
    :type extension_group_id: str, optional
    :param id_: The ID of the object.This is a conceptual ID synthesized from the IDs of the:\<br /\>-   Map\<br /\>-   Process\<br /\>-   Multi-install integration pack \(extensionGroupId\), if applicable\<br /\>-   Environment\<br /\>After obtaining this value with a QUERY operation, you can retrieve or update the extensible map by specifying the ID in a GET or UPDATE operation on an Environment Map Extension object, defaults to None
    :type id_: str, optional
    :param map_id: The ID of the extensible map., defaults to None
    :type map_id: str, optional
    :param name: The name of the extensible map. This name includes the source object definition name and the destination object definition name, separated by a hyphen., defaults to None
    :type name: str, optional
    :param process_id: The ID of the process., defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        destination_field_set: MapExtensionBrowseData,
        source_field_set: MapExtensionBrowseData,
        environment_id: str = SENTINEL,
        extension_group_id: str = SENTINEL,
        id_: str = SENTINEL,
        map_id: str = SENTINEL,
        name: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtensionsSummary

        :param destination_field_set: Fields defining the credentials for connecting to the external service for the purpose of reimporting the source of destination profile to retrieve custom fields. You use these fields in the Environment Map Extension object's EXECUTE action.
        :type destination_field_set: MapExtensionBrowseData
        :param source_field_set: Fields defining the credentials for connecting to the external service for the purpose of reimporting the source of destination profile to retrieve custom fields. You use these fields in the Environment Map Extension object's EXECUTE action.
        :type source_field_set: MapExtensionBrowseData
        :param environment_id: The ID of the environment., defaults to None
        :type environment_id: str, optional
        :param extension_group_id: If applicable, the ID of the multi-install integration pack to which the extensible map applies., defaults to None
        :type extension_group_id: str, optional
        :param id_: The ID of the object.This is a conceptual ID synthesized from the IDs of the:\<br /\>-   Map\<br /\>-   Process\<br /\>-   Multi-install integration pack \(extensionGroupId\), if applicable\<br /\>-   Environment\<br /\>After obtaining this value with a QUERY operation, you can retrieve or update the extensible map by specifying the ID in a GET or UPDATE operation on an Environment Map Extension object, defaults to None
        :type id_: str, optional
        :param map_id: The ID of the extensible map., defaults to None
        :type map_id: str, optional
        :param name: The name of the extensible map. This name includes the source object definition name and the destination object definition name, separated by a hyphen., defaults to None
        :type name: str, optional
        :param process_id: The ID of the process., defaults to None
        :type process_id: str, optional
        """
        self.destination_field_set = self._define_object(
            destination_field_set, MapExtensionBrowseData
        )
        self.source_field_set = self._define_object(
            source_field_set, MapExtensionBrowseData
        )
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
