
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account_group_account_expression import (
    AccountGroupAccountExpression,
    AccountGroupAccountExpressionGuard,
)
from .account_group_account_simple_expression import AccountGroupAccountSimpleExpression
from .account_group_account_grouping_expression import (
    AccountGroupAccountGroupingExpression,
)


@JsonMap({})
class AccountGroupAccountQueryConfigQueryFilter(BaseModel):
    """AccountGroupAccountQueryConfigQueryFilter

    :param expression: expression
    :type expression: AccountGroupAccountExpression
    """

    def __init__(self, expression: AccountGroupAccountExpression, **kwargs):
        """AccountGroupAccountQueryConfigQueryFilter

        :param expression: expression
        :type expression: AccountGroupAccountExpression
        """
        self.expression = AccountGroupAccountExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AccountGroupAccountQueryConfig(BaseModel):
    """AccountGroupAccountQueryConfig

    :param query_filter: query_filter
    :type query_filter: AccountGroupAccountQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: AccountGroupAccountQueryConfigQueryFilter, **kwargs
    ):
        """AccountGroupAccountQueryConfig

        :param query_filter: query_filter
        :type query_filter: AccountGroupAccountQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AccountGroupAccountQueryConfigQueryFilter
        )
        self._kwargs = kwargs
