
from __future__ import annotations
from enum import Enum
from typing import List, Union, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

class ExecutionRecordGroupingExpressionOperator(Enum):
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
                ExecutionRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ExecutionRecordGroupingExpression(BaseModel):
    """ExecutionRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[Union[dict, object]], optional
    :param operator: operator
    :type operator: ExecutionRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ExecutionRecordGroupingExpressionOperator,
        nested_expression: List[Union[dict, object]] = SENTINEL,
        **kwargs,
    ):
        """ExecutionRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[Union[dict, object]], optional
        :param operator: operator
        :type operator: ExecutionRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            # Handle nested expressions which can be SimpleExpression or GroupingExpression
            # For now, store them as raw dicts since they're used in query construction
            self.nested_expression = nested_expression
        self.operator = self._enum_matching(
            operator, ExecutionRecordGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
