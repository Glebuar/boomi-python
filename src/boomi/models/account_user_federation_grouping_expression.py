
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .account_user_federation_expression import AccountUserFederationExpression, AccountUserFederationExpressionGuard
from .account_user_federation_simple_expression import (
    AccountUserFederationSimpleExpression,
)

class AccountUserFederationGroupingExpressionOperator(Enum):
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
                AccountUserFederationGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AccountUserFederationGroupingExpression(BaseModel):
    """AccountUserFederationGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[AccountUserFederationExpression], optional
    :param operator: operator
    :type operator: AccountUserFederationGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AccountUserFederationGroupingExpressionOperator,
        nested_expression: List[AccountUserFederationExpression] = SENTINEL,
        **kwargs,
    ):
        """AccountUserFederationGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[AccountUserFederationExpression], optional
        :param operator: operator
        :type operator: AccountUserFederationGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, AccountUserFederationExpression
            )
        self.operator = self._enum_matching(
            operator, AccountUserFederationGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
