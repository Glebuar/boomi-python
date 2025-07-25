
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .environment_map_extensions_summary_expression import EnvironmentMapExtensionsSummaryExpression, EnvironmentMapExtensionsSummaryExpressionGuard
from .environment_map_extensions_summary_simple_expression import (
    EnvironmentMapExtensionsSummarySimpleExpression,
)

class EnvironmentMapExtensionsSummaryGroupingExpressionOperator(Enum):
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
                EnvironmentMapExtensionsSummaryGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EnvironmentMapExtensionsSummaryGroupingExpression(BaseModel):
    """EnvironmentMapExtensionsSummaryGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[EnvironmentMapExtensionsSummaryExpression], optional
    :param operator: operator
    :type operator: EnvironmentMapExtensionsSummaryGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EnvironmentMapExtensionsSummaryGroupingExpressionOperator,
        nested_expression: List[EnvironmentMapExtensionsSummaryExpression] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtensionsSummaryGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[EnvironmentMapExtensionsSummaryExpression], optional
        :param operator: operator
        :type operator: EnvironmentMapExtensionsSummaryGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, EnvironmentMapExtensionsSummaryExpression
            )
        self.operator = self._enum_matching(
            operator,
            EnvironmentMapExtensionsSummaryGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
