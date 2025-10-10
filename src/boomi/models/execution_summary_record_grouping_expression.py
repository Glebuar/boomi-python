
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .execution_summary_record_expression import ExecutionSummaryRecordExpression, ExecutionSummaryRecordExpressionGuard
from .execution_summary_record_simple_expression import (
    ExecutionSummaryRecordSimpleExpression,
)

class ExecutionSummaryRecordGroupingExpressionOperator(Enum):
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
                ExecutionSummaryRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ExecutionSummaryRecordGroupingExpression(BaseModel):
    """ExecutionSummaryRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ExecutionSummaryRecordExpression], optional
    :param operator: operator
    :type operator: ExecutionSummaryRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ExecutionSummaryRecordGroupingExpressionOperator,
        nested_expression: List[ExecutionSummaryRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """ExecutionSummaryRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ExecutionSummaryRecordExpression], optional
        :param operator: operator
        :type operator: ExecutionSummaryRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ExecutionSummaryRecordExpression
            )
        self.operator = self._enum_matching(
            operator,
            ExecutionSummaryRecordGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
