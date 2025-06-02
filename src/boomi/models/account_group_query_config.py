
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account_group_expression import (
    AccountGroupExpression,
    AccountGroupExpressionGuard,
)
from .account_group_simple_expression import AccountGroupSimpleExpression
from .account_group_grouping_expression import AccountGroupGroupingExpression


@JsonMap({})
class AccountGroupQueryConfigQueryFilter(BaseModel):
    """AccountGroupQueryConfigQueryFilter

    :param expression: expression
    :type expression: AccountGroupExpression
    """

    def __init__(self, expression: AccountGroupExpression, **kwargs):
        """AccountGroupQueryConfigQueryFilter

        :param expression: expression
        :type expression: AccountGroupExpression
        """
        self.expression = AccountGroupExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AccountGroupQueryConfig(BaseModel):
    """AccountGroupQueryConfig

    :param query_filter: query_filter
    :type query_filter: AccountGroupQueryConfigQueryFilter
    """

    def __init__(self, query_filter: AccountGroupQueryConfigQueryFilter, **kwargs):
        """AccountGroupQueryConfig

        :param query_filter: query_filter
        :type query_filter: AccountGroupQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AccountGroupQueryConfigQueryFilter
        )
        self._kwargs = kwargs
