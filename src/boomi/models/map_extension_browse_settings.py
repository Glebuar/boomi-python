
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extension_browse import MapExtensionBrowse


@JsonMap(
    {
        "destination_browse": "DestinationBrowse",
        "source_browse": "SourceBrowse",
        "container_id": "containerId",
    }
)
class MapExtensionBrowseSettings(BaseModel):
    """Represents the Connection information and is used to re-import newly-appended profile fields. This attribute is only applicable for certain application Connectors. To perform a re-import, the client must use the EXECUTE operation. For more information, see the Customizing profiles section later in this topic.

     **Note:** `containerId` is a required field when using BrowseSettings.

    :param destination_browse: destination_browse
    :type destination_browse: MapExtensionBrowse
    :param source_browse: source_browse
    :type source_browse: MapExtensionBrowse
    :param container_id: container_id, defaults to None
    :type container_id: str, optional
    """

    def __init__(
        self,
        destination_browse: MapExtensionBrowse,
        source_browse: MapExtensionBrowse,
        container_id: str = SENTINEL,
        **kwargs,
    ):
        """Represents the Connection information and is used to re-import newly-appended profile fields. This attribute is only applicable for certain application Connectors. To perform a re-import, the client must use the EXECUTE operation. For more information, see the Customizing profiles section later in this topic.

         **Note:** `containerId` is a required field when using BrowseSettings.

        :param destination_browse: destination_browse
        :type destination_browse: MapExtensionBrowse
        :param source_browse: source_browse
        :type source_browse: MapExtensionBrowse
        :param container_id: container_id, defaults to None
        :type container_id: str, optional
        """
        self.destination_browse = self._define_object(
            destination_browse, MapExtensionBrowse
        )
        self.source_browse = self._define_object(source_browse, MapExtensionBrowse)
        if container_id is not SENTINEL:
            self.container_id = container_id
        self._kwargs = kwargs
