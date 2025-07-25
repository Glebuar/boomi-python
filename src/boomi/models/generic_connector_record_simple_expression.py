
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class GenericConnectorRecordSimpleExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar EQUALS: "EQUALS"
    :vartype EQUALS: str
    """

    EQUALS = "EQUALS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                GenericConnectorRecordSimpleExpressionOperator._member_map_.values(),
            )
        )


class GenericConnectorRecordSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar ID: "id"
    :vartype ID: str
    :cvar EXECUTIONCONNECTORID: "executionConnectorId"
    :vartype EXECUTIONCONNECTORID: str
    :cvar EXECUTIONID: "executionId"
    :vartype EXECUTIONID: str
    :cvar CONNECTIONID: "connectionId"
    :vartype CONNECTIONID: str
    :cvar OPERATIONID: "operationId"
    :vartype OPERATIONID: str
    :cvar ACTIONTYPE: "actionType"
    :vartype ACTIONTYPE: str
    :cvar CONNECTORTYPE: "connectorType"
    :vartype CONNECTORTYPE: str
    :cvar ATOMID: "atomId"
    :vartype ATOMID: str
    :cvar DATEPROCESSED: "dateProcessed"
    :vartype DATEPROCESSED: str
    :cvar CONNECTIONNAME: "connectionName"
    :vartype CONNECTIONNAME: str
    :cvar OPERATIONNAME: "operationName"
    :vartype OPERATIONNAME: str
    :cvar ERRORMESSAGE: "errorMessage"
    :vartype ERRORMESSAGE: str
    :cvar STATUS: "status"
    :vartype STATUS: str
    :cvar DOCUMENTINDEX: "documentIndex"
    :vartype DOCUMENTINDEX: str
    :cvar INCREMENTALDOCUMENTINDEX: "incrementalDocumentIndex"
    :vartype INCREMENTALDOCUMENTINDEX: str
    :cvar SIZE: "size"
    :vartype SIZE: str
    :cvar STARTSHAPE: "startShape"
    :vartype STARTSHAPE: str
    :cvar RETRYABLE: "retryable"
    :vartype RETRYABLE: str
    """

    ID = "id"
    EXECUTIONCONNECTORID = "executionConnectorId"
    EXECUTIONID = "executionId"
    CONNECTIONID = "connectionId"
    OPERATIONID = "operationId"
    ACTIONTYPE = "actionType"
    CONNECTORTYPE = "connectorType"
    ATOMID = "atomId"
    DATEPROCESSED = "dateProcessed"
    CONNECTIONNAME = "connectionName"
    OPERATIONNAME = "operationName"
    ERRORMESSAGE = "errorMessage"
    STATUS = "status"
    DOCUMENTINDEX = "documentIndex"
    INCREMENTALDOCUMENTINDEX = "incrementalDocumentIndex"
    SIZE = "size"
    STARTSHAPE = "startShape"
    RETRYABLE = "retryable"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                GenericConnectorRecordSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class GenericConnectorRecordSimpleExpression(BaseModel):
    """GenericConnectorRecordSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: GenericConnectorRecordSimpleExpressionOperator
    :param property: property
    :type property: GenericConnectorRecordSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: GenericConnectorRecordSimpleExpressionOperator,
        property: GenericConnectorRecordSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """GenericConnectorRecordSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: GenericConnectorRecordSimpleExpressionOperator
        :param property: property
        :type property: GenericConnectorRecordSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, GenericConnectorRecordSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, GenericConnectorRecordSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
