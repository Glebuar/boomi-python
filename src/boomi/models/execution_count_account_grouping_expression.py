
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .execution_count_account_expression import ExecutionCountAccountExpression, ExecutionCountAccountExpressionGuard
from .execution_count_account_simple_expression import (
    ExecutionCountAccountSimpleExpression,
)

class ExecutionCountAccountGroupingExpressionOperator(Enum):
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
                ExecutionCountAccountGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ExecutionCountAccountGroupingExpression(BaseModel):
    """ExecutionCountAccountGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ExecutionCountAccountExpression], optional
    :param operator: operator
    :type operator: ExecutionCountAccountGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ExecutionCountAccountGroupingExpressionOperator,
        nested_expression: List[ExecutionCountAccountExpression] = SENTINEL,
        **kwargs,
    ):
        """ExecutionCountAccountGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ExecutionCountAccountExpression], optional
        :param operator: operator
        :type operator: ExecutionCountAccountGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ExecutionCountAccountExpression
            )
        self.operator = self._enum_matching(
            operator, ExecutionCountAccountGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
