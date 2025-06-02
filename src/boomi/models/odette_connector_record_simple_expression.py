
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class OdetteConnectorRecordSimpleExpressionOperator(Enum):
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
                OdetteConnectorRecordSimpleExpressionOperator._member_map_.values(),
            )
        )


@JsonMap({})
class OdetteConnectorRecordSimpleExpression(BaseModel):
    """OdetteConnectorRecordSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: The STARTS_WITH operator accepts values that do not include spaces.
    :type operator: OdetteConnectorRecordSimpleExpressionOperator
    :param property: property
    :type property: str
    """

    def __init__(
        self,
        operator: OdetteConnectorRecordSimpleExpressionOperator,
        property: str,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """OdetteConnectorRecordSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: The STARTS_WITH operator accepts values that do not include spaces.
        :type operator: OdetteConnectorRecordSimpleExpressionOperator
        :param property: property
        :type property: str
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, OdetteConnectorRecordSimpleExpressionOperator.list(), "operator"
        )
        self.property = property
        self._kwargs = kwargs
