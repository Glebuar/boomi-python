
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .custom_tracked_field_expression import CustomTrackedFieldExpression, CustomTrackedFieldExpressionGuard
from .custom_tracked_field_simple_expression import CustomTrackedFieldSimpleExpression

class CustomTrackedFieldGroupingExpressionOperator(Enum):
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
                CustomTrackedFieldGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class CustomTrackedFieldGroupingExpression(BaseModel):
    """CustomTrackedFieldGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[CustomTrackedFieldExpression], optional
    :param operator: operator
    :type operator: CustomTrackedFieldGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: CustomTrackedFieldGroupingExpressionOperator,
        nested_expression: List[CustomTrackedFieldExpression] = SENTINEL,
        **kwargs,
    ):
        """CustomTrackedFieldGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[CustomTrackedFieldExpression], optional
        :param operator: operator
        :type operator: CustomTrackedFieldGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, CustomTrackedFieldExpression
            )
        self.operator = self._enum_matching(
            operator, CustomTrackedFieldGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
