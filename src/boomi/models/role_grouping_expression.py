
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .role_expression import RoleExpression, RoleExpressionGuard
from .role_simple_expression import RoleSimpleExpression

class RoleGroupingExpressionOperator(Enum):
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
            map(lambda x: x.value, RoleGroupingExpressionOperator._member_map_.values())
        )

@JsonMap({"nested_expression": "nestedExpression"})
class RoleGroupingExpression(BaseModel):
    """RoleGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["RoleExpression"], optional
    :param operator: operator
    :type operator: RoleGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: RoleGroupingExpressionOperator,
        nested_expression: List["RoleExpression"] = SENTINEL,
        **kwargs,
    ):
        """RoleGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["RoleExpression"], optional
        :param operator: operator
        :type operator: RoleGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .role_expression import RoleExpression

            self.nested_expression = self._define_list(
                nested_expression, RoleExpression
            )
        self.operator = self._enum_matching(
            operator, RoleGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
