
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class RosettaNetConnectorRecordSimpleExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar EQUALS: "EQUALS"
    :vartype EQUALS: str
    :cvar STARTSWITH: "STARTS_WITH"
    :vartype STARTSWITH: str
    :cvar BETWEEN: "BETWEEN"
    :vartype BETWEEN: str
    :cvar GREATERTHAN: "GREATER_THAN"
    :vartype GREATERTHAN: str
    :cvar GREATERTHANOREQUAL: "GREATER_THAN_OR_EQUAL"
    :vartype GREATERTHANOREQUAL: str
    :cvar LESSTHAN: "LESS_THAN"
    :vartype LESSTHAN: str
    :cvar LESSTHANOREQUAL: "LESS_THAN_OR_EQUAL"
    :vartype LESSTHANOREQUAL: str
    """

    EQUALS = "EQUALS"
    STARTSWITH = "STARTS_WITH"
    BETWEEN = "BETWEEN"
    GREATERTHAN = "GREATER_THAN"
    GREATERTHANOREQUAL = "GREATER_THAN_OR_EQUAL"
    LESSTHAN = "LESS_THAN"
    LESSTHANOREQUAL = "LESS_THAN_OR_EQUAL"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                RosettaNetConnectorRecordSimpleExpressionOperator._member_map_.values(),
            )
        )


class RosettaNetConnectorRecordSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar EXECUTIONID: "executionId"
    :vartype EXECUTIONID: str
    :cvar ATOMID: "atomId"
    :vartype ATOMID: str
    :cvar DATEPROCESSED: "dateProcessed"
    :vartype DATEPROCESSED: str
    :cvar ID: "id"
    :vartype ID: str
    :cvar ACTIONTYPE: "actionType"
    :vartype ACTIONTYPE: str
    :cvar CONNECTORTYPE: "connectorType"
    :vartype CONNECTORTYPE: str
    :cvar CONNECTORNAME: "connectorName"
    :vartype CONNECTORNAME: str
    :cvar OPERATIONNAME: "operationName"
    :vartype OPERATIONNAME: str
    :cvar DOCUMENTINDEX: "documentIndex"
    :vartype DOCUMENTINDEX: str
    :cvar SUCCESSFUL: "successful"
    :vartype SUCCESSFUL: str
    :cvar SIZE: "size"
    :vartype SIZE: str
    :cvar ERRORMESSAGE: "errorMessage"
    :vartype ERRORMESSAGE: str
    :cvar ACKSTATUS: "ackStatus"
    :vartype ACKSTATUS: str
    :cvar ACKREPORT: "ackReport"
    :vartype ACKREPORT: str
    :cvar SENDERID: "senderID"
    :vartype SENDERID: str
    :cvar RECEIVERID: "receiverID"
    :vartype RECEIVERID: str
    :cvar KNOWNINITIATINGPARTNERID: "knownInitiatingPartnerID"
    :vartype KNOWNINITIATINGPARTNERID: str
    :cvar FRAMEWORKVERSION: "frameworkVersion"
    :vartype FRAMEWORKVERSION: str
    :cvar PIPCODE: "PIPCode"
    :vartype PIPCODE: str
    :cvar PIPVERSION: "PIPVersion"
    :vartype PIPVERSION: str
    :cvar GLOBALPROCESSCODE: "globalProcessCode"
    :vartype GLOBALPROCESSCODE: str
    :cvar GLOBALBUSINESSACTIONCODE: "globalBusinessActionCode"
    :vartype GLOBALBUSINESSACTIONCODE: str
    :cvar GLOBALDOCUMENTFUNCTIONCODE: "globalDocumentFunctionCode"
    :vartype GLOBALDOCUMENTFUNCTIONCODE: str
    :cvar FROMGLOBALPARTNERROLECLASSIFICATIONCODE: "fromGlobalPartnerRoleClassificationCode"
    :vartype FROMGLOBALPARTNERROLECLASSIFICATIONCODE: str
    :cvar TOGLOBALPARTNERROLECLASSIFICATIONCODE: "toGlobalPartnerRoleClassificationCode"
    :vartype TOGLOBALPARTNERROLECLASSIFICATIONCODE: str
    :cvar FROMGLOBALBUSINESSSERVICECODE: "fromGlobalBusinessServiceCode"
    :vartype FROMGLOBALBUSINESSSERVICECODE: str
    :cvar TOGLOBALBUSINESSSERVICECODE: "toGlobalBusinessServiceCode"
    :vartype TOGLOBALBUSINESSSERVICECODE: str
    :cvar BUSINESSACTIVITYIDENTIFIER: "businessActivityIdentifier"
    :vartype BUSINESSACTIVITYIDENTIFIER: str
    :cvar PROCESSINSTANCEIDENTIFIER: "processInstanceIdentifier"
    :vartype PROCESSINSTANCEIDENTIFIER: str
    :cvar TRANSACTIONINSTANCEIDENTIFIER: "transactionInstanceIdentifier"
    :vartype TRANSACTIONINSTANCEIDENTIFIER: str
    :cvar ACTIONINSTANCEIDENTIFIER: "actionInstanceIdentifier"
    :vartype ACTIONINSTANCEIDENTIFIER: str
    :cvar INRESPONSETOGLOBALBUSINESSACTIONCODE: "inResponseToGlobalBusinessActionCode"
    :vartype INRESPONSETOGLOBALBUSINESSACTIONCODE: str
    :cvar INRESPONSETOINSTANCEIDENTIFIER: "inResponseToInstanceIdentifier"
    :vartype INRESPONSETOINSTANCEIDENTIFIER: str
    :cvar GLOBALUSAGECODE: "globalUsageCode"
    :vartype GLOBALUSAGECODE: str
    :cvar ATTEMPTCOUNT: "attemptCount"
    :vartype ATTEMPTCOUNT: str
    :cvar DATETIME: "dateTime"
    :vartype DATETIME: str
    :cvar ISSECURETRANSPORTREQUIRED: "isSecureTransportRequired"
    :vartype ISSECURETRANSPORTREQUIRED: str
    :cvar TIMETOACKNOWLEDGEACCEPTANCE: "timeToAcknowledgeAcceptance"
    :vartype TIMETOACKNOWLEDGEACCEPTANCE: str
    :cvar TIMETOACKNOWLEDGERECEIPT: "timeToAcknowledgeReceipt"
    :vartype TIMETOACKNOWLEDGERECEIPT: str
    :cvar TIMETOPERFORM: "timeToPerform"
    :vartype TIMETOPERFORM: str
    :cvar OUTBOUNDVALIDATIONSTATUS: "outboundValidationStatus"
    :vartype OUTBOUNDVALIDATIONSTATUS: str
    :cvar OUTBOUNDVALIDATIONREPORT: "outboundValidationReport"
    :vartype OUTBOUNDVALIDATIONREPORT: str
    """

    EXECUTIONID = "executionId"
    ATOMID = "atomId"
    DATEPROCESSED = "dateProcessed"
    ID = "id"
    ACTIONTYPE = "actionType"
    CONNECTORTYPE = "connectorType"
    CONNECTORNAME = "connectorName"
    OPERATIONNAME = "operationName"
    DOCUMENTINDEX = "documentIndex"
    SUCCESSFUL = "successful"
    SIZE = "size"
    ERRORMESSAGE = "errorMessage"
    ACKSTATUS = "ackStatus"
    ACKREPORT = "ackReport"
    SENDERID = "senderID"
    RECEIVERID = "receiverID"
    KNOWNINITIATINGPARTNERID = "knownInitiatingPartnerID"
    FRAMEWORKVERSION = "frameworkVersion"
    PIPCODE = "PIPCode"
    PIPVERSION = "PIPVersion"
    GLOBALPROCESSCODE = "globalProcessCode"
    GLOBALBUSINESSACTIONCODE = "globalBusinessActionCode"
    GLOBALDOCUMENTFUNCTIONCODE = "globalDocumentFunctionCode"
    FROMGLOBALPARTNERROLECLASSIFICATIONCODE = "fromGlobalPartnerRoleClassificationCode"
    TOGLOBALPARTNERROLECLASSIFICATIONCODE = "toGlobalPartnerRoleClassificationCode"
    FROMGLOBALBUSINESSSERVICECODE = "fromGlobalBusinessServiceCode"
    TOGLOBALBUSINESSSERVICECODE = "toGlobalBusinessServiceCode"
    BUSINESSACTIVITYIDENTIFIER = "businessActivityIdentifier"
    PROCESSINSTANCEIDENTIFIER = "processInstanceIdentifier"
    TRANSACTIONINSTANCEIDENTIFIER = "transactionInstanceIdentifier"
    ACTIONINSTANCEIDENTIFIER = "actionInstanceIdentifier"
    INRESPONSETOGLOBALBUSINESSACTIONCODE = "inResponseToGlobalBusinessActionCode"
    INRESPONSETOINSTANCEIDENTIFIER = "inResponseToInstanceIdentifier"
    GLOBALUSAGECODE = "globalUsageCode"
    ATTEMPTCOUNT = "attemptCount"
    DATETIME = "dateTime"
    ISSECURETRANSPORTREQUIRED = "isSecureTransportRequired"
    TIMETOACKNOWLEDGEACCEPTANCE = "timeToAcknowledgeAcceptance"
    TIMETOACKNOWLEDGERECEIPT = "timeToAcknowledgeReceipt"
    TIMETOPERFORM = "timeToPerform"
    OUTBOUNDVALIDATIONSTATUS = "outboundValidationStatus"
    OUTBOUNDVALIDATIONREPORT = "outboundValidationReport"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                RosettaNetConnectorRecordSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class RosettaNetConnectorRecordSimpleExpression(BaseModel):
    """RosettaNetConnectorRecordSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: RosettaNetConnectorRecordSimpleExpressionOperator
    :param property: property
    :type property: RosettaNetConnectorRecordSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: RosettaNetConnectorRecordSimpleExpressionOperator,
        property: RosettaNetConnectorRecordSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """RosettaNetConnectorRecordSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: RosettaNetConnectorRecordSimpleExpressionOperator
        :param property: property
        :type property: RosettaNetConnectorRecordSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator,
            RosettaNetConnectorRecordSimpleExpressionOperator.list(),
            "operator",
        )
        self.property = self._enum_matching(
            property,
            RosettaNetConnectorRecordSimpleExpressionProperty.list(),
            "property",
        )
        self._kwargs = kwargs
