
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class EdifactConnectorRecordSimpleExpressionOperator(Enum):
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
                EdifactConnectorRecordSimpleExpressionOperator._member_map_.values(),
            )
        )


class EdifactConnectorRecordSimpleExpressionProperty(Enum):
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
    :cvar INTERCHANGECONTROLREFERENCE: "interchangeControlReference"
    :vartype INTERCHANGECONTROLREFERENCE: str
    :cvar MESSAGETYPE: "messageType"
    :vartype MESSAGETYPE: str
    :cvar MESSAGEREFERENCENUMBER: "messageReferenceNumber"
    :vartype MESSAGEREFERENCENUMBER: str
    :cvar INTERCHANGEDATE: "interchangeDate"
    :vartype INTERCHANGEDATE: str
    :cvar INTERCHANGETIME: "interchangeTime"
    :vartype INTERCHANGETIME: str
    :cvar ACKREQUESTED: "ackRequested"
    :vartype ACKREQUESTED: str
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
    INTERCHANGECONTROLREFERENCE = "interchangeControlReference"
    MESSAGETYPE = "messageType"
    MESSAGEREFERENCENUMBER = "messageReferenceNumber"
    INTERCHANGEDATE = "interchangeDate"
    INTERCHANGETIME = "interchangeTime"
    ACKREQUESTED = "ackRequested"
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
                EdifactConnectorRecordSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class EdifactConnectorRecordSimpleExpression(BaseModel):
    """EdifactConnectorRecordSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: EdifactConnectorRecordSimpleExpressionOperator
    :param property: property
    :type property: EdifactConnectorRecordSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: EdifactConnectorRecordSimpleExpressionOperator,
        property: EdifactConnectorRecordSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """EdifactConnectorRecordSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: EdifactConnectorRecordSimpleExpressionOperator
        :param property: property
        :type property: EdifactConnectorRecordSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, EdifactConnectorRecordSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, EdifactConnectorRecordSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
