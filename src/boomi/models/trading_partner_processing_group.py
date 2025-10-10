
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .processing_group_default_routing import ProcessingGroupDefaultRouting
from .processing_group_document_based_routing import ProcessingGroupDocumentBasedRouting
from .processing_group_partner_based_routing import ProcessingGroupPartnerBasedRouting
from .processing_group_trading_partners import ProcessingGroupTradingPartners


@JsonMap(
    {
        "default_routing": "DefaultRouting",
        "document_routing": "DocumentRouting",
        "partner_routing": "PartnerRouting",
        "trading_partners": "TradingPartners",
        "component_id": "componentId",
        "component_name": "componentName",
        "folder_id": "folderId",
        "folder_name": "folderName",
    }
)
class TradingPartnerProcessingGroup(BaseModel):
    """TradingPartnerProcessingGroup

    :param default_routing: default_routing, defaults to None
    :type default_routing: ProcessingGroupDefaultRouting, optional
    :param document_routing: document_routing, defaults to None
    :type document_routing: ProcessingGroupDocumentBasedRouting, optional
    :param partner_routing: partner_routing, defaults to None
    :type partner_routing: ProcessingGroupPartnerBasedRouting, optional
    :param trading_partners: trading_partners, defaults to None
    :type trading_partners: ProcessingGroupTradingPartners, optional
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
        default_routing: ProcessingGroupDefaultRouting = SENTINEL,
        document_routing: ProcessingGroupDocumentBasedRouting = SENTINEL,
        partner_routing: ProcessingGroupPartnerBasedRouting = SENTINEL,
        trading_partners: ProcessingGroupTradingPartners = SENTINEL,
        component_id: str = SENTINEL,
        component_name: str = SENTINEL,
        deleted: bool = SENTINEL,
        description: str = SENTINEL,
        folder_id: int = SENTINEL,
        folder_name: str = SENTINEL,
        **kwargs,
    ):
        """TradingPartnerProcessingGroup

        :param default_routing: default_routing, defaults to None
        :type default_routing: ProcessingGroupDefaultRouting, optional
        :param document_routing: document_routing, defaults to None
        :type document_routing: ProcessingGroupDocumentBasedRouting, optional
        :param partner_routing: partner_routing, defaults to None
        :type partner_routing: ProcessingGroupPartnerBasedRouting, optional
        :param trading_partners: trading_partners, defaults to None
        :type trading_partners: ProcessingGroupTradingPartners, optional
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
        if default_routing is not SENTINEL:
            self.default_routing = self._define_object(
                default_routing, ProcessingGroupDefaultRouting
            )
        if document_routing is not SENTINEL:
            self.document_routing = self._define_object(
                document_routing, ProcessingGroupDocumentBasedRouting
            )
        if partner_routing is not SENTINEL:
            self.partner_routing = self._define_object(
                partner_routing, ProcessingGroupPartnerBasedRouting
            )
        if trading_partners is not SENTINEL:
            self.trading_partners = self._define_object(
                trading_partners, ProcessingGroupTradingPartners
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
        self._kwargs = kwargs
