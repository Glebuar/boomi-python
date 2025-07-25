
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class AccountSimpleExpressionOperator(Enum):
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
                lambda x: x.value, AccountSimpleExpressionOperator._member_map_.values()
            )
        )


class AccountSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar ACCOUNTID: "ACCOUNTID"
    :vartype ACCOUNTID: str
    :cvar DATECREATED: "DATECREATED"
    :vartype DATECREATED: str
    :cvar EXPIRATIONDATE: "EXPIRATIONDATE"
    :vartype EXPIRATIONDATE: str
    :cvar NAME: "NAME"
    :vartype NAME: str
    :cvar STATUS: "STATUS"
    :vartype STATUS: str
    :cvar WIDGETACCOUNT: "WIDGETACCOUNT"
    :vartype WIDGETACCOUNT: str
    :cvar OVERDEPLOYED: "OVERDEPLOYED"
    :vartype OVERDEPLOYED: str
    """

    ACCOUNTID = "ACCOUNTID"
    DATECREATED = "DATECREATED"
    EXPIRATIONDATE = "EXPIRATIONDATE"
    NAME = "NAME"
    STATUS = "STATUS"
    WIDGETACCOUNT = "WIDGETACCOUNT"
    OVERDEPLOYED = "OVERDEPLOYED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, AccountSimpleExpressionProperty._member_map_.values()
            )
        )


@JsonMap({})
class AccountSimpleExpression(BaseModel):
    """AccountSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: AccountSimpleExpressionOperator
    :param property: property
    :type property: AccountSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: AccountSimpleExpressionOperator,
        property: AccountSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """AccountSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: AccountSimpleExpressionOperator
        :param property: property
        :type property: AccountSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, AccountSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, AccountSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
