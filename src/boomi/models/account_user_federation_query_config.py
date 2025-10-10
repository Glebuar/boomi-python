
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account_user_federation_expression import (
    AccountUserFederationExpression,
    AccountUserFederationExpressionGuard,
)
from .account_user_federation_simple_expression import (
    AccountUserFederationSimpleExpression,
)
from .account_user_federation_grouping_expression import (
    AccountUserFederationGroupingExpression,
)


@JsonMap({})
class AccountUserFederationQueryConfigQueryFilter(BaseModel):
    """AccountUserFederationQueryConfigQueryFilter

    :param expression: expression
    :type expression: AccountUserFederationExpression
    """

    def __init__(self, expression: AccountUserFederationExpression, **kwargs):
        """AccountUserFederationQueryConfigQueryFilter

        :param expression: expression
        :type expression: AccountUserFederationExpression
        """
        self.expression = AccountUserFederationExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AccountUserFederationQueryConfig(BaseModel):
    """AccountUserFederationQueryConfig

    :param query_filter: query_filter
    :type query_filter: AccountUserFederationQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: AccountUserFederationQueryConfigQueryFilter, **kwargs
    ):
        """AccountUserFederationQueryConfig

        :param query_filter: query_filter
        :type query_filter: AccountUserFederationQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AccountUserFederationQueryConfigQueryFilter
        )
        self._kwargs = kwargs
