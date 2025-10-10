
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .partner_document_type import PartnerDocumentType


@JsonMap({"partner_document_type": "PartnerDocumentType"})
class PartnerDocumentTypes(BaseModel):
    """PartnerDocumentTypes

    :param partner_document_type: partner_document_type, defaults to None
    :type partner_document_type: List[PartnerDocumentType], optional
    """

    def __init__(
        self, partner_document_type: List[PartnerDocumentType] = SENTINEL, **kwargs
    ):
        """PartnerDocumentTypes

        :param partner_document_type: partner_document_type, defaults to None
        :type partner_document_type: List[PartnerDocumentType], optional
        """
        if partner_document_type is not SENTINEL:
            self.partner_document_type = self._define_list(
                partner_document_type, PartnerDocumentType
            )
        self._kwargs = kwargs
