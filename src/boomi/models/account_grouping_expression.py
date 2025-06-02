
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    
    from .account_expression import AccountExpression, AccountExpressionGuard

class AccountGroupingExpressionOperator(Enum):
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
                AccountGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AccountGroupingExpression(BaseModel):
    """AccountGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["AccountExpression"], optional
    :param operator: operator
    :type operator: AccountGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AccountGroupingExpressionOperator,
        nested_expression: List["AccountExpression"] = SENTINEL,
        **kwargs,
    ):
        """AccountGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["AccountExpression"], optional
        :param operator: operator
        :type operator: AccountGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .account_expression import AccountExpression

            self.nested_expression = self._define_list(
                nested_expression, AccountExpression
            )
        self.operator = self._enum_matching(
            operator, AccountGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
