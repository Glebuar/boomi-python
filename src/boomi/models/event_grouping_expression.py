
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .event_expression import EventExpression, EventExpressionGuard
from .event_simple_expression import EventSimpleExpression

class EventGroupingExpressionOperator(Enum):
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
                lambda x: x.value, EventGroupingExpressionOperator._member_map_.values()
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EventGroupingExpression(BaseModel):
    """EventGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["EventExpression"], optional
    :param operator: operator
    :type operator: EventGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EventGroupingExpressionOperator,
        nested_expression: List["EventExpression"] = SENTINEL,
        **kwargs,
    ):
        """EventGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["EventExpression"], optional
        :param operator: operator
        :type operator: EventGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .event_expression import EventExpression

            self.nested_expression = self._define_list(
                nested_expression, EventExpression
            )
        self.operator = self._enum_matching(
            operator, EventGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
