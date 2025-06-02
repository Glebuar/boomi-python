
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_fields import CustomFields


@JsonMap(
    {
        "accept_ack_report": "acceptAckReport",
        "accept_ack_status": "acceptAckStatus",
        "ack_report": "ackReport",
        "ack_status": "ackStatus",
        "action_type": "actionType",
        "atom_id": "atomId",
        "connector_name": "connectorName",
        "connector_type": "connectorType",
        "custom_fields": "customFields",
        "date_processed": "dateProcessed",
        "document_index": "documentIndex",
        "error_message": "errorMessage",
        "execution_id": "executionId",
        "id_": "id",
        "is_valid_message": "isValidMessage",
        "message_control_id": "messageControlId",
        "message_type": "messageType",
        "operation_name": "operationName",
        "outbound_validation_report": "outboundValidationReport",
        "outbound_validation_status": "outboundValidationStatus",
        "receiver_application_id": "receiverApplicationId",
        "receiver_facility_id": "receiverFacilityId",
        "sender_application_id": "senderApplicationId",
        "sender_facility_id": "senderFacilityId",
    }
)
class Hl7ConnectorRecord(BaseModel):
    """Hl7ConnectorRecord

    :param accept_ack_report: The Accept Acknowledgment Report., defaults to None
    :type accept_ack_report: str, optional
    :param accept_ack_status: The Accept Acknowledgment status — either *Commit Accept*, *Commit Error*, or *Commit Reject*., defaults to None
    :type accept_ack_status: str, optional
    :param account: The ID of the account in which you ran this record.
    :type account: str
    :param ack_report: The acknowledgment report., defaults to None
    :type ack_report: str, optional
    :param ack_status: The acknowledgment status — either *Application Accept*, *Application Error*, or *Application Reject*., defaults to None
    :type ack_status: str, optional
    :param action_type: The type of action with which this record corresponds — *Send* for an outbound interchange or *Listen* for an inbound interchange.
    :type action_type: str
    :param atom_id: The processing ID of the Runtime for this record.
    :type atom_id: str
    :param connector_name: The value is *Trading Partner* for an HL7 trading partner Send operation, or *Start* for an HL7 trading partner Listen operation.
    :type connector_name: str
    :param connector_type: *hl7* is the connector type for any record.
    :type connector_type: str
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: The processing date and time of this record. The format is yyyy-MM-dd'T'HH:mm:ss'Z', for example 2019-09-14T15:32:00Z.
    :type date_processed: str
    :param document_index: The numerical index of this record in the run., defaults to None
    :type document_index: int, optional
    :param error_message: Any error message associated with this record. This field is omitted for a successful interchange.
    :type error_message: str
    :param execution_id: The ID of the run.
    :type execution_id: str
    :param id_: The ID of this record.
    :type id_: str
    :param is_valid_message: If the message satisfies the requirements of the referenced profile’s segment and element configuration, including mandatory fields, data types, and minimum and maximum lengths, the value is true. Otherwise, the value is false., defaults to None
    :type is_valid_message: str, optional
    :param message_control_id: The unique identifier for the message., defaults to None
    :type message_control_id: str, optional
    :param message_type: The code identifying the type of message., defaults to None
    :type message_type: str, optional
    :param operation_name: The name of the operation component processing the record.
    :type operation_name: str
    :param outbound_validation_report: The outbound validation report. This report contains descriptions of errors present in the outbound interchange. If the outbound validation option is not selected in the sending trading partner, the value is N/A. The API omits this field or an inbound interchange., defaults to None
    :type outbound_validation_report: str, optional
    :param outbound_validation_status: The outbound validation status — is either Success, Error-Interchange, Error-Message, or N/A. For an outbound interchange for which you do not select the outbound validation option in the sending trading partner, the value is N/A. This field is omitted for an inbound interchange., defaults to None
    :type outbound_validation_status: str, optional
    :param receiver_application_id: The ID of the receiving application among all other applications within the network enterprise., defaults to None
    :type receiver_application_id: str, optional
    :param receiver_facility_id: Additional detail regarding the receiving application., defaults to None
    :type receiver_facility_id: str, optional
    :param sender_application_id: The ID of the sending application among all other applications within the network enterprise., defaults to None
    :type sender_application_id: str, optional
    :param sender_facility_id: Additional detail regarding the sending application., defaults to None
    :type sender_facility_id: str, optional
    :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
    :type size: int, optional
    :param successful: Whether the record is a success or error., defaults to None
    :type successful: bool, optional
    :param version: The applicable HL7 version., defaults to None
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
        accept_ack_report: str = SENTINEL,
        accept_ack_status: str = SENTINEL,
        ack_report: str = SENTINEL,
        ack_status: str = SENTINEL,
        document_index: int = SENTINEL,
        is_valid_message: str = SENTINEL,
        message_control_id: str = SENTINEL,
        message_type: str = SENTINEL,
        outbound_validation_report: str = SENTINEL,
        outbound_validation_status: str = SENTINEL,
        receiver_application_id: str = SENTINEL,
        receiver_facility_id: str = SENTINEL,
        sender_application_id: str = SENTINEL,
        sender_facility_id: str = SENTINEL,
        size: int = SENTINEL,
        successful: bool = SENTINEL,
        version: str = SENTINEL,
        **kwargs,
    ):
        """Hl7ConnectorRecord

        :param accept_ack_report: The Accept Acknowledgment Report., defaults to None
        :type accept_ack_report: str, optional
        :param accept_ack_status: The Accept Acknowledgment status — either *Commit Accept*, *Commit Error*, or *Commit Reject*., defaults to None
        :type accept_ack_status: str, optional
        :param account: The ID of the account in which you ran this record.
        :type account: str
        :param ack_report: The acknowledgment report., defaults to None
        :type ack_report: str, optional
        :param ack_status: The acknowledgment status — either *Application Accept*, *Application Error*, or *Application Reject*., defaults to None
        :type ack_status: str, optional
        :param action_type: The type of action with which this record corresponds — *Send* for an outbound interchange or *Listen* for an inbound interchange.
        :type action_type: str
        :param atom_id: The processing ID of the Runtime for this record.
        :type atom_id: str
        :param connector_name: The value is *Trading Partner* for an HL7 trading partner Send operation, or *Start* for an HL7 trading partner Listen operation.
        :type connector_name: str
        :param connector_type: *hl7* is the connector type for any record.
        :type connector_type: str
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: The processing date and time of this record. The format is yyyy-MM-dd'T'HH:mm:ss'Z', for example 2019-09-14T15:32:00Z.
        :type date_processed: str
        :param document_index: The numerical index of this record in the run., defaults to None
        :type document_index: int, optional
        :param error_message: Any error message associated with this record. This field is omitted for a successful interchange.
        :type error_message: str
        :param execution_id: The ID of the run.
        :type execution_id: str
        :param id_: The ID of this record.
        :type id_: str
        :param is_valid_message: If the message satisfies the requirements of the referenced profile’s segment and element configuration, including mandatory fields, data types, and minimum and maximum lengths, the value is true. Otherwise, the value is false., defaults to None
        :type is_valid_message: str, optional
        :param message_control_id: The unique identifier for the message., defaults to None
        :type message_control_id: str, optional
        :param message_type: The code identifying the type of message., defaults to None
        :type message_type: str, optional
        :param operation_name: The name of the operation component processing the record.
        :type operation_name: str
        :param outbound_validation_report: The outbound validation report. This report contains descriptions of errors present in the outbound interchange. If the outbound validation option is not selected in the sending trading partner, the value is N/A. The API omits this field or an inbound interchange., defaults to None
        :type outbound_validation_report: str, optional
        :param outbound_validation_status: The outbound validation status — is either Success, Error-Interchange, Error-Message, or N/A. For an outbound interchange for which you do not select the outbound validation option in the sending trading partner, the value is N/A. This field is omitted for an inbound interchange., defaults to None
        :type outbound_validation_status: str, optional
        :param receiver_application_id: The ID of the receiving application among all other applications within the network enterprise., defaults to None
        :type receiver_application_id: str, optional
        :param receiver_facility_id: Additional detail regarding the receiving application., defaults to None
        :type receiver_facility_id: str, optional
        :param sender_application_id: The ID of the sending application among all other applications within the network enterprise., defaults to None
        :type sender_application_id: str, optional
        :param sender_facility_id: Additional detail regarding the sending application., defaults to None
        :type sender_facility_id: str, optional
        :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
        :type size: int, optional
        :param successful: Whether the record is a success or error., defaults to None
        :type successful: bool, optional
        :param version: The applicable HL7 version., defaults to None
        :type version: str, optional
        """
        if accept_ack_report is not SENTINEL:
            self.accept_ack_report = accept_ack_report
        if accept_ack_status is not SENTINEL:
            self.accept_ack_status = accept_ack_status
        self.account = account
        if ack_report is not SENTINEL:
            self.ack_report = ack_report
        if ack_status is not SENTINEL:
            self.ack_status = ack_status
        self.action_type = action_type
        self.atom_id = atom_id
        self.connector_name = connector_name
        self.connector_type = connector_type
        self.custom_fields = self._define_object(custom_fields, CustomFields)
        self.date_processed = date_processed
        if document_index is not SENTINEL:
            self.document_index = document_index
        self.error_message = error_message
        self.execution_id = execution_id
        self.id_ = id_
        if is_valid_message is not SENTINEL:
            self.is_valid_message = is_valid_message
        if message_control_id is not SENTINEL:
            self.message_control_id = message_control_id
        if message_type is not SENTINEL:
            self.message_type = message_type
        self.operation_name = operation_name
        if outbound_validation_report is not SENTINEL:
            self.outbound_validation_report = outbound_validation_report
        if outbound_validation_status is not SENTINEL:
            self.outbound_validation_status = outbound_validation_status
        if receiver_application_id is not SENTINEL:
            self.receiver_application_id = receiver_application_id
        if receiver_facility_id is not SENTINEL:
            self.receiver_facility_id = receiver_facility_id
        if sender_application_id is not SENTINEL:
            self.sender_application_id = sender_application_id
        if sender_facility_id is not SENTINEL:
            self.sender_facility_id = sender_facility_id
        if size is not SENTINEL:
            self.size = size
        if successful is not SENTINEL:
            self.successful = successful
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
