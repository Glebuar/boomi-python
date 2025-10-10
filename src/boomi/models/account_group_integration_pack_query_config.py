
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account_group_integration_pack_expression import (
    AccountGroupIntegrationPackExpression,
)


@JsonMap({})
class AccountGroupIntegrationPackQueryConfigQueryFilter(BaseModel):
    """AccountGroupIntegrationPackQueryConfigQueryFilter

    :param expression: expression
    :type expression: AccountGroupIntegrationPackExpression
    """

    def __init__(self, expression: AccountGroupIntegrationPackExpression, **kwargs):
        """AccountGroupIntegrationPackQueryConfigQueryFilter

        :param expression: expression
        :type expression: AccountGroupIntegrationPackExpression
        """
        self.expression = self._define_object(
            expression, AccountGroupIntegrationPackExpression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AccountGroupIntegrationPackQueryConfig(BaseModel):
    """AccountGroupIntegrationPackQueryConfig

    :param query_filter: query_filter
    :type query_filter: AccountGroupIntegrationPackQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: AccountGroupIntegrationPackQueryConfigQueryFilter, **kwargs
    ):
        """AccountGroupIntegrationPackQueryConfig

        :param query_filter: query_filter
        :type query_filter: AccountGroupIntegrationPackQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AccountGroupIntegrationPackQueryConfigQueryFilter
        )
        self._kwargs = kwargs
