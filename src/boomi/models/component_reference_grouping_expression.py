
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .component_reference_expression import ComponentReferenceExpression, ComponentReferenceExpressionGuard
from .component_reference_simple_expression import ComponentReferenceSimpleExpression

class ComponentReferenceGroupingExpressionOperator(Enum):
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
                ComponentReferenceGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ComponentReferenceGroupingExpression(BaseModel):
    """ComponentReferenceGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ComponentReferenceExpression], optional
    :param operator: operator
    :type operator: ComponentReferenceGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ComponentReferenceGroupingExpressionOperator,
        nested_expression: List[ComponentReferenceExpression] = SENTINEL,
        **kwargs,
    ):
        """ComponentReferenceGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ComponentReferenceExpression], optional
        :param operator: operator
        :type operator: ComponentReferenceGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ComponentReferenceExpression
            )
        self.operator = self._enum_matching(
            operator, ComponentReferenceGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
