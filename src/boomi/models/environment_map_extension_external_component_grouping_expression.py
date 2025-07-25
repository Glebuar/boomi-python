
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .environment_map_extension_external_component_expression import EnvironmentMapExtensionExternalComponentExpression, EnvironmentMapExtensionExternalComponentExpressionGuard
from .environment_map_extension_external_component_simple_expression import (
    EnvironmentMapExtensionExternalComponentSimpleExpression,
)

class EnvironmentMapExtensionExternalComponentGroupingExpressionOperator(Enum):
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
                EnvironmentMapExtensionExternalComponentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EnvironmentMapExtensionExternalComponentGroupingExpression(BaseModel):
    """EnvironmentMapExtensionExternalComponentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[EnvironmentMapExtensionExternalComponentExpression], optional
    :param operator: operator
    :type operator: EnvironmentMapExtensionExternalComponentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EnvironmentMapExtensionExternalComponentGroupingExpressionOperator,
        nested_expression: List[
            EnvironmentMapExtensionExternalComponentExpression
        ] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtensionExternalComponentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[EnvironmentMapExtensionExternalComponentExpression], optional
        :param operator: operator
        :type operator: EnvironmentMapExtensionExternalComponentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, EnvironmentMapExtensionExternalComponentExpression
            )
        self.operator = self._enum_matching(
            operator,
            EnvironmentMapExtensionExternalComponentGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
