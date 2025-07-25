
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .execution_connector_expression import ExecutionConnectorExpression, ExecutionConnectorExpressionGuard
from .execution_connector_simple_expression import ExecutionConnectorSimpleExpression

class ExecutionConnectorGroupingExpressionOperator(Enum):
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
                ExecutionConnectorGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ExecutionConnectorGroupingExpression(BaseModel):
    """ExecutionConnectorGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ExecutionConnectorExpression], optional
    :param operator: operator
    :type operator: ExecutionConnectorGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ExecutionConnectorGroupingExpressionOperator,
        nested_expression: List[ExecutionConnectorExpression] = SENTINEL,
        **kwargs,
    ):
        """ExecutionConnectorGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ExecutionConnectorExpression], optional
        :param operator: operator
        :type operator: ExecutionConnectorGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ExecutionConnectorExpression
            )
        self.operator = self._enum_matching(
            operator, ExecutionConnectorGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
