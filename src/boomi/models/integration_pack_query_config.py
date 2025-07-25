
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .integration_pack_expression import (
    IntegrationPackExpression,
    IntegrationPackExpressionGuard,
)
from .integration_pack_simple_expression import IntegrationPackSimpleExpression
from .integration_pack_grouping_expression import IntegrationPackGroupingExpression


@JsonMap({})
class IntegrationPackQueryConfigQueryFilter(BaseModel):
    """IntegrationPackQueryConfigQueryFilter

    :param expression: expression
    :type expression: IntegrationPackExpression
    """

    def __init__(self, expression: IntegrationPackExpression, **kwargs):
        """IntegrationPackQueryConfigQueryFilter

        :param expression: expression
        :type expression: IntegrationPackExpression
        """
        self.expression = IntegrationPackExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class IntegrationPackQueryConfig(BaseModel):
    """IntegrationPackQueryConfig

    :param query_filter: query_filter
    :type query_filter: IntegrationPackQueryConfigQueryFilter
    """

    def __init__(self, query_filter: IntegrationPackQueryConfigQueryFilter, **kwargs):
        """IntegrationPackQueryConfig

        :param query_filter: query_filter
        :type query_filter: IntegrationPackQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, IntegrationPackQueryConfigQueryFilter
        )
        self._kwargs = kwargs
