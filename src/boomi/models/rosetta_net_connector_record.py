
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_fields import CustomFields


@JsonMap(
    {
        "pip_code": "PIPCode",
        "pip_version": "PIPVersion",
        "ack_report": "ackReport",
        "ack_status": "ackStatus",
        "action_instance_identifier": "actionInstanceIdentifier",
        "action_type": "actionType",
        "atom_id": "atomId",
        "attempt_count": "attemptCount",
        "business_activity_identifier": "businessActivityIdentifier",
        "connector_name": "connectorName",
        "connector_type": "connectorType",
        "custom_fields": "customFields",
        "date_processed": "dateProcessed",
        "date_time": "dateTime",
        "document_index": "documentIndex",
        "error_message": "errorMessage",
        "execution_id": "executionId",
        "framework_version": "frameworkVersion",
        "from_global_business_service_code": "fromGlobalBusinessServiceCode",
        "from_global_partner_role_classification_code": "fromGlobalPartnerRoleClassificationCode",
        "global_business_action_code": "globalBusinessActionCode",
        "global_document_function_code": "globalDocumentFunctionCode",
        "global_process_code": "globalProcessCode",
        "global_usage_code": "globalUsageCode",
        "id_": "id",
        "in_response_to_global_business_action_code": "inResponseToGlobalBusinessActionCode",
        "in_response_to_instance_identifier": "inResponseToInstanceIdentifier",
        "is_secure_transport_required": "isSecureTransportRequired",
        "known_initiating_partner_id": "knownInitiatingPartnerID",
        "operation_name": "operationName",
        "outbound_validation_report": "outboundValidationReport",
        "outbound_validation_status": "outboundValidationStatus",
        "process_instance_identifier": "processInstanceIdentifier",
        "receiver_id": "receiverID",
        "sender_id": "senderID",
        "time_to_acknowledge_acceptance": "timeToAcknowledgeAcceptance",
        "time_to_acknowledge_receipt": "timeToAcknowledgeReceipt",
        "time_to_perform": "timeToPerform",
        "to_global_business_service_code": "toGlobalBusinessServiceCode",
        "to_global_partner_role_classification_code": "toGlobalPartnerRoleClassificationCode",
        "transaction_instance_identifier": "transactionInstanceIdentifier",
    }
)
class RosettaNetConnectorRecord(BaseModel):
    """RosettaNetConnectorRecord

    :param pip_code: The Partner Interface Process \(PIP\) code., defaults to None
    :type pip_code: str, optional
    :param pip_version: The unique version number of the PIP document., defaults to None
    :type pip_version: str, optional
    :param account: The ID of the account in which you ran the record.
    :type account: str
    :param ack_report: The acknowledgment report., defaults to None
    :type ack_report: str, optional
    :param ack_status: The acknowledgment status — either Acknowledged, Error - No Acknowledgement Returned, Exception, or Not Expected., defaults to None
    :type ack_status: str, optional
    :param action_instance_identifier: The unique identifier for the action instance., defaults to None
    :type action_instance_identifier: str, optional
    :param action_type: The type of action with which this record corresponds — Send for an outbound interchange, Get for an inbound interchange using the Disk, FTP, or SFTP communication method, or Listen for an inbound interchange using the AS2 or HTTP communication method.
    :type action_type: str
    :param atom_id: The ID of the Runtime that processed this record.
    :type atom_id: str
    :param attempt_count: The number of times you attempted the transaction — for example, 1 for the first attempt. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
    :type attempt_count: str, optional
    :param business_activity_identifier: The code identifying the business activity within the PIP., defaults to None
    :type business_activity_identifier: str, optional
    :param connector_name: The value is Trading Partner** for a RosettaNet trading partner Send operation, or Start for a RosettaNet trading partner Listen operation.
    :type connector_name: str
    :param connector_type: *rosettanet* is the connector type for any record.
    :type connector_type: str
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: The processing date and time of this record. The format is *yyyy-MM-dd'T'HH:mm:ss'Z'*, — for example, 2016-01-31T15:32:00Z.
    :type date_processed: str
    :param date_time: The date and time of the message delivery., defaults to None
    :type date_time: str, optional
    :param document_index: The numerical index of this record in the run., defaults to None
    :type document_index: int, optional
    :param error_message: Any error message associated with this record. This field is omitted for a successful interchange.
    :type error_message: str
    :param execution_id: The ID of the run.
    :type execution_id: str
    :param framework_version: The version of the RosettaNet Implementation Framework — *1.1* or *2.0* — that specifies the structure of the document represented by this record., defaults to None
    :type framework_version: str, optional
    :param from_global_business_service_code: The code identifying the sending trading partner’s business service network component., defaults to None
    :type from_global_business_service_code: str, optional
    :param from_global_partner_role_classification_code: The code identifying the role the sending trading partner plays in the PIP., defaults to None
    :type from_global_partner_role_classification_code: str, optional
    :param global_business_action_code: The business action., defaults to None
    :type global_business_action_code: str, optional
    :param global_document_function_code: Specifies whether the record represents a Request, Response, or neither; in the latter case the value is N/A. For a RosettaNet 2.0 interchange the value is N/A., defaults to None
    :type global_document_function_code: str, optional
    :param global_process_code: The name of the PIP specification document. For a RosettaNet 2.0 interchange, the value is *N/A*., defaults to None
    :type global_process_code: str, optional
    :param global_usage_code: Indicates whether the record is a Production or Test mode interchange., defaults to None
    :type global_usage_code: str, optional
    :param id_: The ID of this record.
    :type id_: str
    :param in_response_to_global_business_action_code: If the document is a response, the business action of the corresponding request., defaults to None
    :type in_response_to_global_business_action_code: str, optional
    :param in_response_to_instance_identifier: If the document is a response, the action instance identifier of the corresponding request., defaults to None
    :type in_response_to_instance_identifier: str, optional
    :param is_secure_transport_required: Yes indicates transporting the document from the next hub securely. No suggests the document does not need transporting from the next hub uniquely. For a RosettaNet 1.1 interchange, the value is N/A., defaults to None
    :type is_secure_transport_required: str, optional
    :param known_initiating_partner_id: The unique identifier for the known initiating trading partner. The value is sourced by the document property Known Initiating Partner Global Business Identifier in the process. If this document property is not set in the process, the field’s value is the same as the senderID., defaults to None
    :type known_initiating_partner_id: str, optional
    :param operation_name: The name of the operation component that processed the record.
    :type operation_name: str
    :param outbound_validation_report: The outbound validation report. This report contains descriptions of errors present in the outbound message. If you did not select the outbound validation option in the sending trading partner, the value is N/A. Inbound messages omit this field., defaults to None
    :type outbound_validation_report: str, optional
    :param outbound_validation_status: The outbound validation status — is either Success, Error-Message, or N/A. For an outbound message for which you do not select the outbound validation option in the sending trading partner, the value is N/A. Inbound messages omit this field., defaults to None
    :type outbound_validation_status: str, optional
    :param process_instance_identifier: The unique identifier for the process instance. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
    :type process_instance_identifier: str, optional
    :param receiver_id: The unique identifier for the receiving trading partner., defaults to None
    :type receiver_id: str, optional
    :param sender_id: The unique identifier for the sending trading partner., defaults to None
    :type sender_id: str, optional
    :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
    :type size: int, optional
    :param successful: Whether the record is a success or error., defaults to None
    :type successful: bool, optional
    :param time_to_acknowledge_acceptance: The length of the time-out period, in the format *CCYYMMDDThhmmss.sss*, for acknowledging acceptance of a message. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
    :type time_to_acknowledge_acceptance: str, optional
    :param time_to_acknowledge_receipt: The length of the time-out period, in the format *CCYYMMDDThhmmss.sss*, for acknowledging receipt of a message. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
    :type time_to_acknowledge_receipt: str, optional
    :param time_to_perform: The maximum length of the time period, in the format *CCYYMMDDThhmmss.sss*, that an initiating business activity waits for a responding activity to process a document. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
    :type time_to_perform: str, optional
    :param to_global_business_service_code: The code identifying the receiving trading partner’s business service network component., defaults to None
    :type to_global_business_service_code: str, optional
    :param to_global_partner_role_classification_code: The code identifying the role the receiving trading partner plays in the PIP., defaults to None
    :type to_global_partner_role_classification_code: str, optional
    :param transaction_instance_identifier: The unique identifier for the transaction instance., defaults to None
    :type transaction_instance_identifier: str, optional
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
        pip_code: str = SENTINEL,
        pip_version: str = SENTINEL,
        ack_report: str = SENTINEL,
        ack_status: str = SENTINEL,
        action_instance_identifier: str = SENTINEL,
        attempt_count: str = SENTINEL,
        business_activity_identifier: str = SENTINEL,
        date_time: str = SENTINEL,
        document_index: int = SENTINEL,
        framework_version: str = SENTINEL,
        from_global_business_service_code: str = SENTINEL,
        from_global_partner_role_classification_code: str = SENTINEL,
        global_business_action_code: str = SENTINEL,
        global_document_function_code: str = SENTINEL,
        global_process_code: str = SENTINEL,
        global_usage_code: str = SENTINEL,
        in_response_to_global_business_action_code: str = SENTINEL,
        in_response_to_instance_identifier: str = SENTINEL,
        is_secure_transport_required: str = SENTINEL,
        known_initiating_partner_id: str = SENTINEL,
        outbound_validation_report: str = SENTINEL,
        outbound_validation_status: str = SENTINEL,
        process_instance_identifier: str = SENTINEL,
        receiver_id: str = SENTINEL,
        sender_id: str = SENTINEL,
        size: int = SENTINEL,
        successful: bool = SENTINEL,
        time_to_acknowledge_acceptance: str = SENTINEL,
        time_to_acknowledge_receipt: str = SENTINEL,
        time_to_perform: str = SENTINEL,
        to_global_business_service_code: str = SENTINEL,
        to_global_partner_role_classification_code: str = SENTINEL,
        transaction_instance_identifier: str = SENTINEL,
        **kwargs,
    ):
        """RosettaNetConnectorRecord

        :param pip_code: The Partner Interface Process \(PIP\) code., defaults to None
        :type pip_code: str, optional
        :param pip_version: The unique version number of the PIP document., defaults to None
        :type pip_version: str, optional
        :param account: The ID of the account in which you ran the record.
        :type account: str
        :param ack_report: The acknowledgment report., defaults to None
        :type ack_report: str, optional
        :param ack_status: The acknowledgment status — either Acknowledged, Error - No Acknowledgement Returned, Exception, or Not Expected., defaults to None
        :type ack_status: str, optional
        :param action_instance_identifier: The unique identifier for the action instance., defaults to None
        :type action_instance_identifier: str, optional
        :param action_type: The type of action with which this record corresponds — Send for an outbound interchange, Get for an inbound interchange using the Disk, FTP, or SFTP communication method, or Listen for an inbound interchange using the AS2 or HTTP communication method.
        :type action_type: str
        :param atom_id: The ID of the Runtime that processed this record.
        :type atom_id: str
        :param attempt_count: The number of times you attempted the transaction — for example, 1 for the first attempt. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
        :type attempt_count: str, optional
        :param business_activity_identifier: The code identifying the business activity within the PIP., defaults to None
        :type business_activity_identifier: str, optional
        :param connector_name: The value is Trading Partner** for a RosettaNet trading partner Send operation, or Start for a RosettaNet trading partner Listen operation.
        :type connector_name: str
        :param connector_type: *rosettanet* is the connector type for any record.
        :type connector_type: str
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: The processing date and time of this record. The format is *yyyy-MM-dd'T'HH:mm:ss'Z'*, — for example, 2016-01-31T15:32:00Z.
        :type date_processed: str
        :param date_time: The date and time of the message delivery., defaults to None
        :type date_time: str, optional
        :param document_index: The numerical index of this record in the run., defaults to None
        :type document_index: int, optional
        :param error_message: Any error message associated with this record. This field is omitted for a successful interchange.
        :type error_message: str
        :param execution_id: The ID of the run.
        :type execution_id: str
        :param framework_version: The version of the RosettaNet Implementation Framework — *1.1* or *2.0* — that specifies the structure of the document represented by this record., defaults to None
        :type framework_version: str, optional
        :param from_global_business_service_code: The code identifying the sending trading partner’s business service network component., defaults to None
        :type from_global_business_service_code: str, optional
        :param from_global_partner_role_classification_code: The code identifying the role the sending trading partner plays in the PIP., defaults to None
        :type from_global_partner_role_classification_code: str, optional
        :param global_business_action_code: The business action., defaults to None
        :type global_business_action_code: str, optional
        :param global_document_function_code: Specifies whether the record represents a Request, Response, or neither; in the latter case the value is N/A. For a RosettaNet 2.0 interchange the value is N/A., defaults to None
        :type global_document_function_code: str, optional
        :param global_process_code: The name of the PIP specification document. For a RosettaNet 2.0 interchange, the value is *N/A*., defaults to None
        :type global_process_code: str, optional
        :param global_usage_code: Indicates whether the record is a Production or Test mode interchange., defaults to None
        :type global_usage_code: str, optional
        :param id_: The ID of this record.
        :type id_: str
        :param in_response_to_global_business_action_code: If the document is a response, the business action of the corresponding request., defaults to None
        :type in_response_to_global_business_action_code: str, optional
        :param in_response_to_instance_identifier: If the document is a response, the action instance identifier of the corresponding request., defaults to None
        :type in_response_to_instance_identifier: str, optional
        :param is_secure_transport_required: Yes indicates transporting the document from the next hub securely. No suggests the document does not need transporting from the next hub uniquely. For a RosettaNet 1.1 interchange, the value is N/A., defaults to None
        :type is_secure_transport_required: str, optional
        :param known_initiating_partner_id: The unique identifier for the known initiating trading partner. The value is sourced by the document property Known Initiating Partner Global Business Identifier in the process. If this document property is not set in the process, the field’s value is the same as the senderID., defaults to None
        :type known_initiating_partner_id: str, optional
        :param operation_name: The name of the operation component that processed the record.
        :type operation_name: str
        :param outbound_validation_report: The outbound validation report. This report contains descriptions of errors present in the outbound message. If you did not select the outbound validation option in the sending trading partner, the value is N/A. Inbound messages omit this field., defaults to None
        :type outbound_validation_report: str, optional
        :param outbound_validation_status: The outbound validation status — is either Success, Error-Message, or N/A. For an outbound message for which you do not select the outbound validation option in the sending trading partner, the value is N/A. Inbound messages omit this field., defaults to None
        :type outbound_validation_status: str, optional
        :param process_instance_identifier: The unique identifier for the process instance. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
        :type process_instance_identifier: str, optional
        :param receiver_id: The unique identifier for the receiving trading partner., defaults to None
        :type receiver_id: str, optional
        :param sender_id: The unique identifier for the sending trading partner., defaults to None
        :type sender_id: str, optional
        :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
        :type size: int, optional
        :param successful: Whether the record is a success or error., defaults to None
        :type successful: bool, optional
        :param time_to_acknowledge_acceptance: The length of the time-out period, in the format *CCYYMMDDThhmmss.sss*, for acknowledging acceptance of a message. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
        :type time_to_acknowledge_acceptance: str, optional
        :param time_to_acknowledge_receipt: The length of the time-out period, in the format *CCYYMMDDThhmmss.sss*, for acknowledging receipt of a message. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
        :type time_to_acknowledge_receipt: str, optional
        :param time_to_perform: The maximum length of the time period, in the format *CCYYMMDDThhmmss.sss*, that an initiating business activity waits for a responding activity to process a document. For a RosettaNet 2.0 interchange, the value is N/A., defaults to None
        :type time_to_perform: str, optional
        :param to_global_business_service_code: The code identifying the receiving trading partner’s business service network component., defaults to None
        :type to_global_business_service_code: str, optional
        :param to_global_partner_role_classification_code: The code identifying the role the receiving trading partner plays in the PIP., defaults to None
        :type to_global_partner_role_classification_code: str, optional
        :param transaction_instance_identifier: The unique identifier for the transaction instance., defaults to None
        :type transaction_instance_identifier: str, optional
        """
        if pip_code is not SENTINEL:
            self.pip_code = pip_code
        if pip_version is not SENTINEL:
            self.pip_version = pip_version
        self.account = account
        if ack_report is not SENTINEL:
            self.ack_report = ack_report
        if ack_status is not SENTINEL:
            self.ack_status = ack_status
        if action_instance_identifier is not SENTINEL:
            self.action_instance_identifier = action_instance_identifier
        self.action_type = action_type
        self.atom_id = atom_id
        if attempt_count is not SENTINEL:
            self.attempt_count = attempt_count
        if business_activity_identifier is not SENTINEL:
            self.business_activity_identifier = business_activity_identifier
        self.connector_name = connector_name
        self.connector_type = connector_type
        self.custom_fields = self._define_object(custom_fields, CustomFields)
        self.date_processed = date_processed
        if date_time is not SENTINEL:
            self.date_time = date_time
        if document_index is not SENTINEL:
            self.document_index = document_index
        self.error_message = error_message
        self.execution_id = execution_id
        if framework_version is not SENTINEL:
            self.framework_version = framework_version
        if from_global_business_service_code is not SENTINEL:
            self.from_global_business_service_code = from_global_business_service_code
        if from_global_partner_role_classification_code is not SENTINEL:
            self.from_global_partner_role_classification_code = (
                from_global_partner_role_classification_code
            )
        if global_business_action_code is not SENTINEL:
            self.global_business_action_code = global_business_action_code
        if global_document_function_code is not SENTINEL:
            self.global_document_function_code = global_document_function_code
        if global_process_code is not SENTINEL:
            self.global_process_code = global_process_code
        if global_usage_code is not SENTINEL:
            self.global_usage_code = global_usage_code
        self.id_ = id_
        if in_response_to_global_business_action_code is not SENTINEL:
            self.in_response_to_global_business_action_code = (
                in_response_to_global_business_action_code
            )
        if in_response_to_instance_identifier is not SENTINEL:
            self.in_response_to_instance_identifier = in_response_to_instance_identifier
        if is_secure_transport_required is not SENTINEL:
            self.is_secure_transport_required = is_secure_transport_required
        if known_initiating_partner_id is not SENTINEL:
            self.known_initiating_partner_id = known_initiating_partner_id
        self.operation_name = operation_name
        if outbound_validation_report is not SENTINEL:
            self.outbound_validation_report = outbound_validation_report
        if outbound_validation_status is not SENTINEL:
            self.outbound_validation_status = outbound_validation_status
        if process_instance_identifier is not SENTINEL:
            self.process_instance_identifier = process_instance_identifier
        if receiver_id is not SENTINEL:
            self.receiver_id = receiver_id
        if sender_id is not SENTINEL:
            self.sender_id = sender_id
        if size is not SENTINEL:
            self.size = size
        if successful is not SENTINEL:
            self.successful = successful
        if time_to_acknowledge_acceptance is not SENTINEL:
            self.time_to_acknowledge_acceptance = time_to_acknowledge_acceptance
        if time_to_acknowledge_receipt is not SENTINEL:
            self.time_to_acknowledge_receipt = time_to_acknowledge_receipt
        if time_to_perform is not SENTINEL:
            self.time_to_perform = time_to_perform
        if to_global_business_service_code is not SENTINEL:
            self.to_global_business_service_code = to_global_business_service_code
        if to_global_partner_role_classification_code is not SENTINEL:
            self.to_global_partner_role_classification_code = (
                to_global_partner_role_classification_code
            )
        if transaction_instance_identifier is not SENTINEL:
            self.transaction_instance_identifier = transaction_instance_identifier
        self._kwargs = kwargs
