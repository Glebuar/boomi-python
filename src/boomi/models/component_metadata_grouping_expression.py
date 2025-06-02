
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .component_metadata_expression import ComponentMetadataExpression, ComponentMetadataExpressionGuard
from .component_metadata_simple_expression import ComponentMetadataSimpleExpression

class ComponentMetadataGroupingExpressionOperator(Enum):
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
                ComponentMetadataGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ComponentMetadataGroupingExpression(BaseModel):
    """ComponentMetadataGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ComponentMetadataExpression], optional
    :param operator: operator
    :type operator: ComponentMetadataGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ComponentMetadataGroupingExpressionOperator,
        nested_expression: List[ComponentMetadataExpression] = SENTINEL,
        **kwargs,
    ):
        """ComponentMetadataGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ComponentMetadataExpression], optional
        :param operator: operator
        :type operator: ComponentMetadataGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ComponentMetadataExpression
            )
        self.operator = self._enum_matching(
            operator, ComponentMetadataGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
