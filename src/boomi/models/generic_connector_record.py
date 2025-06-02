
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .connector_fields import ConnectorFields
from .tracked_fields import TrackedFields


class GenericConnectorRecordStatus(Enum):
    """An enumeration representing different categories.

    :cvar SUCCESS: "SUCCESS"
    :vartype SUCCESS: str
    :cvar ERROR: "ERROR"
    :vartype ERROR: str
    """

    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GenericConnectorRecordStatus._member_map_.values())
        )


@JsonMap(
    {
        "action_type": "actionType",
        "atom_id": "atomId",
        "connection_id": "connectionId",
        "connection_name": "connectionName",
        "connector_fields": "connectorFields",
        "connector_type": "connectorType",
        "date_processed": "dateProcessed",
        "document_index": "documentIndex",
        "error_message": "errorMessage",
        "execution_connector_id": "executionConnectorId",
        "execution_id": "executionId",
        "id_": "id",
        "incremental_document_index": "incrementalDocumentIndex",
        "operation_id": "operationId",
        "operation_name": "operationName",
        "start_shape": "startShape",
        "tracked_fields": "trackedFields",
    }
)
class GenericConnectorRecord(BaseModel):
    """GenericConnectorRecord

    :param account: account, defaults to None
    :type account: str, optional
    :param action_type: The type of action the connector performs, for example, GET, SEND, LISTEN, and so on., defaults to None
    :type action_type: str, optional
    :param atom_id: The ID of the Runtime in which the process ran. In the case of a Runtime cloud, use the ID of the Cloud attachment and not that of the Cloud itself., defaults to None
    :type atom_id: str, optional
    :param connection_id: When sending documents into or out of the Connection component, use this ID., defaults to None
    :type connection_id: str, optional
    :param connection_name: When sending documents into or out of the Connection component, use this user-defined name., defaults to None
    :type connection_name: str, optional
    :param connector_fields: Displays all connector-related fields from the connector included in this document.
    :type connector_fields: ConnectorFields
    :param connector_type: The internal and unique identifier for the connector type the document was sent into or out of, such as `http`, `ftp`, or `greatplains`., defaults to None
    :type connector_type: str, optional
    :param date_processed: The processing date and time of the document., defaults to None
    :type date_processed: str, optional
    :param document_index: Index of the document within the context of its execution connector \(starting from 0\)., defaults to None
    :type document_index: int, optional
    :param error_message: Displays the corresponding error message for an unsuccessful document.
    :type error_message: str
    :param execution_connector_id: The ID of the [Execution Connector object](/api/platformapi#tag/ExecutionConnector). This ID identifies the execution connector of which this document is a part., defaults to None
    :type execution_connector_id: str, optional
    :param execution_id: The ID of the process run., defaults to None
    :type execution_id: str, optional
    :param id_: The ID of the GenericConnectorRecord. You obtain this ID from querying the GenericConnectorRecord object, defaults to None
    :type id_: str, optional
    :param incremental_document_index: Index of the document in the context of the overall run \(starting from 1\)., defaults to None
    :type incremental_document_index: int, optional
    :param operation_id: When sending documents into or out of the Operation component, use this ID., defaults to None
    :type operation_id: str, optional
    :param operation_name: When sending documents into or out of the Operation component, use this user-defined name., defaults to None
    :type operation_name: str, optional
    :param retryable: If the value is true, this indicates that you can rerun the document using the Rerun Document operation. If the value is false, this indicates that you cannot rerun the document using the Rerun Document operation., defaults to None
    :type retryable: bool, optional
    :param size: The size of the document in kilobytes., defaults to None
    :type size: int, optional
    :param start_shape: If the value is true, this indicates the configuration of the Connector or Trading Partner as a **Start** shape in the process run. If the value is false, this indicates that you did not configure the Connector or Trading Partner as a **Start** shape in the process run., defaults to None
    :type start_shape: bool, optional
    :param status: Indicates whether the document successfully or unsuccessfully ran., defaults to None
    :type status: GenericConnectorRecordStatus, optional
    :param tracked_fields: Displays all the custom tracked fields from this document.
    :type tracked_fields: TrackedFields
    """

    def __init__(
        self,
        connector_fields: ConnectorFields,
        error_message: str,
        tracked_fields: TrackedFields,
        account: str = SENTINEL,
        action_type: str = SENTINEL,
        atom_id: str = SENTINEL,
        connection_id: str = SENTINEL,
        connection_name: str = SENTINEL,
        connector_type: str = SENTINEL,
        date_processed: str = SENTINEL,
        document_index: int = SENTINEL,
        execution_connector_id: str = SENTINEL,
        execution_id: str = SENTINEL,
        id_: str = SENTINEL,
        incremental_document_index: int = SENTINEL,
        operation_id: str = SENTINEL,
        operation_name: str = SENTINEL,
        retryable: bool = SENTINEL,
        size: int = SENTINEL,
        start_shape: bool = SENTINEL,
        status: GenericConnectorRecordStatus = SENTINEL,
        **kwargs,
    ):
        """GenericConnectorRecord

        :param account: account, defaults to None
        :type account: str, optional
        :param action_type: The type of action the connector performs, for example, GET, SEND, LISTEN, and so on., defaults to None
        :type action_type: str, optional
        :param atom_id: The ID of the Runtime in which the process ran. In the case of a Runtime cloud, use the ID of the Cloud attachment and not that of the Cloud itself., defaults to None
        :type atom_id: str, optional
        :param connection_id: When sending documents into or out of the Connection component, use this ID., defaults to None
        :type connection_id: str, optional
        :param connection_name: When sending documents into or out of the Connection component, use this user-defined name., defaults to None
        :type connection_name: str, optional
        :param connector_fields: Displays all connector-related fields from the connector included in this document.
        :type connector_fields: ConnectorFields
        :param connector_type: The internal and unique identifier for the connector type the document was sent into or out of, such as `http`, `ftp`, or `greatplains`., defaults to None
        :type connector_type: str, optional
        :param date_processed: The processing date and time of the document., defaults to None
        :type date_processed: str, optional
        :param document_index: Index of the document within the context of its execution connector \(starting from 0\)., defaults to None
        :type document_index: int, optional
        :param error_message: Displays the corresponding error message for an unsuccessful document.
        :type error_message: str
        :param execution_connector_id: The ID of the [Execution Connector object](/api/platformapi#tag/ExecutionConnector). This ID identifies the execution connector of which this document is a part., defaults to None
        :type execution_connector_id: str, optional
        :param execution_id: The ID of the process run., defaults to None
        :type execution_id: str, optional
        :param id_: The ID of the GenericConnectorRecord. You obtain this ID from querying the GenericConnectorRecord object, defaults to None
        :type id_: str, optional
        :param incremental_document_index: Index of the document in the context of the overall run \(starting from 1\)., defaults to None
        :type incremental_document_index: int, optional
        :param operation_id: When sending documents into or out of the Operation component, use this ID., defaults to None
        :type operation_id: str, optional
        :param operation_name: When sending documents into or out of the Operation component, use this user-defined name., defaults to None
        :type operation_name: str, optional
        :param retryable: If the value is true, this indicates that you can rerun the document using the Rerun Document operation. If the value is false, this indicates that you cannot rerun the document using the Rerun Document operation., defaults to None
        :type retryable: bool, optional
        :param size: The size of the document in kilobytes., defaults to None
        :type size: int, optional
        :param start_shape: If the value is true, this indicates the configuration of the Connector or Trading Partner as a **Start** shape in the process run. If the value is false, this indicates that you did not configure the Connector or Trading Partner as a **Start** shape in the process run., defaults to None
        :type start_shape: bool, optional
        :param status: Indicates whether the document successfully or unsuccessfully ran., defaults to None
        :type status: GenericConnectorRecordStatus, optional
        :param tracked_fields: Displays all the custom tracked fields from this document.
        :type tracked_fields: TrackedFields
        """
        if account is not SENTINEL:
            self.account = account
        if action_type is not SENTINEL:
            self.action_type = action_type
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if connection_id is not SENTINEL:
            self.connection_id = connection_id
        if connection_name is not SENTINEL:
            self.connection_name = connection_name
        self.connector_fields = self._define_object(connector_fields, ConnectorFields)
        if connector_type is not SENTINEL:
            self.connector_type = connector_type
        if date_processed is not SENTINEL:
            self.date_processed = date_processed
        if document_index is not SENTINEL:
            self.document_index = document_index
        self.error_message = error_message
        if execution_connector_id is not SENTINEL:
            self.execution_connector_id = execution_connector_id
        if execution_id is not SENTINEL:
            self.execution_id = execution_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if incremental_document_index is not SENTINEL:
            self.incremental_document_index = incremental_document_index
        if operation_id is not SENTINEL:
            self.operation_id = operation_id
        if operation_name is not SENTINEL:
            self.operation_name = operation_name
        if retryable is not SENTINEL:
            self.retryable = retryable
        if size is not SENTINEL:
            self.size = size
        if start_shape is not SENTINEL:
            self.start_shape = start_shape
        if status is not SENTINEL:
            self.status = self._enum_matching(
                status, GenericConnectorRecordStatus.list(), "status"
            )
        self.tracked_fields = self._define_object(tracked_fields, TrackedFields)
        self._kwargs = kwargs
