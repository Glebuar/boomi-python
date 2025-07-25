
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .process_schedule_status_expression import ProcessScheduleStatusExpression, ProcessScheduleStatusExpressionGuard
from .process_schedule_status_simple_expression import (
    ProcessScheduleStatusSimpleExpression,
)

class ProcessScheduleStatusGroupingExpressionOperator(Enum):
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
                ProcessScheduleStatusGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ProcessScheduleStatusGroupingExpression(BaseModel):
    """ProcessScheduleStatusGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ProcessScheduleStatusExpression], optional
    :param operator: operator
    :type operator: ProcessScheduleStatusGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ProcessScheduleStatusGroupingExpressionOperator,
        nested_expression: List[ProcessScheduleStatusExpression] = SENTINEL,
        **kwargs,
    ):
        """ProcessScheduleStatusGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ProcessScheduleStatusExpression], optional
        :param operator: operator
        :type operator: ProcessScheduleStatusGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ProcessScheduleStatusExpression
            )
        self.operator = self._enum_matching(
            operator, ProcessScheduleStatusGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
