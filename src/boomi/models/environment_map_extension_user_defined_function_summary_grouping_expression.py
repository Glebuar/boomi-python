
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .environment_map_extension_user_defined_function_summary_expression import EnvironmentMapExtensionUserDefinedFunctionSummaryExpression, EnvironmentMapExtensionUserDefinedFunctionSummaryExpressionGuard
from .environment_map_extension_user_defined_function_summary_simple_expression import (
    EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpression,
)

class EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpressionOperator(Enum):
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
                EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression(BaseModel):
    """EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[EnvironmentMapExtensionUserDefinedFunctionSummaryExpression], optional
    :param operator: operator
    :type operator: EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpressionOperator,
        nested_expression: List[
            EnvironmentMapExtensionUserDefinedFunctionSummaryExpression
        ] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[EnvironmentMapExtensionUserDefinedFunctionSummaryExpression], optional
        :param operator: operator
        :type operator: EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression,
                EnvironmentMapExtensionUserDefinedFunctionSummaryExpression,
            )
        self.operator = self._enum_matching(
            operator,
            EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
