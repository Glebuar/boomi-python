
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account_expression import AccountExpression, AccountExpressionGuard
from .account_simple_expression import AccountSimpleExpression
from .account_grouping_expression import AccountGroupingExpression


@JsonMap({})
class AccountQueryConfigQueryFilter(BaseModel):
    """AccountQueryConfigQueryFilter

    :param expression: expression
    :type expression: AccountExpression
    """

    def __init__(self, expression: AccountExpression, **kwargs):
        """AccountQueryConfigQueryFilter

        :param expression: expression
        :type expression: AccountExpression
        """
        self.expression = AccountExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AccountQueryConfig(BaseModel):
    """AccountQueryConfig

    :param query_filter: query_filter
    :type query_filter: AccountQueryConfigQueryFilter
    """

    def __init__(self, query_filter: AccountQueryConfigQueryFilter, **kwargs):
        """AccountQueryConfig

        :param query_filter: query_filter
        :type query_filter: AccountQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AccountQueryConfigQueryFilter
        )
        self._kwargs = kwargs
