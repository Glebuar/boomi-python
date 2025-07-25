
from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .contact_info import ContactInfo
from .partner_communication import PartnerCommunication
from .partner_document_types import PartnerDocumentTypes
from .partner_info import PartnerInfo


class TradingPartnerComponentClassification(Enum):
    """An enumeration representing different categories.

    :cvar TRADINGPARTNER: "tradingpartner"
    :vartype TRADINGPARTNER: str
    :cvar MYCOMPANY: "mycompany"
    :vartype MYCOMPANY: str
    """

    TRADINGPARTNER = "tradingpartner"
    MYCOMPANY = "mycompany"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                TradingPartnerComponentClassification._member_map_.values(),
            )
        )


class TradingPartnerComponentStandard(Enum):
    """An enumeration representing different categories.

    :cvar X12: "x12"
    :vartype X12: str
    :cvar EDIFACT: "edifact"
    :vartype EDIFACT: str
    :cvar HL7: "hl7"
    :vartype HL7: str
    :cvar CUSTOM: "custom"
    :vartype CUSTOM: str
    :cvar ROSETTANET: "rosettanet"
    :vartype ROSETTANET: str
    :cvar TRADACOMS: "tradacoms"
    :vartype TRADACOMS: str
    :cvar ODETTE: "odette"
    :vartype ODETTE: str
    """

    X12 = "x12"
    EDIFACT = "edifact"
    HL7 = "hl7"
    CUSTOM = "custom"
    ROSETTANET = "rosettanet"
    TRADACOMS = "tradacoms"
    ODETTE = "odette"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, TradingPartnerComponentStandard._member_map_.values()
            )
        )


@JsonMap(
    {
        "contact_info": "ContactInfo",
        "partner_communication": "PartnerCommunication",
        "partner_communication_types": "PartnerCommunicationTypes",
        "partner_document_types": "PartnerDocumentTypes",
        "partner_info": "PartnerInfo",
        "component_id": "componentId",
        "component_name": "componentName",
        "folder_id": "folderId",
        "folder_name": "folderName",
        "organization_id": "organizationId",
    }
)
class TradingPartnerComponent(BaseModel):
    """TradingPartnerComponent

    :param contact_info: contact_info
    :type contact_info: ContactInfo
    :param partner_communication: partner_communication
    :type partner_communication: PartnerCommunication
    :param partner_communication_types: partner_communication_types, defaults to None
    :type partner_communication_types: List[str], optional
    :param partner_document_types: partner_document_types
    :type partner_document_types: PartnerDocumentTypes
    :param partner_info: partner_info
    :type partner_info: PartnerInfo
    :param classification: classification, defaults to None
    :type classification: TradingPartnerComponentClassification, optional
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
    :param identifier: identifier, defaults to None
    :type identifier: str, optional
    :param organization_id: organization_id, defaults to None
    :type organization_id: str, optional
    :param standard: standard, defaults to None
    :type standard: TradingPartnerComponentStandard, optional
    """

    def __init__(
        self,
        contact_info: ContactInfo,
        partner_communication: PartnerCommunication,
        partner_document_types: PartnerDocumentTypes,
        partner_info: PartnerInfo,
        partner_communication_types: List[str] = SENTINEL,
        classification: TradingPartnerComponentClassification = SENTINEL,
        component_id: str = SENTINEL,
        component_name: str = SENTINEL,
        deleted: bool = SENTINEL,
        description: str = SENTINEL,
        folder_id: int = SENTINEL,
        folder_name: str = SENTINEL,
        identifier: str = SENTINEL,
        organization_id: str = SENTINEL,
        standard: TradingPartnerComponentStandard = SENTINEL,
        **kwargs,
    ):
        """TradingPartnerComponent

        :param contact_info: contact_info
        :type contact_info: ContactInfo
        :param partner_communication: partner_communication
        :type partner_communication: PartnerCommunication
        :param partner_communication_types: partner_communication_types, defaults to None
        :type partner_communication_types: List[str], optional
        :param partner_document_types: partner_document_types
        :type partner_document_types: PartnerDocumentTypes
        :param partner_info: partner_info
        :type partner_info: PartnerInfo
        :param classification: classification, defaults to None
        :type classification: TradingPartnerComponentClassification, optional
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
        :param identifier: identifier, defaults to None
        :type identifier: str, optional
        :param organization_id: organization_id, defaults to None
        :type organization_id: str, optional
        :param standard: standard, defaults to None
        :type standard: TradingPartnerComponentStandard, optional
        """
        self.contact_info = self._define_object(contact_info, ContactInfo)
        self.partner_communication = self._define_object(
            partner_communication, PartnerCommunication
        )
        if partner_communication_types is not SENTINEL:
            self.partner_communication_types = partner_communication_types
        self.partner_document_types = self._define_object(
            partner_document_types, PartnerDocumentTypes
        )
        self.partner_info = self._define_object(partner_info, PartnerInfo)
        if classification is not SENTINEL:
            self.classification = self._enum_matching(
                classification,
                TradingPartnerComponentClassification.list(),
                "classification",
            )
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
        if identifier is not SENTINEL:
            self.identifier = identifier
        if organization_id is not SENTINEL:
            self.organization_id = organization_id
        if standard is not SENTINEL:
            self.standard = self._enum_matching(
                standard, TradingPartnerComponentStandard.list(), "standard"
            )
        self._kwargs = kwargs
