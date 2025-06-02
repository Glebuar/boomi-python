
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .environment_connection_field_extension_summary_expression import EnvironmentConnectionFieldExtensionSummaryExpression, EnvironmentConnectionFieldExtensionSummaryExpressionGuard
from .environment_connection_field_extension_summary_simple_expression import (
    EnvironmentConnectionFieldExtensionSummarySimpleExpression,
)

class EnvironmentConnectionFieldExtensionSummaryGroupingExpressionOperator(Enum):
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
                EnvironmentConnectionFieldExtensionSummaryGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EnvironmentConnectionFieldExtensionSummaryGroupingExpression(BaseModel):
    """EnvironmentConnectionFieldExtensionSummaryGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[EnvironmentConnectionFieldExtensionSummaryExpression], optional
    :param operator: operator
    :type operator: EnvironmentConnectionFieldExtensionSummaryGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EnvironmentConnectionFieldExtensionSummaryGroupingExpressionOperator,
        nested_expression: List[
            EnvironmentConnectionFieldExtensionSummaryExpression
        ] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentConnectionFieldExtensionSummaryGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[EnvironmentConnectionFieldExtensionSummaryExpression], optional
        :param operator: operator
        :type operator: EnvironmentConnectionFieldExtensionSummaryGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, EnvironmentConnectionFieldExtensionSummaryExpression
            )
        self.operator = self._enum_matching(
            operator,
            EnvironmentConnectionFieldExtensionSummaryGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
