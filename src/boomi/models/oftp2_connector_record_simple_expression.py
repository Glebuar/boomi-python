
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class Oftp2ConnectorRecordSimpleExpressionOperator(Enum):
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
                Oftp2ConnectorRecordSimpleExpressionOperator._member_map_.values(),
            )
        )


class Oftp2ConnectorRecordSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar SFIDDSN: "sfiddsn"
    :vartype SFIDDSN: str
    :cvar SFIDDATE: "sfiddate"
    :vartype SFIDDATE: str
    :cvar SFIDTIME: "sfidtime"
    :vartype SFIDTIME: str
    :cvar SFIDDEST: "sfiddest"
    :vartype SFIDDEST: str
    :cvar INITIATORSSIDCODE: "initiator_ssidcode"
    :vartype INITIATORSSIDCODE: str
    :cvar RESPONDERSSIDCODE: "responder_ssidcode"
    :vartype RESPONDERSSIDCODE: str
    :cvar SFIDORIG: "sfidorig"
    :vartype SFIDORIG: str
    :cvar SFIDSEC: "sfidsec"
    :vartype SFIDSEC: str
    :cvar SFIDCOMP: "sfidcomp"
    :vartype SFIDCOMP: str
    :cvar SFIDCIPH: "sfidciph"
    :vartype SFIDCIPH: str
    :cvar SFIDDESC: "sfiddesc"
    :vartype SFIDDESC: str
    :cvar SFIDSIGN: "sfidsign"
    :vartype SFIDSIGN: str
    :cvar SFIDOSIZ: "sfidosiz"
    :vartype SFIDOSIZ: str
    :cvar SFIDENV: "sfidenv"
    :vartype SFIDENV: str
    :cvar STATUS: "status"
    :vartype STATUS: str
    :cvar ACCOUNT: "account"
    :vartype ACCOUNT: str
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
    :cvar CUSTOMFIELDS: "customFields"
    :vartype CUSTOMFIELDS: str
    :cvar NAREAS: "nareas"
    :vartype NAREAS: str
    :cvar NAREAST: "nareast"
    :vartype NAREAST: str
    """

    SFIDDSN = "sfiddsn"
    SFIDDATE = "sfiddate"
    SFIDTIME = "sfidtime"
    SFIDDEST = "sfiddest"
    INITIATORSSIDCODE = "initiator_ssidcode"
    RESPONDERSSIDCODE = "responder_ssidcode"
    SFIDORIG = "sfidorig"
    SFIDSEC = "sfidsec"
    SFIDCOMP = "sfidcomp"
    SFIDCIPH = "sfidciph"
    SFIDDESC = "sfiddesc"
    SFIDSIGN = "sfidsign"
    SFIDOSIZ = "sfidosiz"
    SFIDENV = "sfidenv"
    STATUS = "status"
    ACCOUNT = "account"
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
    CUSTOMFIELDS = "customFields"
    NAREAS = "nareas"
    NAREAST = "nareast"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                Oftp2ConnectorRecordSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class Oftp2ConnectorRecordSimpleExpression(BaseModel):
    """Oftp2ConnectorRecordSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: Oftp2ConnectorRecordSimpleExpressionOperator
    :param property: property
    :type property: Oftp2ConnectorRecordSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: Oftp2ConnectorRecordSimpleExpressionOperator,
        property: Oftp2ConnectorRecordSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """Oftp2ConnectorRecordSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: Oftp2ConnectorRecordSimpleExpressionOperator
        :param property: property
        :type property: Oftp2ConnectorRecordSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, Oftp2ConnectorRecordSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, Oftp2ConnectorRecordSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
