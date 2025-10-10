
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_fields import CustomFields


@JsonMap(
    {
        "ack_status": "ackStatus",
        "action_type": "actionType",
        "as2_from_id": "as2FromId",
        "as2_to_id": "as2ToId",
        "atom_id": "atomId",
        "connector_name": "connectorName",
        "connector_type": "connectorType",
        "content_length": "contentLength",
        "custom_fields": "customFields",
        "date_processed": "dateProcessed",
        "document_index": "documentIndex",
        "error_message": "errorMessage",
        "execution_id": "executionId",
        "id_": "id",
        "mdn_message": "mdnMessage",
        "message_id": "messageId",
        "operation_name": "operationName",
    }
)
class As2ConnectorRecord(BaseModel):
    """As2ConnectorRecord

    :param account: The ID of the account this record was run in.
    :type account: str
    :param ack_status: The acknowledgment status — Acknowledged, Acknowledged/Errors, or Not Acknowledged., defaults to None
    :type ack_status: str, optional
    :param action_type: The type of action with which this record corresponds — Listen or Send.
    :type action_type: str
    :param as2_from_id: The arbitrary identifier that indicates the sender of the message., defaults to None
    :type as2_from_id: str, optional
    :param as2_to_id: The arbitrary identifier that indicates the recipient of the message., defaults to None
    :type as2_to_id: str, optional
    :param atom_id: The ID of the Runtime that processed this record.
    :type atom_id: str
    :param connector_name: For an AS2 Client \(Send\) operation, the value is the name of the AS2 Client connection component through which the document that corresponds to this record was sent. The value is as2sharedserver Connector for an AS2 Shared Server \(Listen\) operation, Trading Partner for an X12 trading partner Send operation, or Start for an X12 trading partner Listen operation.
    :type connector_name: str
    :param connector_type: The type of connector to which this record corresponds — as2 for AS2 Client \(Send\), as2sharedserver for AS2 Shared Server \(Listen\), or x12 for Trading Partner Send or Listen using the X12 standard.
    :type connector_type: str
    :param content_length: The length of the message in bytes., defaults to None
    :type content_length: str, optional
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: The processing date and time of this record.
    :type date_processed: str
    :param document_index: The numerical index of this record in the run., defaults to None
    :type document_index: int, optional
    :param error_message: The error message associated with this record if applicable.
    :type error_message: str
    :param execution_id: The ID of the run.
    :type execution_id: str
    :param filename: The file name of the document that corresponds to this record., defaults to None
    :type filename: str, optional
    :param id_: The ID of this record.
    :type id_: str
    :param mdn_message: The content of the Message Delivery Notification \(MDN\) message — *processed*, *processed/error*, *processed/error:* *authentication-failed*, *processed/error: decompression-failed*, or *processed/error: decryption-failed*. In a Listen action by the AS2 shared server, an MDN message generates automatically. For a Send action, generating an MDN message is an option for the processing AS2 Client operation., defaults to None
    :type mdn_message: str, optional
    :param message_id: The arbitrary identifier for the message., defaults to None
    :type message_id: str, optional
    :param mimetype: The MIME type of the message — *text/plain*, *application/binary*, *application/edifact*, *application/octet-stream*, *application/edi-x12*, or *application/xml*, defaults to None
    :type mimetype: str, optional
    :param operation_name: The name of the operation component that processed this record. The component is an AS2 Client operation in the case of a Send action or an AS2 Shared Server operation in the case of a Listen action.
    :type operation_name: str
    :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
    :type size: int, optional
    :param subject: The arbitrary subject name for the message., defaults to None
    :type subject: str, optional
    :param successful: Whether the record is a success or error., defaults to None
    :type successful: bool, optional
    """

    def __init__(
        self,
        account: str,
        action_type: str,
        atom_id: str,
        connector_name: str,
        connector_type: str,
        custom_fields: CustomFields,
        date_processed: str,
        error_message: str,
        execution_id: str,
        id_: str,
        operation_name: str,
        ack_status: str = SENTINEL,
        as2_from_id: str = SENTINEL,
        as2_to_id: str = SENTINEL,
        content_length: str = SENTINEL,
        document_index: int = SENTINEL,
        filename: str = SENTINEL,
        mdn_message: str = SENTINEL,
        message_id: str = SENTINEL,
        mimetype: str = SENTINEL,
        size: int = SENTINEL,
        subject: str = SENTINEL,
        successful: bool = SENTINEL,
        **kwargs,
    ):
        """As2ConnectorRecord

        :param account: The ID of the account this record was run in.
        :type account: str
        :param ack_status: The acknowledgment status — Acknowledged, Acknowledged/Errors, or Not Acknowledged., defaults to None
        :type ack_status: str, optional
        :param action_type: The type of action with which this record corresponds — Listen or Send.
        :type action_type: str
        :param as2_from_id: The arbitrary identifier that indicates the sender of the message., defaults to None
        :type as2_from_id: str, optional
        :param as2_to_id: The arbitrary identifier that indicates the recipient of the message., defaults to None
        :type as2_to_id: str, optional
        :param atom_id: The ID of the Runtime that processed this record.
        :type atom_id: str
        :param connector_name: For an AS2 Client \(Send\) operation, the value is the name of the AS2 Client connection component through which the document that corresponds to this record was sent. The value is as2sharedserver Connector for an AS2 Shared Server \(Listen\) operation, Trading Partner for an X12 trading partner Send operation, or Start for an X12 trading partner Listen operation.
        :type connector_name: str
        :param connector_type: The type of connector to which this record corresponds — as2 for AS2 Client \(Send\), as2sharedserver for AS2 Shared Server \(Listen\), or x12 for Trading Partner Send or Listen using the X12 standard.
        :type connector_type: str
        :param content_length: The length of the message in bytes., defaults to None
        :type content_length: str, optional
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: The processing date and time of this record.
        :type date_processed: str
        :param document_index: The numerical index of this record in the run., defaults to None
        :type document_index: int, optional
        :param error_message: The error message associated with this record if applicable.
        :type error_message: str
        :param execution_id: The ID of the run.
        :type execution_id: str
        :param filename: The file name of the document that corresponds to this record., defaults to None
        :type filename: str, optional
        :param id_: The ID of this record.
        :type id_: str
        :param mdn_message: The content of the Message Delivery Notification \(MDN\) message — *processed*, *processed/error*, *processed/error:* *authentication-failed*, *processed/error: decompression-failed*, or *processed/error: decryption-failed*. In a Listen action by the AS2 shared server, an MDN message generates automatically. For a Send action, generating an MDN message is an option for the processing AS2 Client operation., defaults to None
        :type mdn_message: str, optional
        :param message_id: The arbitrary identifier for the message., defaults to None
        :type message_id: str, optional
        :param mimetype: The MIME type of the message — *text/plain*, *application/binary*, *application/edifact*, *application/octet-stream*, *application/edi-x12*, or *application/xml*, defaults to None
        :type mimetype: str, optional
        :param operation_name: The name of the operation component that processed this record. The component is an AS2 Client operation in the case of a Send action or an AS2 Shared Server operation in the case of a Listen action.
        :type operation_name: str
        :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
        :type size: int, optional
        :param subject: The arbitrary subject name for the message., defaults to None
        :type subject: str, optional
        :param successful: Whether the record is a success or error., defaults to None
        :type successful: bool, optional
        """
        self.account = account
        if ack_status is not SENTINEL:
            self.ack_status = ack_status
        self.action_type = action_type
        if as2_from_id is not SENTINEL:
            self.as2_from_id = as2_from_id
        if as2_to_id is not SENTINEL:
            self.as2_to_id = as2_to_id
        self.atom_id = atom_id
        self.connector_name = connector_name
        self.connector_type = connector_type
        if content_length is not SENTINEL:
            self.content_length = content_length
        self.custom_fields = self._define_object(custom_fields, CustomFields)
        self.date_processed = date_processed
        if document_index is not SENTINEL:
            self.document_index = document_index
        self.error_message = error_message
        self.execution_id = execution_id
        if filename is not SENTINEL:
            self.filename = filename
        self.id_ = id_
        if mdn_message is not SENTINEL:
            self.mdn_message = mdn_message
        if message_id is not SENTINEL:
            self.message_id = message_id
        if mimetype is not SENTINEL:
            self.mimetype = mimetype
        self.operation_name = operation_name
        if size is not SENTINEL:
            self.size = size
        if subject is not SENTINEL:
            self.subject = subject
        if successful is not SENTINEL:
            self.successful = successful
        self._kwargs = kwargs
