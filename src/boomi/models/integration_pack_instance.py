
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .process_id import ProcessId


@JsonMap(
    {
        "process_id": "ProcessId",
        "id_": "id",
        "integration_pack_id": "integrationPackId",
        "integration_pack_override_name": "integrationPackOverrideName",
    }
)
class IntegrationPackInstance(BaseModel):
    """IntegrationPackInstance

    :param process_id: A list of process IDs associated with the integration pack instance, defaults to None
    :type process_id: List[ProcessId], optional
    :param id_: A unique ID assigned by the system to the installed instance of the integration pack. This field populates only if you install the integration pack in the requesting account., defaults to None
    :type id_: str, optional
    :param integration_pack_id: A unique ID assigned by the system to the integration pack., defaults to None
    :type integration_pack_id: str, optional
    :param integration_pack_override_name: The name of the installed instance of the integration pack. You can set this value only in the case of multi-install integration packs; its purpose is to distinguish between instances., defaults to None
    :type integration_pack_override_name: str, optional
    """

    def __init__(
        self,
        process_id: List[ProcessId] = SENTINEL,
        id_: str = SENTINEL,
        integration_pack_id: str = SENTINEL,
        integration_pack_override_name: str = SENTINEL,
        **kwargs,
    ):
        """IntegrationPackInstance

        :param process_id: A list of process IDs associated with the integration pack instance, defaults to None
        :type process_id: List[ProcessId], optional
        :param id_: A unique ID assigned by the system to the installed instance of the integration pack. This field populates only if you install the integration pack in the requesting account., defaults to None
        :type id_: str, optional
        :param integration_pack_id: A unique ID assigned by the system to the integration pack., defaults to None
        :type integration_pack_id: str, optional
        :param integration_pack_override_name: The name of the installed instance of the integration pack. You can set this value only in the case of multi-install integration packs; its purpose is to distinguish between instances., defaults to None
        :type integration_pack_override_name: str, optional
        """
        if process_id is not SENTINEL:
            self.process_id = self._define_list(process_id, ProcessId)
        if id_ is not SENTINEL:
            self.id_ = id_
        if integration_pack_id is not SENTINEL:
            self.integration_pack_id = integration_pack_id
        if integration_pack_override_name is not SENTINEL:
            self.integration_pack_override_name = integration_pack_override_name
        self._kwargs = kwargs
