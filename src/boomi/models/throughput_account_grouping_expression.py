
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .throughput_account_expression import ThroughputAccountExpression, ThroughputAccountExpressionGuard
from .throughput_account_simple_expression import ThroughputAccountSimpleExpression

class ThroughputAccountGroupingExpressionOperator(Enum):
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
                ThroughputAccountGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ThroughputAccountGroupingExpression(BaseModel):
    """ThroughputAccountGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ThroughputAccountExpression], optional
    :param operator: operator
    :type operator: ThroughputAccountGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ThroughputAccountGroupingExpressionOperator,
        nested_expression: List[ThroughputAccountExpression] = SENTINEL,
        **kwargs,
    ):
        """ThroughputAccountGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ThroughputAccountExpression], optional
        :param operator: operator
        :type operator: ThroughputAccountGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ThroughputAccountExpression
            )
        self.operator = self._enum_matching(
            operator, ThroughputAccountGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
