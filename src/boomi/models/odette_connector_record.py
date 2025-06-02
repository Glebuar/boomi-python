
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_fields import CustomFields


@JsonMap(
    {
        "account": "account",
        "ack_report": "ackReport",
        "ack_requested": "ackRequested",
        "ack_status": "ackStatus",
        "action_type": "actionType",
        "atom_id": "atomId",
        "connector_name": "connectorName",
        "connector_type": "connectorType",
        "controlling_agency": "controllingAgency",
        "custom_fields": "customFields",
        "date_processed": "dateProcessed",
        "document_index": "documentIndex",
        "error_message": "errorMessage",
        "execution_id": "executionId",
        "id_": "id",
        "interchange_control_reference": "interchangeControlReference",
        "interchange_date": "interchangeDate",
        "interchange_time": "interchangeTime",
        "message_reference_number": "messageReferenceNumber",
        "message_type": "messageType",
        "operation_name": "operationName",
        "outbound_validation_report": "outboundValidationReport",
        "outbound_validation_status": "outboundValidationStatus",
        "receiver_id": "receiverID",
        "release": "release",
        "sender_id": "senderID",
        "size": "size",
        "successful": "successful",
        "version": "version",
    }
)
class OdetteConnectorRecord(BaseModel):
    """OdetteConnectorRecord

    :param account: account
    :type account: str
    :param ack_report: ack_report, defaults to None
    :type ack_report: str, optional
    :param ack_requested: ack_requested, defaults to None
    :type ack_requested: str, optional
    :param ack_status: ack_status, defaults to None
    :type ack_status: str, optional
    :param action_type: action_type
    :type action_type: str
    :param atom_id: atom_id
    :type atom_id: str
    :param connector_name: connector_name
    :type connector_name: str
    :param connector_type: connector_type
    :type connector_type: str
    :param controlling_agency: controlling_agency, defaults to None
    :type controlling_agency: str, optional
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: date_processed
    :type date_processed: str
    :param document_index: document_index, defaults to None
    :type document_index: int, optional
    :param error_message: error_message
    :type error_message: str
    :param execution_id: execution_id
    :type execution_id: str
    :param id_: id_
    :type id_: str
    :param interchange_control_reference: interchange_control_reference, defaults to None
    :type interchange_control_reference: str, optional
    :param interchange_date: interchange_date, defaults to None
    :type interchange_date: str, optional
    :param interchange_time: interchange_time, defaults to None
    :type interchange_time: str, optional
    :param message_reference_number: message_reference_number, defaults to None
    :type message_reference_number: str, optional
    :param message_type: message_type, defaults to None
    :type message_type: str, optional
    :param operation_name: operation_name
    :type operation_name: str
    :param outbound_validation_report: outbound_validation_report, defaults to None
    :type outbound_validation_report: str, optional
    :param outbound_validation_status: outbound_validation_status, defaults to None
    :type outbound_validation_status: str, optional
    :param receiver_id: receiver_id, defaults to None
    :type receiver_id: str, optional
    :param release: release, defaults to None
    :type release: str, optional
    :param sender_id: sender_id, defaults to None
    :type sender_id: str, optional
    :param size: size, defaults to None
    :type size: int, optional
    :param successful: successful, defaults to None
    :type successful: bool, optional
    :param version: version, defaults to None
    :type version: str, optional
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
        ack_report: str = SENTINEL,
        ack_requested: str = SENTINEL,
        ack_status: str = SENTINEL,
        controlling_agency: str = SENTINEL,
        document_index: int = SENTINEL,
        interchange_control_reference: str = SENTINEL,
        interchange_date: str = SENTINEL,
        interchange_time: str = SENTINEL,
        message_reference_number: str = SENTINEL,
        message_type: str = SENTINEL,
        outbound_validation_report: str = SENTINEL,
        outbound_validation_status: str = SENTINEL,
        receiver_id: str = SENTINEL,
        release: str = SENTINEL,
        sender_id: str = SENTINEL,
        size: int = SENTINEL,
        successful: bool = SENTINEL,
        version: str = SENTINEL,
        **kwargs,
    ):
        """OdetteConnectorRecord

        :param account: account
        :type account: str
        :param ack_report: ack_report, defaults to None
        :type ack_report: str, optional
        :param ack_requested: ack_requested, defaults to None
        :type ack_requested: str, optional
        :param ack_status: ack_status, defaults to None
        :type ack_status: str, optional
        :param action_type: action_type
        :type action_type: str
        :param atom_id: atom_id
        :type atom_id: str
        :param connector_name: connector_name
        :type connector_name: str
        :param connector_type: connector_type
        :type connector_type: str
        :param controlling_agency: controlling_agency, defaults to None
        :type controlling_agency: str, optional
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: date_processed
        :type date_processed: str
        :param document_index: document_index, defaults to None
        :type document_index: int, optional
        :param error_message: error_message
        :type error_message: str
        :param execution_id: execution_id
        :type execution_id: str
        :param id_: id_
        :type id_: str
        :param interchange_control_reference: interchange_control_reference, defaults to None
        :type interchange_control_reference: str, optional
        :param interchange_date: interchange_date, defaults to None
        :type interchange_date: str, optional
        :param interchange_time: interchange_time, defaults to None
        :type interchange_time: str, optional
        :param message_reference_number: message_reference_number, defaults to None
        :type message_reference_number: str, optional
        :param message_type: message_type, defaults to None
        :type message_type: str, optional
        :param operation_name: operation_name
        :type operation_name: str
        :param outbound_validation_report: outbound_validation_report, defaults to None
        :type outbound_validation_report: str, optional
        :param outbound_validation_status: outbound_validation_status, defaults to None
        :type outbound_validation_status: str, optional
        :param receiver_id: receiver_id, defaults to None
        :type receiver_id: str, optional
        :param release: release, defaults to None
        :type release: str, optional
        :param sender_id: sender_id, defaults to None
        :type sender_id: str, optional
        :param size: size, defaults to None
        :type size: int, optional
        :param successful: successful, defaults to None
        :type successful: bool, optional
        :param version: version, defaults to None
        :type version: str, optional
        """
        self.account = account
        if ack_report is not SENTINEL:
            self.ack_report = ack_report
        if ack_requested is not SENTINEL:
            self.ack_requested = ack_requested
        if ack_status is not SENTINEL:
            self.ack_status = ack_status
        self.action_type = action_type
        self.atom_id = atom_id
        self.connector_name = connector_name
        self.connector_type = connector_type
        if controlling_agency is not SENTINEL:
            self.controlling_agency = controlling_agency
        self.custom_fields = self._define_object(custom_fields, CustomFields)
        self.date_processed = date_processed
        if document_index is not SENTINEL:
            self.document_index = document_index
        self.error_message = error_message
        self.execution_id = execution_id
        self.id_ = id_
        if interchange_control_reference is not SENTINEL:
            self.interchange_control_reference = interchange_control_reference
        if interchange_date is not SENTINEL:
            self.interchange_date = interchange_date
        if interchange_time is not SENTINEL:
            self.interchange_time = interchange_time
        if message_reference_number is not SENTINEL:
            self.message_reference_number = message_reference_number
        if message_type is not SENTINEL:
            self.message_type = message_type
        self.operation_name = operation_name
        if outbound_validation_report is not SENTINEL:
            self.outbound_validation_report = outbound_validation_report
        if outbound_validation_status is not SENTINEL:
            self.outbound_validation_status = outbound_validation_status
        if receiver_id is not SENTINEL:
            self.receiver_id = receiver_id
        if release is not SENTINEL:
            self.release = release
        if sender_id is not SENTINEL:
            self.sender_id = sender_id
        if size is not SENTINEL:
            self.size = size
        if successful is not SENTINEL:
            self.successful = successful
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
