
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .organization_component_expression import OrganizationComponentExpression, OrganizationComponentExpressionGuard
from .organization_component_simple_expression import (
    OrganizationComponentSimpleExpression,
)

class OrganizationComponentGroupingExpressionOperator(Enum):
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
                OrganizationComponentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class OrganizationComponentGroupingExpression(BaseModel):
    """OrganizationComponentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[OrganizationComponentExpression], optional
    :param operator: operator
    :type operator: OrganizationComponentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: OrganizationComponentGroupingExpressionOperator,
        nested_expression: List[OrganizationComponentExpression] = SENTINEL,
        **kwargs,
    ):
        """OrganizationComponentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[OrganizationComponentExpression], optional
        :param operator: operator
        :type operator: OrganizationComponentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, OrganizationComponentExpression
            )
        self.operator = self._enum_matching(
            operator, OrganizationComponentGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
