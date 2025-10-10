
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ExecutionRecordSimpleExpressionOperator(Enum):
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
            map(
                lambda x: x.value,
                ExecutionRecordSimpleExpressionOperator._member_map_.values(),
            )
        )


class ExecutionRecordSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar EXECUTIONID: "executionId"
    :vartype EXECUTIONID: str
    :cvar ORIGINALEXECUTIONID: "originalExecutionId"
    :vartype ORIGINALEXECUTIONID: str
    :cvar ACCOUNT: "account"
    :vartype ACCOUNT: str
    :cvar EXECUTIONTIME: "executionTime"
    :vartype EXECUTIONTIME: str
    :cvar STATUS: "status"
    :vartype STATUS: str
    :cvar EXECUTIONTYPE: "executionType"
    :vartype EXECUTIONTYPE: str
    :cvar PROCESSNAME: "processName"
    :vartype PROCESSNAME: str
    :cvar PROCESSID: "processId"
    :vartype PROCESSID: str
    :cvar ATOMNAME: "atomName"
    :vartype ATOMNAME: str
    :cvar ATOMID: "atomId"
    :vartype ATOMID: str
    :cvar INBOUNDDOCUMENTCOUNT: "inboundDocumentCount"
    :vartype INBOUNDDOCUMENTCOUNT: str
    :cvar OUTBOUNDDOCUMENTCOUNT: "outboundDocumentCount"
    :vartype OUTBOUNDDOCUMENTCOUNT: str
    :cvar EXECUTIONDURATION: "executionDuration"
    :vartype EXECUTIONDURATION: str
    :cvar MESSAGE: "message"
    :vartype MESSAGE: str
    :cvar REPORTKEY: "reportKey"
    :vartype REPORTKEY: str
    :cvar LAUNCHERID: "launcherId"
    :vartype LAUNCHERID: str
    :cvar NODEID: "nodeId"
    :vartype NODEID: str
    :cvar RECORDEDDATE: "recordedDate"
    :vartype RECORDEDDATE: str
    """

    EXECUTIONID = "executionId"
    ORIGINALEXECUTIONID = "originalExecutionId"
    ACCOUNT = "account"
    EXECUTIONTIME = "executionTime"
    STATUS = "status"
    EXECUTIONTYPE = "executionType"
    PROCESSNAME = "processName"
    PROCESSID = "processId"
    ATOMNAME = "atomName"
    ATOMID = "atomId"
    INBOUNDDOCUMENTCOUNT = "inboundDocumentCount"
    OUTBOUNDDOCUMENTCOUNT = "outboundDocumentCount"
    EXECUTIONDURATION = "executionDuration"
    MESSAGE = "message"
    REPORTKEY = "reportKey"
    LAUNCHERID = "launcherId"
    NODEID = "nodeId"
    RECORDEDDATE = "recordedDate"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                ExecutionRecordSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class ExecutionRecordSimpleExpression(BaseModel):
    """ExecutionRecordSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: ExecutionRecordSimpleExpressionOperator
    :param property: property
    :type property: ExecutionRecordSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: ExecutionRecordSimpleExpressionOperator,
        property: ExecutionRecordSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """ExecutionRecordSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: ExecutionRecordSimpleExpressionOperator
        :param property: property
        :type property: ExecutionRecordSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, ExecutionRecordSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, ExecutionRecordSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
