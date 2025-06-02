
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class DocumentStatus(Enum):
    """An enumeration representing different categories.

    :cvar ANY: "ANY"
    :vartype ANY: str
    :cvar SUCCESS: "SUCCESS"
    :vartype SUCCESS: str
    :cvar ERROR: "ERROR"
    :vartype ERROR: str
    """

    ANY = "ANY"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DocumentStatus._member_map_.values()))


@JsonMap({"document_status": "documentStatus"})
class AllDocuments(BaseModel):
    """You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both.

     Indicates that the Rerun Document operation reruns all documents in the original run.

    When using AllDocuments in a request, you must also specify a `documentStatus` value.

    :param document_status: - A value of ANY reruns all documents in the specified process run (in other words, the originalExecutionID).  - A value of SUCCESS returns successfully run documents in the process run.  - A value of ERROR returns documents that unsuccessfully ran in the process run., defaults to None
    :type document_status: DocumentStatus, optional
    """

    def __init__(self, document_status: DocumentStatus = SENTINEL, **kwargs):
        """You must include either the `AllDocuments` field or the `SelectedDocuments` field in a request, but not both.

         Indicates that the Rerun Document operation reruns all documents in the original run.

        When using AllDocuments in a request, you must also specify a `documentStatus` value.

        :param document_status: - A value of ANY reruns all documents in the specified process run (in other words, the originalExecutionID).  - A value of SUCCESS returns successfully run documents in the process run.  - A value of ERROR returns documents that unsuccessfully ran in the process run., defaults to None
        :type document_status: DocumentStatus, optional
        """
        if document_status is not SENTINEL:
            self.document_status = self._enum_matching(
                document_status, DocumentStatus.list(), "document_status"
            )
        self._kwargs = kwargs
