
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_fields import CustomFields


@JsonMap(
    {
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
        "sender_id": "senderID",
    }
)
class EdifactConnectorRecord(BaseModel):
    """EdifactConnectorRecord

    :param account: The ID of the account from which you ran this record.
    :type account: str
    :param ack_report: The acknowledgment report., defaults to None
    :type ack_report: str, optional
    :param ack_requested: The UNB09, the Acknowledgement Request field value, determines whether the sending trading partner requests a CONTRL message as functional acknowledgment. A value of 1 indicates there is an acknowledgment request. An empty value means there is no acknowledgment request., defaults to None
    :type ack_requested: str, optional
    :param ack_status: The acknowledgment status — either Accepted, Received, or Rejected., defaults to None
    :type ack_status: str, optional
    :param action_type: The type of action with which this record corresponds — Send for an outbound interchange, Get for an inbound interchange using the Disk, FTP, or SFTP communication method, or Listen for an inbound interchange using the AS2 or HTTP communication method.
    :type action_type: str
    :param atom_id: The ID of the Atom that processed this record.
    :type atom_id: str
    :param connector_name: The value is Trading Partner for an EDIFACT trading partner Send operation, or Start for an EDIFACT trading partner Listen operation.
    :type connector_name: str
    :param connector_type: edifact is the connector type for any record.
    :type connector_type: str
    :param controlling_agency: The controlling agency for the message type., defaults to None
    :type controlling_agency: str, optional
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: The processing date and time of this record. The format is yyyy-MM-dd'T'HH:mm:ss'Z', for example, 2018-08-08T15:32:00Z.
    :type date_processed: str
    :param document_index: The numerical index of this record in the run., defaults to None
    :type document_index: int, optional
    :param error_message: Any error message associated with this record.
    :type error_message: str
    :param execution_id: The ID of the run.
    :type execution_id: str
    :param id_: The ID of this record.
    :type id_: str
    :param interchange_control_reference: The number that uniquely identifies the interchange., defaults to None
    :type interchange_control_reference: str, optional
    :param interchange_date: The date of preparation. The format is *yyMMdd*., defaults to None
    :type interchange_date: str, optional
    :param interchange_time: The time of preparation. The format is *HHmm*., defaults to None
    :type interchange_time: str, optional
    :param message_reference_number: The unique message reference assigned by the sender., defaults to None
    :type message_reference_number: str, optional
    :param message_type: The code identifying the type of message., defaults to None
    :type message_type: str, optional
    :param operation_name: The name of the operation component that processed the record.
    :type operation_name: str
    :param outbound_validation_report: The outbound validation report. This report contains descriptions of errors present in the outbound interchange. If the outbound validation option is not selected in the sending trading partner, the value is N/A. An inbound interchange omits this field., defaults to None
    :type outbound_validation_report: str, optional
    :param outbound_validation_status: The outbound validation status — either Success, Error - Interchange, Error - Message, or N/A. For an outbound interchange for which the outbound validation option is not selected in the sending trading partner, the value is *N/A*. An inbound interchange omits this field., defaults to None
    :type outbound_validation_status: str, optional
    :param receiver_id: For an inbound interchange, the UNB03, Interchange Receiver ID, field value, which identifies the receiver., defaults to None
    :type receiver_id: str, optional
    :param release: The message type release number., defaults to None
    :type release: str, optional
    :param sender_id: For an outbound interchange, the UNB02, Interchange Sender ID, field value, which identifies the sender., defaults to None
    :type sender_id: str, optional
    :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
    :type size: int, optional
    :param successful: Whether the record is a success or an error., defaults to None
    :type successful: bool, optional
    :param version: The message type version number., defaults to None
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
        """EdifactConnectorRecord

        :param account: The ID of the account from which you ran this record.
        :type account: str
        :param ack_report: The acknowledgment report., defaults to None
        :type ack_report: str, optional
        :param ack_requested: The UNB09, the Acknowledgement Request field value, determines whether the sending trading partner requests a CONTRL message as functional acknowledgment. A value of 1 indicates there is an acknowledgment request. An empty value means there is no acknowledgment request., defaults to None
        :type ack_requested: str, optional
        :param ack_status: The acknowledgment status — either Accepted, Received, or Rejected., defaults to None
        :type ack_status: str, optional
        :param action_type: The type of action with which this record corresponds — Send for an outbound interchange, Get for an inbound interchange using the Disk, FTP, or SFTP communication method, or Listen for an inbound interchange using the AS2 or HTTP communication method.
        :type action_type: str
        :param atom_id: The ID of the Atom that processed this record.
        :type atom_id: str
        :param connector_name: The value is Trading Partner for an EDIFACT trading partner Send operation, or Start for an EDIFACT trading partner Listen operation.
        :type connector_name: str
        :param connector_type: edifact is the connector type for any record.
        :type connector_type: str
        :param controlling_agency: The controlling agency for the message type., defaults to None
        :type controlling_agency: str, optional
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: The processing date and time of this record. The format is yyyy-MM-dd'T'HH:mm:ss'Z', for example, 2018-08-08T15:32:00Z.
        :type date_processed: str
        :param document_index: The numerical index of this record in the run., defaults to None
        :type document_index: int, optional
        :param error_message: Any error message associated with this record.
        :type error_message: str
        :param execution_id: The ID of the run.
        :type execution_id: str
        :param id_: The ID of this record.
        :type id_: str
        :param interchange_control_reference: The number that uniquely identifies the interchange., defaults to None
        :type interchange_control_reference: str, optional
        :param interchange_date: The date of preparation. The format is *yyMMdd*., defaults to None
        :type interchange_date: str, optional
        :param interchange_time: The time of preparation. The format is *HHmm*., defaults to None
        :type interchange_time: str, optional
        :param message_reference_number: The unique message reference assigned by the sender., defaults to None
        :type message_reference_number: str, optional
        :param message_type: The code identifying the type of message., defaults to None
        :type message_type: str, optional
        :param operation_name: The name of the operation component that processed the record.
        :type operation_name: str
        :param outbound_validation_report: The outbound validation report. This report contains descriptions of errors present in the outbound interchange. If the outbound validation option is not selected in the sending trading partner, the value is N/A. An inbound interchange omits this field., defaults to None
        :type outbound_validation_report: str, optional
        :param outbound_validation_status: The outbound validation status — either Success, Error - Interchange, Error - Message, or N/A. For an outbound interchange for which the outbound validation option is not selected in the sending trading partner, the value is *N/A*. An inbound interchange omits this field., defaults to None
        :type outbound_validation_status: str, optional
        :param receiver_id: For an inbound interchange, the UNB03, Interchange Receiver ID, field value, which identifies the receiver., defaults to None
        :type receiver_id: str, optional
        :param release: The message type release number., defaults to None
        :type release: str, optional
        :param sender_id: For an outbound interchange, the UNB02, Interchange Sender ID, field value, which identifies the sender., defaults to None
        :type sender_id: str, optional
        :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
        :type size: int, optional
        :param successful: Whether the record is a success or an error., defaults to None
        :type successful: bool, optional
        :param version: The message type version number., defaults to None
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
