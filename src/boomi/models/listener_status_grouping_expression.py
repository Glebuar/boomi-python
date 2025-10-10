
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .listener_status_expression import ListenerStatusExpression, ListenerStatusExpressionGuard
from .listener_status_simple_expression import ListenerStatusSimpleExpression

class ListenerStatusGroupingExpressionOperator(Enum):
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
                ListenerStatusGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ListenerStatusGroupingExpression(BaseModel):
    """ListenerStatusGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ListenerStatusExpression], optional
    :param operator: operator
    :type operator: ListenerStatusGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ListenerStatusGroupingExpressionOperator,
        nested_expression: List[ListenerStatusExpression] = SENTINEL,
        **kwargs,
    ):
        """ListenerStatusGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ListenerStatusExpression], optional
        :param operator: operator
        :type operator: ListenerStatusGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ListenerStatusExpression
            )
        self.operator = self._enum_matching(
            operator, ListenerStatusGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
