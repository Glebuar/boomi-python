
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .execution_count_account_group_expression import ExecutionCountAccountGroupExpression, ExecutionCountAccountGroupExpressionGuard
from .execution_count_account_group_simple_expression import (
    ExecutionCountAccountGroupSimpleExpression,
)

class ExecutionCountAccountGroupGroupingExpressionOperator(Enum):
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
                ExecutionCountAccountGroupGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ExecutionCountAccountGroupGroupingExpression(BaseModel):
    """ExecutionCountAccountGroupGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ExecutionCountAccountGroupExpression], optional
    :param operator: operator
    :type operator: ExecutionCountAccountGroupGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ExecutionCountAccountGroupGroupingExpressionOperator,
        nested_expression: List[ExecutionCountAccountGroupExpression] = SENTINEL,
        **kwargs,
    ):
        """ExecutionCountAccountGroupGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ExecutionCountAccountGroupExpression], optional
        :param operator: operator
        :type operator: ExecutionCountAccountGroupGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ExecutionCountAccountGroupExpression
            )
        self.operator = self._enum_matching(
            operator,
            ExecutionCountAccountGroupGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
