
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .account_group_user_role_expression import AccountGroupUserRoleExpression, AccountGroupUserRoleExpressionGuard
from .account_group_user_role_simple_expression import (
    AccountGroupUserRoleSimpleExpression,
)

class AccountGroupUserRoleGroupingExpressionOperator(Enum):
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
                AccountGroupUserRoleGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AccountGroupUserRoleGroupingExpression(BaseModel):
    """AccountGroupUserRoleGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[AccountGroupUserRoleExpression], optional
    :param operator: operator
    :type operator: AccountGroupUserRoleGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AccountGroupUserRoleGroupingExpressionOperator,
        nested_expression: List[AccountGroupUserRoleExpression] = SENTINEL,
        **kwargs,
    ):
        """AccountGroupUserRoleGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[AccountGroupUserRoleExpression], optional
        :param operator: operator
        :type operator: AccountGroupUserRoleGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, AccountGroupUserRoleExpression
            )
        self.operator = self._enum_matching(
            operator, AccountGroupUserRoleGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
