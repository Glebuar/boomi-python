
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class EnvironmentExtensionsSimpleExpressionOperator(Enum):
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
                EnvironmentExtensionsSimpleExpressionOperator._member_map_.values(),
            )
        )


class EnvironmentExtensionsSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar ENVIRONMENTID: "environmentId"
    :vartype ENVIRONMENTID: str
    :cvar EXTENSIONGROUPID: "extensionGroupId"
    :vartype EXTENSIONGROUPID: str
    """

    ENVIRONMENTID = "environmentId"
    EXTENSIONGROUPID = "extensionGroupId"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                EnvironmentExtensionsSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class EnvironmentExtensionsSimpleExpression(BaseModel):
    """EnvironmentExtensionsSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: EnvironmentExtensionsSimpleExpressionOperator
    :param property: property
    :type property: EnvironmentExtensionsSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: EnvironmentExtensionsSimpleExpressionOperator,
        property: EnvironmentExtensionsSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """EnvironmentExtensionsSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: EnvironmentExtensionsSimpleExpressionOperator
        :param property: property
        :type property: EnvironmentExtensionsSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, EnvironmentExtensionsSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, EnvironmentExtensionsSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
