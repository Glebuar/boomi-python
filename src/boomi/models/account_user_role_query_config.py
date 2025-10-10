
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account_user_role_expression import (
    AccountUserRoleExpression,
    AccountUserRoleExpressionGuard,
)
from .account_user_role_simple_expression import AccountUserRoleSimpleExpression
from .account_user_role_grouping_expression import AccountUserRoleGroupingExpression


@JsonMap({})
class AccountUserRoleQueryConfigQueryFilter(BaseModel):
    """AccountUserRoleQueryConfigQueryFilter

    :param expression: expression
    :type expression: AccountUserRoleExpression
    """

    def __init__(self, expression: AccountUserRoleExpression, **kwargs):
        """AccountUserRoleQueryConfigQueryFilter

        :param expression: expression
        :type expression: AccountUserRoleExpression
        """
        self.expression = AccountUserRoleExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AccountUserRoleQueryConfig(BaseModel):
    """AccountUserRoleQueryConfig

    :param query_filter: query_filter
    :type query_filter: AccountUserRoleQueryConfigQueryFilter
    """

    def __init__(self, query_filter: AccountUserRoleQueryConfigQueryFilter, **kwargs):
        """AccountUserRoleQueryConfig

        :param query_filter: query_filter
        :type query_filter: AccountUserRoleQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AccountUserRoleQueryConfigQueryFilter
        )
        self._kwargs = kwargs
