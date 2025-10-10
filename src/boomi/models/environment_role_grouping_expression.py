
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .environment_role_expression import EnvironmentRoleExpression, EnvironmentRoleExpressionGuard
from .environment_role_simple_expression import EnvironmentRoleSimpleExpression

class EnvironmentRoleGroupingExpressionOperator(Enum):
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
                EnvironmentRoleGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EnvironmentRoleGroupingExpression(BaseModel):
    """EnvironmentRoleGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[EnvironmentRoleExpression], optional
    :param operator: operator
    :type operator: EnvironmentRoleGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EnvironmentRoleGroupingExpressionOperator,
        nested_expression: List[EnvironmentRoleExpression] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentRoleGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[EnvironmentRoleExpression], optional
        :param operator: operator
        :type operator: EnvironmentRoleGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, EnvironmentRoleExpression
            )
        self.operator = self._enum_matching(
            operator, EnvironmentRoleGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
