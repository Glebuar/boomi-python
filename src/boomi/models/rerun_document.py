
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .all_documents import AllDocuments
from .selected_documents import SelectedDocuments


@JsonMap(
    {
        "all_documents": "AllDocuments",
        "selected_documents": "SelectedDocuments",
        "original_execution_id": "originalExecutionId",
        "record_url": "recordUrl",
        "request_id": "requestId",
    }
)
class RerunDocument(BaseModel):
    """RerunDocument

    :param all_documents: You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both.  Indicates that the Rerun Document operation reruns all documents in the original run. When using AllDocuments in a request, you must also specify a `documentStatus` value.
    :type all_documents: AllDocuments
    :param selected_documents: You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both. Indicates that the Rerun Document operation reruns only those documents you specify in the `genericConnectorRecordId` value.
    :type selected_documents: SelectedDocuments
    :param original_execution_id: The ID of the original process run. You can obtain the `originalExecutionId` from the user interface from the Process Reporting page, selecting the Actions menu for a specific process run, and selecting View Extended Information from the list of options.
    :type original_execution_id: str
    :param record_url: (Response-only field) The ID of the process run. The initial CREATE response returns this field and uses it in the subsequent call to find the corresponding run record., defaults to None
    :type record_url: str, optional
    :param request_id: (Response-only field) The full endpoint URL used to make a second call to the Execution Record object. This URL is provided for your convenience in recordUrl field of the initial CREATE response., defaults to None
    :type request_id: str, optional
    """

    def __init__(
        self,
        all_documents: AllDocuments,
        selected_documents: SelectedDocuments,
        original_execution_id: str,
        record_url: str = SENTINEL,
        request_id: str = SENTINEL,
        **kwargs,
    ):
        """RerunDocument

        :param all_documents: You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both.  Indicates that the Rerun Document operation reruns all documents in the original run. When using AllDocuments in a request, you must also specify a `documentStatus` value.
        :type all_documents: AllDocuments
        :param selected_documents: You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both. Indicates that the Rerun Document operation reruns only those documents you specify in the `genericConnectorRecordId` value.
        :type selected_documents: SelectedDocuments
        :param original_execution_id: The ID of the original process run. You can obtain the `originalExecutionId` from the user interface from the Process Reporting page, selecting the Actions menu for a specific process run, and selecting View Extended Information from the list of options.
        :type original_execution_id: str
        :param record_url: (Response-only field) The ID of the process run. The initial CREATE response returns this field and uses it in the subsequent call to find the corresponding run record., defaults to None
        :type record_url: str, optional
        :param request_id: (Response-only field) The full endpoint URL used to make a second call to the Execution Record object. This URL is provided for your convenience in recordUrl field of the initial CREATE response., defaults to None
        :type request_id: str, optional
        """
        self.all_documents = self._define_object(all_documents, AllDocuments)
        self.selected_documents = self._define_object(
            selected_documents, SelectedDocuments
        )
        self.original_execution_id = original_execution_id
        if record_url is not SENTINEL:
            self.record_url = record_url
        if request_id is not SENTINEL:
            self.request_id = request_id
        self._kwargs = kwargs
