
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class TradacomsConnectorRecordSimpleExpressionOperator(Enum):
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
                TradacomsConnectorRecordSimpleExpressionOperator._member_map_.values(),
            )
        )


class TradacomsConnectorRecordSimpleExpressionProperty(Enum):
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
    :cvar VALIDATIONSTATUS: "validationStatus"
    :vartype VALIDATIONSTATUS: str
    :cvar VALIDATIONREPORT: "validationReport"
    :vartype VALIDATIONREPORT: str
    :cvar SENDERNAME: "senderName"
    :vartype SENDERNAME: str
    :cvar RECEIVERNAME: "receiverName"
    :vartype RECEIVERNAME: str
    :cvar MESSAGETYPE: "messageType"
    :vartype MESSAGETYPE: str
    :cvar DATE: "date"
    :vartype DATE: str
    :cvar TIME: "time"
    :vartype TIME: str
    :cvar SENDERTRANSMISSIONREFERENCE: "senderTransmissionReference"
    :vartype SENDERTRANSMISSIONREFERENCE: str
    :cvar RECEIVERTRANSMISSIONREFERENCE: "receiverTransmissionReference"
    :vartype RECEIVERTRANSMISSIONREFERENCE: str
    :cvar APPLICATIONREFERENCE: "applicationReference"
    :vartype APPLICATIONREFERENCE: str
    :cvar TRANSMISSIONPRIORITYCODE: "transmissionPriorityCode"
    :vartype TRANSMISSIONPRIORITYCODE: str
    :cvar FILEGENERATIONNUMBER: "fileGenerationNumber"
    :vartype FILEGENERATIONNUMBER: str
    :cvar FILEVERSIONNUMBER: "fileVersionNumber"
    :vartype FILEVERSIONNUMBER: str
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
    VALIDATIONSTATUS = "validationStatus"
    VALIDATIONREPORT = "validationReport"
    SENDERNAME = "senderName"
    RECEIVERNAME = "receiverName"
    MESSAGETYPE = "messageType"
    DATE = "date"
    TIME = "time"
    SENDERTRANSMISSIONREFERENCE = "senderTransmissionReference"
    RECEIVERTRANSMISSIONREFERENCE = "receiverTransmissionReference"
    APPLICATIONREFERENCE = "applicationReference"
    TRANSMISSIONPRIORITYCODE = "transmissionPriorityCode"
    FILEGENERATIONNUMBER = "fileGenerationNumber"
    FILEVERSIONNUMBER = "fileVersionNumber"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                TradacomsConnectorRecordSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class TradacomsConnectorRecordSimpleExpression(BaseModel):
    """TradacomsConnectorRecordSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: TradacomsConnectorRecordSimpleExpressionOperator
    :param property: property
    :type property: TradacomsConnectorRecordSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: TradacomsConnectorRecordSimpleExpressionOperator,
        property: TradacomsConnectorRecordSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """TradacomsConnectorRecordSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: TradacomsConnectorRecordSimpleExpressionOperator
        :param property: property
        :type property: TradacomsConnectorRecordSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator,
            TradacomsConnectorRecordSimpleExpressionOperator.list(),
            "operator",
        )
        self.property = self._enum_matching(
            property,
            TradacomsConnectorRecordSimpleExpressionProperty.list(),
            "property",
        )
        self._kwargs = kwargs
