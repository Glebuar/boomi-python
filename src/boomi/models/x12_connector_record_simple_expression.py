
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class X12ConnectorRecordSimpleExpressionOperator(Enum):
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
                X12ConnectorRecordSimpleExpressionOperator._member_map_.values(),
            )
        )


class X12ConnectorRecordSimpleExpressionProperty(Enum):
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
    :cvar ISAACKSTATUS: "isaAckStatus"
    :vartype ISAACKSTATUS: str
    :cvar ISAACKREPORT: "isaAckReport"
    :vartype ISAACKREPORT: str
    :cvar ACKSTATUS: "ackStatus"
    :vartype ACKSTATUS: str
    :cvar ACKREPORT: "ackReport"
    :vartype ACKREPORT: str
    :cvar ISACONTROL: "isaControl"
    :vartype ISACONTROL: str
    :cvar GSCONTROL: "gsControl"
    :vartype GSCONTROL: str
    :cvar STCONTROL: "stControl"
    :vartype STCONTROL: str
    :cvar FUNCTIONALID: "functionalID"
    :vartype FUNCTIONALID: str
    :cvar TRANSACTIONSET: "transactionSet"
    :vartype TRANSACTIONSET: str
    :cvar TESTINDICATOR: "testIndicator"
    :vartype TESTINDICATOR: str
    :cvar SENDERIDQUALIFIER: "senderIDQualifier"
    :vartype SENDERIDQUALIFIER: str
    :cvar SENDERID: "senderID"
    :vartype SENDERID: str
    :cvar RECEIVERIDQUALIFIER: "receiverIDQualifier"
    :vartype RECEIVERIDQUALIFIER: str
    :cvar RECEIVERID: "receiverID"
    :vartype RECEIVERID: str
    :cvar APPSENDERID: "appSenderID"
    :vartype APPSENDERID: str
    :cvar APPRECEIVERID: "appReceiverID"
    :vartype APPRECEIVERID: str
    :cvar STANDARDID: "standardID"
    :vartype STANDARDID: str
    :cvar STANDARD: "standard"
    :vartype STANDARD: str
    :cvar GSVERSION: "gsVersion"
    :vartype GSVERSION: str
    :cvar AGENCYCODE: "agencyCode"
    :vartype AGENCYCODE: str
    :cvar GSDATE: "gsDate"
    :vartype GSDATE: str
    :cvar GSTIME: "gsTime"
    :vartype GSTIME: str
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
    ISAACKSTATUS = "isaAckStatus"
    ISAACKREPORT = "isaAckReport"
    ACKSTATUS = "ackStatus"
    ACKREPORT = "ackReport"
    ISACONTROL = "isaControl"
    GSCONTROL = "gsControl"
    STCONTROL = "stControl"
    FUNCTIONALID = "functionalID"
    TRANSACTIONSET = "transactionSet"
    TESTINDICATOR = "testIndicator"
    SENDERIDQUALIFIER = "senderIDQualifier"
    SENDERID = "senderID"
    RECEIVERIDQUALIFIER = "receiverIDQualifier"
    RECEIVERID = "receiverID"
    APPSENDERID = "appSenderID"
    APPRECEIVERID = "appReceiverID"
    STANDARDID = "standardID"
    STANDARD = "standard"
    GSVERSION = "gsVersion"
    AGENCYCODE = "agencyCode"
    GSDATE = "gsDate"
    GSTIME = "gsTime"
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
                X12ConnectorRecordSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class X12ConnectorRecordSimpleExpression(BaseModel):
    """X12ConnectorRecordSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: X12ConnectorRecordSimpleExpressionOperator
    :param property: property
    :type property: X12ConnectorRecordSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: X12ConnectorRecordSimpleExpressionOperator,
        property: X12ConnectorRecordSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """X12ConnectorRecordSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: X12ConnectorRecordSimpleExpressionOperator
        :param property: property
        :type property: X12ConnectorRecordSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, X12ConnectorRecordSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, X12ConnectorRecordSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
