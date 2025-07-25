
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account_group_user_role_expression import (
    AccountGroupUserRoleExpression,
    AccountGroupUserRoleExpressionGuard,
)
from .account_group_user_role_simple_expression import (
    AccountGroupUserRoleSimpleExpression,
)
from .account_group_user_role_grouping_expression import (
    AccountGroupUserRoleGroupingExpression,
)


@JsonMap({})
class AccountGroupUserRoleQueryConfigQueryFilter(BaseModel):
    """AccountGroupUserRoleQueryConfigQueryFilter

    :param expression: expression
    :type expression: AccountGroupUserRoleExpression
    """

    def __init__(self, expression: AccountGroupUserRoleExpression, **kwargs):
        """AccountGroupUserRoleQueryConfigQueryFilter

        :param expression: expression
        :type expression: AccountGroupUserRoleExpression
        """
        self.expression = AccountGroupUserRoleExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AccountGroupUserRoleQueryConfig(BaseModel):
    """AccountGroupUserRoleQueryConfig

    :param query_filter: query_filter
    :type query_filter: AccountGroupUserRoleQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: AccountGroupUserRoleQueryConfigQueryFilter, **kwargs
    ):
        """AccountGroupUserRoleQueryConfig

        :param query_filter: query_filter
        :type query_filter: AccountGroupUserRoleQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AccountGroupUserRoleQueryConfigQueryFilter
        )
        self._kwargs = kwargs
