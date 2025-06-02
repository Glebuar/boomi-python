
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class EventSimpleExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar EQUALS: "EQUALS"
    :vartype EQUALS: str
    :cvar LIKE: "LIKE"
    :vartype LIKE: str
    :cvar NOTEQUALS: "NOT_EQUALS"
    :vartype NOTEQUALS: str
    :cvar ISNULL: "IS_NULL"
    :vartype ISNULL: str
    :cvar ISNOTNULL: "IS_NOT_NULL"
    :vartype ISNOTNULL: str
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
    :cvar CONTAINS: "CONTAINS"
    :vartype CONTAINS: str
    :cvar NOTCONTAINS: "NOT_CONTAINS"
    :vartype NOTCONTAINS: str
    """

    EQUALS = "EQUALS"
    LIKE = "LIKE"
    NOTEQUALS = "NOT_EQUALS"
    ISNULL = "IS_NULL"
    ISNOTNULL = "IS_NOT_NULL"
    BETWEEN = "BETWEEN"
    GREATERTHAN = "GREATER_THAN"
    GREATERTHANOREQUAL = "GREATER_THAN_OR_EQUAL"
    LESSTHAN = "LESS_THAN"
    LESSTHANOREQUAL = "LESS_THAN_OR_EQUAL"
    CONTAINS = "CONTAINS"
    NOTCONTAINS = "NOT_CONTAINS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, EventSimpleExpressionOperator._member_map_.values())
        )


class EventSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar EVENTID: "eventId"
    :vartype EVENTID: str
    :cvar ACCOUNTID: "accountId"
    :vartype ACCOUNTID: str
    :cvar ATOMID: "atomId"
    :vartype ATOMID: str
    :cvar ATOMNAME: "atomName"
    :vartype ATOMNAME: str
    :cvar EVENTLEVEL: "eventLevel"
    :vartype EVENTLEVEL: str
    :cvar EVENTDATE: "eventDate"
    :vartype EVENTDATE: str
    :cvar STATUS: "status"
    :vartype STATUS: str
    :cvar EVENTTYPE: "eventType"
    :vartype EVENTTYPE: str
    :cvar EXECUTIONID: "executionId"
    :vartype EXECUTIONID: str
    :cvar TITLE: "title"
    :vartype TITLE: str
    :cvar UPDATEDATE: "updateDate"
    :vartype UPDATEDATE: str
    :cvar STARTTIME: "startTime"
    :vartype STARTTIME: str
    :cvar ENDTIME: "endTime"
    :vartype ENDTIME: str
    :cvar ERRORDOCUMENTCOUNT: "errorDocumentCount"
    :vartype ERRORDOCUMENTCOUNT: str
    :cvar INBOUNDDOCUMENTCOUNT: "inboundDocumentCount"
    :vartype INBOUNDDOCUMENTCOUNT: str
    :cvar OUTBOUNDDOCUMENTCOUNT: "outboundDocumentCount"
    :vartype OUTBOUNDDOCUMENTCOUNT: str
    :cvar PROCESSNAME: "processName"
    :vartype PROCESSNAME: str
    :cvar RECORDDATE: "recordDate"
    :vartype RECORDDATE: str
    :cvar ERROR: "error"
    :vartype ERROR: str
    :cvar ENVIRONMENT: "environment"
    :vartype ENVIRONMENT: str
    :cvar CLASSIFICATION: "classification"
    :vartype CLASSIFICATION: str
    """

    EVENTID = "eventId"
    ACCOUNTID = "accountId"
    ATOMID = "atomId"
    ATOMNAME = "atomName"
    EVENTLEVEL = "eventLevel"
    EVENTDATE = "eventDate"
    STATUS = "status"
    EVENTTYPE = "eventType"
    EXECUTIONID = "executionId"
    TITLE = "title"
    UPDATEDATE = "updateDate"
    STARTTIME = "startTime"
    ENDTIME = "endTime"
    ERRORDOCUMENTCOUNT = "errorDocumentCount"
    INBOUNDDOCUMENTCOUNT = "inboundDocumentCount"
    OUTBOUNDDOCUMENTCOUNT = "outboundDocumentCount"
    PROCESSNAME = "processName"
    RECORDDATE = "recordDate"
    ERROR = "error"
    ENVIRONMENT = "environment"
    CLASSIFICATION = "classification"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, EventSimpleExpressionProperty._member_map_.values())
        )


@JsonMap({})
class EventSimpleExpression(BaseModel):
    """EventSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: EventSimpleExpressionOperator
    :param property: property
    :type property: EventSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: EventSimpleExpressionOperator,
        property: EventSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """EventSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: EventSimpleExpressionOperator
        :param property: property
        :type property: EventSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, EventSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, EventSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
