
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .account_group_expression import AccountGroupExpression, AccountGroupExpressionGuard
from .account_group_simple_expression import AccountGroupSimpleExpression

class AccountGroupGroupingExpressionOperator(Enum):
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
                AccountGroupGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AccountGroupGroupingExpression(BaseModel):
    """AccountGroupGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[AccountGroupExpression], optional
    :param operator: operator
    :type operator: AccountGroupGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AccountGroupGroupingExpressionOperator,
        nested_expression: List[AccountGroupExpression] = SENTINEL,
        **kwargs,
    ):
        """AccountGroupGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[AccountGroupExpression], optional
        :param operator: operator
        :type operator: AccountGroupGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, AccountGroupExpression
            )
        self.operator = self._enum_matching(
            operator, AccountGroupGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
