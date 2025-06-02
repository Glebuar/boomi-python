
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"document_type": "documentType", "process_id": "processId"})
class ProcessingGroupPartnerDocumentRoute(BaseModel):
    """ProcessingGroupPartnerDocumentRoute

    :param document_type: document_type, defaults to None
    :type document_type: str, optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self, document_type: str = SENTINEL, process_id: str = SENTINEL, **kwargs
    ):
        """ProcessingGroupPartnerDocumentRoute

        :param document_type: document_type, defaults to None
        :type document_type: str, optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        """
        if document_type is not SENTINEL:
            self.document_type = document_type
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
