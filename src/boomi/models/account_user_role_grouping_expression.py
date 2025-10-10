
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .account_user_role_expression import AccountUserRoleExpression, AccountUserRoleExpressionGuard
from .account_user_role_simple_expression import AccountUserRoleSimpleExpression

class AccountUserRoleGroupingExpressionOperator(Enum):
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
                AccountUserRoleGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AccountUserRoleGroupingExpression(BaseModel):
    """AccountUserRoleGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[AccountUserRoleExpression], optional
    :param operator: operator
    :type operator: AccountUserRoleGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AccountUserRoleGroupingExpressionOperator,
        nested_expression: List[AccountUserRoleExpression] = SENTINEL,
        **kwargs,
    ):
        """AccountUserRoleGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[AccountUserRoleExpression], optional
        :param operator: operator
        :type operator: AccountUserRoleGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, AccountUserRoleExpression
            )
        self.operator = self._enum_matching(
            operator, AccountUserRoleGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
