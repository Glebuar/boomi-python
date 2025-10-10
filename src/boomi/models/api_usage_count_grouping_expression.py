
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .api_usage_count_expression import ApiUsageCountExpression, ApiUsageCountExpressionGuard
from .api_usage_count_simple_expression import ApiUsageCountSimpleExpression

class ApiUsageCountGroupingExpressionOperator(Enum):
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
                ApiUsageCountGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ApiUsageCountGroupingExpression(BaseModel):
    """ApiUsageCountGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ApiUsageCountExpression], optional
    :param operator: operator
    :type operator: ApiUsageCountGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ApiUsageCountGroupingExpressionOperator,
        nested_expression: List[ApiUsageCountExpression] = SENTINEL,
        **kwargs,
    ):
        """ApiUsageCountGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ApiUsageCountExpression], optional
        :param operator: operator
        :type operator: ApiUsageCountGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ApiUsageCountExpression
            )
        self.operator = self._enum_matching(
            operator, ApiUsageCountGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
