
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_fields import CustomFields


@JsonMap(
    {
        "ack_report": "ackReport",
        "ack_status": "ackStatus",
        "action_type": "actionType",
        "agency_code": "agencyCode",
        "app_receiver_id": "appReceiverID",
        "app_sender_id": "appSenderID",
        "atom_id": "atomId",
        "connector_name": "connectorName",
        "connector_type": "connectorType",
        "custom_fields": "customFields",
        "date_processed": "dateProcessed",
        "document_index": "documentIndex",
        "error_message": "errorMessage",
        "execution_id": "executionId",
        "functional_id": "functionalID",
        "gs_control": "gsControl",
        "gs_date": "gsDate",
        "gs_time": "gsTime",
        "gs_version": "gsVersion",
        "id_": "id",
        "isa_ack_report": "isaAckReport",
        "isa_ack_status": "isaAckStatus",
        "isa_control": "isaControl",
        "operation_name": "operationName",
        "outbound_validation_report": "outboundValidationReport",
        "outbound_validation_status": "outboundValidationStatus",
        "receiver_id": "receiverID",
        "receiver_id_qualifier": "receiverIDQualifier",
        "sender_id": "senderID",
        "sender_id_qualifier": "senderIDQualifier",
        "st_control": "stControl",
        "standard_id": "standardID",
        "test_indicator": "testIndicator",
        "transaction_set": "transactionSet",
    }
)
class X12ConnectorRecord(BaseModel):
    """X12ConnectorRecord

    :param account: The ID of the account in which this record ran.
    :type account: str
    :param ack_report: The acknowledgment report., defaults to None
    :type ack_report: str, optional
    :param ack_status: The acknowledgment status — either Accepted, Accepted with Errors, Partially Accepted, or Rejected., defaults to None
    :type ack_status: str, optional
    :param action_type: The type of action with which this record corresponds — Send for an outbound interchange, Get for an inbound interchange using the Disk, FTP, or SFTP communication method, or Listen for an inbound interchange using the AS2 or HTTP communication method.
    :type action_type: str
    :param agency_code: The Responsible Agency Code., defaults to None
    :type agency_code: str, optional
    :param app_receiver_id: For inbound interchanges, the Application Receiver’s Code, which identifies the receiver., defaults to None
    :type app_receiver_id: str, optional
    :param app_sender_id: For outbound interchanges, the Application Sender’s Code, which identifies the sender., defaults to None
    :type app_sender_id: str, optional
    :param atom_id: The ID of the Runtime that processed this record.
    :type atom_id: str
    :param connector_name: The value is Trading Partner for an X12 trading partner Send operation, or Start for an X12 trading partner Listen operation.
    :type connector_name: str
    :param connector_type: x12 is the connector type for any record.
    :type connector_type: str
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: The processing date and time for this record. The format is *yyyy-MM-dd'T'HH:mm:ss'Z'*, for example, 2016-01-31T15:32:00Z.
    :type date_processed: str
    :param document_index: The numerical index of this record in the run., defaults to None
    :type document_index: int, optional
    :param error_message: Any error message associated with this record.
    :type error_message: str
    :param execution_id: The ID of the run.
    :type execution_id: str
    :param functional_id: The identifier for the type of message in the functional group., defaults to None
    :type functional_id: str, optional
    :param gs_control: The group control number., defaults to None
    :type gs_control: str, optional
    :param gs_date: The preparation date of the interchange., defaults to None
    :type gs_date: str, optional
    :param gs_time: The preparation time of the interchange., defaults to None
    :type gs_time: str, optional
    :param gs_version: The Version, Release, and Industry identifier code., defaults to None
    :type gs_version: str, optional
    :param id_: The ID of this record.
    :type id_: str
    :param isa_ack_report: The interchange acknowledgment report, which contains descriptions of interchange segment validation errors., defaults to None
    :type isa_ack_report: str, optional
    :param isa_ack_status: The interchange acknowledgment status — either Accepted, Accepted with Errors, Partially Accepted, or Rejected, defaults to None
    :type isa_ack_status: str, optional
    :param isa_control: The number that uniquely identifies the interchange., defaults to None
    :type isa_control: str, optional
    :param operation_name: The name of the operation component that processed the record.
    :type operation_name: str
    :param outbound_validation_report: The outbound validation report. This report contains descriptions of errors present in the outbound interchange. If you did not select the outbound validation option in the sending trading partner, the value is N/A. The platform omits this field for an inbound interchange., defaults to None
    :type outbound_validation_report: str, optional
    :param outbound_validation_status: The outbound validation status — is either Success, Error-Interchange, Error-Transaction Set, or N/A. For an outbound interchange for which you did not select the outbound validation option in the sending trading partner, the value is N/A. The platform omits this field for an inbound interchange., defaults to None
    :type outbound_validation_status: str, optional
    :param receiver_id: For inbound interchanges, the Interchange Receiver ID, which identifies the receiver., defaults to None
    :type receiver_id: str, optional
    :param receiver_id_qualifier: For inbound interchanges, the Interchange ID Qualifier, which categorizes the Receiver ID., defaults to None
    :type receiver_id_qualifier: str, optional
    :param sender_id: For outbound interchanges, the Interchange Sender ID, which identifies the sender., defaults to None
    :type sender_id: str, optional
    :param sender_id_qualifier: For outbound interchanges, the Interchange ID Qualifier, which categorizes the Sender ID., defaults to None
    :type sender_id_qualifier: str, optional
    :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
    :type size: int, optional
    :param st_control: The transaction set control number., defaults to None
    :type st_control: str, optional
    :param standard: The Interchange Control standard., defaults to None
    :type standard: str, optional
    :param standard_id: Displays the same information as in the **Standard** column of the user interface., defaults to None
    :type standard_id: str, optional
    :param successful: Whether the record is a success or error., defaults to None
    :type successful: bool, optional
    :param test_indicator: Specifies whether the interchange is for testing or production., defaults to None
    :type test_indicator: str, optional
    :param transaction_set: The identifier code for the transaction set., defaults to None
    :type transaction_set: str, optional
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
        ack_status: str = SENTINEL,
        agency_code: str = SENTINEL,
        app_receiver_id: str = SENTINEL,
        app_sender_id: str = SENTINEL,
        document_index: int = SENTINEL,
        functional_id: str = SENTINEL,
        gs_control: str = SENTINEL,
        gs_date: str = SENTINEL,
        gs_time: str = SENTINEL,
        gs_version: str = SENTINEL,
        isa_ack_report: str = SENTINEL,
        isa_ack_status: str = SENTINEL,
        isa_control: str = SENTINEL,
        outbound_validation_report: str = SENTINEL,
        outbound_validation_status: str = SENTINEL,
        receiver_id: str = SENTINEL,
        receiver_id_qualifier: str = SENTINEL,
        sender_id: str = SENTINEL,
        sender_id_qualifier: str = SENTINEL,
        size: int = SENTINEL,
        st_control: str = SENTINEL,
        standard: str = SENTINEL,
        standard_id: str = SENTINEL,
        successful: bool = SENTINEL,
        test_indicator: str = SENTINEL,
        transaction_set: str = SENTINEL,
        **kwargs,
    ):
        """X12ConnectorRecord

        :param account: The ID of the account in which this record ran.
        :type account: str
        :param ack_report: The acknowledgment report., defaults to None
        :type ack_report: str, optional
        :param ack_status: The acknowledgment status — either Accepted, Accepted with Errors, Partially Accepted, or Rejected., defaults to None
        :type ack_status: str, optional
        :param action_type: The type of action with which this record corresponds — Send for an outbound interchange, Get for an inbound interchange using the Disk, FTP, or SFTP communication method, or Listen for an inbound interchange using the AS2 or HTTP communication method.
        :type action_type: str
        :param agency_code: The Responsible Agency Code., defaults to None
        :type agency_code: str, optional
        :param app_receiver_id: For inbound interchanges, the Application Receiver’s Code, which identifies the receiver., defaults to None
        :type app_receiver_id: str, optional
        :param app_sender_id: For outbound interchanges, the Application Sender’s Code, which identifies the sender., defaults to None
        :type app_sender_id: str, optional
        :param atom_id: The ID of the Runtime that processed this record.
        :type atom_id: str
        :param connector_name: The value is Trading Partner for an X12 trading partner Send operation, or Start for an X12 trading partner Listen operation.
        :type connector_name: str
        :param connector_type: x12 is the connector type for any record.
        :type connector_type: str
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: The processing date and time for this record. The format is *yyyy-MM-dd'T'HH:mm:ss'Z'*, for example, 2016-01-31T15:32:00Z.
        :type date_processed: str
        :param document_index: The numerical index of this record in the run., defaults to None
        :type document_index: int, optional
        :param error_message: Any error message associated with this record.
        :type error_message: str
        :param execution_id: The ID of the run.
        :type execution_id: str
        :param functional_id: The identifier for the type of message in the functional group., defaults to None
        :type functional_id: str, optional
        :param gs_control: The group control number., defaults to None
        :type gs_control: str, optional
        :param gs_date: The preparation date of the interchange., defaults to None
        :type gs_date: str, optional
        :param gs_time: The preparation time of the interchange., defaults to None
        :type gs_time: str, optional
        :param gs_version: The Version, Release, and Industry identifier code., defaults to None
        :type gs_version: str, optional
        :param id_: The ID of this record.
        :type id_: str
        :param isa_ack_report: The interchange acknowledgment report, which contains descriptions of interchange segment validation errors., defaults to None
        :type isa_ack_report: str, optional
        :param isa_ack_status: The interchange acknowledgment status — either Accepted, Accepted with Errors, Partially Accepted, or Rejected, defaults to None
        :type isa_ack_status: str, optional
        :param isa_control: The number that uniquely identifies the interchange., defaults to None
        :type isa_control: str, optional
        :param operation_name: The name of the operation component that processed the record.
        :type operation_name: str
        :param outbound_validation_report: The outbound validation report. This report contains descriptions of errors present in the outbound interchange. If you did not select the outbound validation option in the sending trading partner, the value is N/A. The platform omits this field for an inbound interchange., defaults to None
        :type outbound_validation_report: str, optional
        :param outbound_validation_status: The outbound validation status — is either Success, Error-Interchange, Error-Transaction Set, or N/A. For an outbound interchange for which you did not select the outbound validation option in the sending trading partner, the value is N/A. The platform omits this field for an inbound interchange., defaults to None
        :type outbound_validation_status: str, optional
        :param receiver_id: For inbound interchanges, the Interchange Receiver ID, which identifies the receiver., defaults to None
        :type receiver_id: str, optional
        :param receiver_id_qualifier: For inbound interchanges, the Interchange ID Qualifier, which categorizes the Receiver ID., defaults to None
        :type receiver_id_qualifier: str, optional
        :param sender_id: For outbound interchanges, the Interchange Sender ID, which identifies the sender., defaults to None
        :type sender_id: str, optional
        :param sender_id_qualifier: For outbound interchanges, the Interchange ID Qualifier, which categorizes the Sender ID., defaults to None
        :type sender_id_qualifier: str, optional
        :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
        :type size: int, optional
        :param st_control: The transaction set control number., defaults to None
        :type st_control: str, optional
        :param standard: The Interchange Control standard., defaults to None
        :type standard: str, optional
        :param standard_id: Displays the same information as in the **Standard** column of the user interface., defaults to None
        :type standard_id: str, optional
        :param successful: Whether the record is a success or error., defaults to None
        :type successful: bool, optional
        :param test_indicator: Specifies whether the interchange is for testing or production., defaults to None
        :type test_indicator: str, optional
        :param transaction_set: The identifier code for the transaction set., defaults to None
        :type transaction_set: str, optional
        """
        self.account = account
        if ack_report is not SENTINEL:
            self.ack_report = ack_report
        if ack_status is not SENTINEL:
            self.ack_status = ack_status
        self.action_type = action_type
        if agency_code is not SENTINEL:
            self.agency_code = agency_code
        if app_receiver_id is not SENTINEL:
            self.app_receiver_id = app_receiver_id
        if app_sender_id is not SENTINEL:
            self.app_sender_id = app_sender_id
        self.atom_id = atom_id
        self.connector_name = connector_name
        self.connector_type = connector_type
        self.custom_fields = self._define_object(custom_fields, CustomFields)
        self.date_processed = date_processed
        if document_index is not SENTINEL:
            self.document_index = document_index
        self.error_message = error_message
        self.execution_id = execution_id
        if functional_id is not SENTINEL:
            self.functional_id = functional_id
        if gs_control is not SENTINEL:
            self.gs_control = gs_control
        if gs_date is not SENTINEL:
            self.gs_date = gs_date
        if gs_time is not SENTINEL:
            self.gs_time = gs_time
        if gs_version is not SENTINEL:
            self.gs_version = gs_version
        self.id_ = id_
        if isa_ack_report is not SENTINEL:
            self.isa_ack_report = isa_ack_report
        if isa_ack_status is not SENTINEL:
            self.isa_ack_status = isa_ack_status
        if isa_control is not SENTINEL:
            self.isa_control = isa_control
        self.operation_name = operation_name
        if outbound_validation_report is not SENTINEL:
            self.outbound_validation_report = outbound_validation_report
        if outbound_validation_status is not SENTINEL:
            self.outbound_validation_status = outbound_validation_status
        if receiver_id is not SENTINEL:
            self.receiver_id = receiver_id
        if receiver_id_qualifier is not SENTINEL:
            self.receiver_id_qualifier = receiver_id_qualifier
        if sender_id is not SENTINEL:
            self.sender_id = sender_id
        if sender_id_qualifier is not SENTINEL:
            self.sender_id_qualifier = sender_id_qualifier
        if size is not SENTINEL:
            self.size = size
        if st_control is not SENTINEL:
            self.st_control = st_control
        if standard is not SENTINEL:
            self.standard = standard
        if standard_id is not SENTINEL:
            self.standard_id = standard_id
        if successful is not SENTINEL:
            self.successful = successful
        if test_indicator is not SENTINEL:
            self.test_indicator = test_indicator
        if transaction_set is not SENTINEL:
            self.transaction_set = transaction_set
        self._kwargs = kwargs
