
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .document import Document


@JsonMap({"document": "Document"})
class SelectedDocuments(BaseModel):
    """You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both. Indicates that the Rerun Document operation reruns only those documents you specify in the `genericConnectorRecordId` value.

    :param document: document, defaults to None
    :type document: List[Document], optional
    """

    def __init__(self, document: List[Document] = SENTINEL, **kwargs):
        """You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both. Indicates that the Rerun Document operation reruns only those documents you specify in the `genericConnectorRecordId` value.

        :param document: document, defaults to None
        :type document: List[Document], optional
        """
        if document is not SENTINEL:
            self.document = self._define_list(document, Document)
        self._kwargs = kwargs
