
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .throughput_account_group_expression import ThroughputAccountGroupExpression, ThroughputAccountGroupExpressionGuard
from .throughput_account_group_simple_expression import (
    ThroughputAccountGroupSimpleExpression,
)

class ThroughputAccountGroupGroupingExpressionOperator(Enum):
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
                ThroughputAccountGroupGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ThroughputAccountGroupGroupingExpression(BaseModel):
    """ThroughputAccountGroupGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ThroughputAccountGroupExpression], optional
    :param operator: operator
    :type operator: ThroughputAccountGroupGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ThroughputAccountGroupGroupingExpressionOperator,
        nested_expression: List[ThroughputAccountGroupExpression] = SENTINEL,
        **kwargs,
    ):
        """ThroughputAccountGroupGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ThroughputAccountGroupExpression], optional
        :param operator: operator
        :type operator: ThroughputAccountGroupGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ThroughputAccountGroupExpression
            )
        self.operator = self._enum_matching(
            operator,
            ThroughputAccountGroupGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
