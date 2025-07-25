
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .processing_group_document_partner_route import ProcessingGroupDocumentPartnerRoute


@JsonMap(
    {
        "partner_route": "PartnerRoute",
        "document_type": "documentType",
        "process_id": "processId",
    }
)
class ProcessingGroupDocumentTypeRoute(BaseModel):
    """ProcessingGroupDocumentTypeRoute

    :param partner_route: partner_route, defaults to None
    :type partner_route: List[ProcessingGroupDocumentPartnerRoute], optional
    :param document_type: document_type, defaults to None
    :type document_type: str, optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        partner_route: List[ProcessingGroupDocumentPartnerRoute] = SENTINEL,
        document_type: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs,
    ):
        """ProcessingGroupDocumentTypeRoute

        :param partner_route: partner_route, defaults to None
        :type partner_route: List[ProcessingGroupDocumentPartnerRoute], optional
        :param document_type: document_type, defaults to None
        :type document_type: str, optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        """
        if partner_route is not SENTINEL:
            self.partner_route = self._define_list(
                partner_route, ProcessingGroupDocumentPartnerRoute
            )
        if document_type is not SENTINEL:
            self.document_type = document_type
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
