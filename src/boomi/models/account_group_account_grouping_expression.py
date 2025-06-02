
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .account_group_account_expression import AccountGroupAccountExpression, AccountGroupAccountExpressionGuard
from .account_group_account_simple_expression import AccountGroupAccountSimpleExpression

class AccountGroupAccountGroupingExpressionOperator(Enum):
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
                AccountGroupAccountGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AccountGroupAccountGroupingExpression(BaseModel):
    """AccountGroupAccountGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[AccountGroupAccountExpression], optional
    :param operator: operator
    :type operator: AccountGroupAccountGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AccountGroupAccountGroupingExpressionOperator,
        nested_expression: List[AccountGroupAccountExpression] = SENTINEL,
        **kwargs,
    ):
        """AccountGroupAccountGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[AccountGroupAccountExpression], optional
        :param operator: operator
        :type operator: AccountGroupAccountGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, AccountGroupAccountExpression
            )
        self.operator = self._enum_matching(
            operator, AccountGroupAccountGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
