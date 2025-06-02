
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .environment_expression import EnvironmentExpression, EnvironmentExpressionGuard
from .environment_simple_expression import EnvironmentSimpleExpression

class EnvironmentGroupingExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar AND: "and"
    :vartype AND: str
    :cvar OR: "or"
    :vartype OR: str
    """

    AND = "and"
    OR = "or"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                EnvironmentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EnvironmentGroupingExpression(BaseModel):
    """EnvironmentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["EnvironmentExpression"], optional
    :param operator: operator
    :type operator: EnvironmentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EnvironmentGroupingExpressionOperator,
        nested_expression: List["EnvironmentExpression"] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["EnvironmentExpression"], optional
        :param operator: operator
        :type operator: EnvironmentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .environment_expression import EnvironmentExpression

            self.nested_expression = self._define_list(
                nested_expression, EnvironmentExpression
            )
        self.operator = self._enum_matching(
            operator, EnvironmentGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
