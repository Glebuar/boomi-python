
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .partner_archiving import PartnerArchiving
from .partner_communication import PartnerCommunication


@JsonMap(
    {
        "partner_archiving": "PartnerArchiving",
        "partner_communication": "PartnerCommunication",
        "communication_type": "communicationType",
        "component_id": "componentId",
        "component_name": "componentName",
        "folder_id": "folderId",
        "folder_name": "folderName",
    }
)
class SharedCommunicationChannelComponent(BaseModel):
    """SharedCommunicationChannelComponent

    :param partner_archiving: partner_archiving
    :type partner_archiving: PartnerArchiving
    :param partner_communication: partner_communication
    :type partner_communication: PartnerCommunication
    :param communication_type: communication_type, defaults to None
    :type communication_type: str, optional
    :param component_id: component_id, defaults to None
    :type component_id: str, optional
    :param component_name: component_name, defaults to None
    :type component_name: str, optional
    :param deleted: deleted, defaults to None
    :type deleted: bool, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param folder_id: folder_id, defaults to None
    :type folder_id: int, optional
    :param folder_name: folder_name, defaults to None
    :type folder_name: str, optional
    """

    def __init__(
        self,
        partner_archiving: PartnerArchiving,
        partner_communication: PartnerCommunication,
        communication_type: str = SENTINEL,
        component_id: str = SENTINEL,
        component_name: str = SENTINEL,
        deleted: bool = SENTINEL,
        description: str = SENTINEL,
        folder_id: int = SENTINEL,
        folder_name: str = SENTINEL,
        **kwargs,
    ):
        """SharedCommunicationChannelComponent

        :param partner_archiving: partner_archiving
        :type partner_archiving: PartnerArchiving
        :param partner_communication: partner_communication
        :type partner_communication: PartnerCommunication
        :param communication_type: communication_type, defaults to None
        :type communication_type: str, optional
        :param component_id: component_id, defaults to None
        :type component_id: str, optional
        :param component_name: component_name, defaults to None
        :type component_name: str, optional
        :param deleted: deleted, defaults to None
        :type deleted: bool, optional
        :param description: description, defaults to None
        :type description: str, optional
        :param folder_id: folder_id, defaults to None
        :type folder_id: int, optional
        :param folder_name: folder_name, defaults to None
        :type folder_name: str, optional
        """
        self.partner_archiving = self._define_object(
            partner_archiving, PartnerArchiving
        )
        self.partner_communication = self._define_object(
            partner_communication, PartnerCommunication
        )
        if communication_type is not SENTINEL:
            self.communication_type = communication_type
        if component_id is not SENTINEL:
            self.component_id = component_id
        if component_name is not SENTINEL:
            self.component_name = component_name
        if deleted is not SENTINEL:
            self.deleted = deleted
        if description is not SENTINEL:
            self.description = description
        if folder_id is not SENTINEL:
            self.folder_id = folder_id
        if folder_name is not SENTINEL:
            self.folder_name = folder_name
        self._kwargs = kwargs
