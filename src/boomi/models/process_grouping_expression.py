
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .process_expression import ProcessExpression, ProcessExpressionGuard
from .process_simple_expression import ProcessSimpleExpression

class ProcessGroupingExpressionOperator(Enum):
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
                ProcessGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ProcessGroupingExpression(BaseModel):
    """ProcessGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["ProcessExpression"], optional
    :param operator: operator
    :type operator: ProcessGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ProcessGroupingExpressionOperator,
        nested_expression: List["ProcessExpression"] = SENTINEL,
        **kwargs,
    ):
        """ProcessGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["ProcessExpression"], optional
        :param operator: operator
        :type operator: ProcessGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .process_expression import ProcessExpression

            self.nested_expression = self._define_list(
                nested_expression, ProcessExpression
            )
        self.operator = self._enum_matching(
            operator, ProcessGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
