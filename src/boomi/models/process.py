
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .process_integration_pack_info import ProcessIntegrationPackInfo


@JsonMap(
    {"description": "Description", "integration_pack": "IntegrationPack", "id_": "id"}
)
class Process(BaseModel):
    """Process

    :param description: description
    :type description: str
    :param integration_pack: integration_pack, defaults to None
    :type integration_pack: List[ProcessIntegrationPackInfo], optional
    :param id_: A unique ID assigned by the system to the process. For deployed processes and processes belonging to single-install integration packs, this value is the process component ID.For processes belonging to multi-install integration packs, this is an synthetic ID and does not match an actual process component. You can use this value as the extensionGroupId when querying the Environment Extensions object, defaults to None
    :type id_: str, optional
    :param name: The name of the process., defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        description: str,
        integration_pack: List[ProcessIntegrationPackInfo] = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        **kwargs,
    ):
        """Process

        :param description: description
        :type description: str
        :param integration_pack: integration_pack, defaults to None
        :type integration_pack: List[ProcessIntegrationPackInfo], optional
        :param id_: A unique ID assigned by the system to the process. For deployed processes and processes belonging to single-install integration packs, this value is the process component ID.For processes belonging to multi-install integration packs, this is an synthetic ID and does not match an actual process component. You can use this value as the extensionGroupId when querying the Environment Extensions object, defaults to None
        :type id_: str, optional
        :param name: The name of the process., defaults to None
        :type name: str, optional
        """
        self.description = description
        if integration_pack is not SENTINEL:
            self.integration_pack = self._define_list(
                integration_pack, ProcessIntegrationPackInfo
            )
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
