
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .api_usage_count_expression import (
    ApiUsageCountExpression,
    ApiUsageCountExpressionGuard,
)
from .api_usage_count_simple_expression import ApiUsageCountSimpleExpression
from .api_usage_count_grouping_expression import ApiUsageCountGroupingExpression


@JsonMap({})
class ApiUsageCountQueryConfigQueryFilter(BaseModel):
    """ApiUsageCountQueryConfigQueryFilter

    :param expression: expression
    :type expression: ApiUsageCountExpression
    """

    def __init__(self, expression: ApiUsageCountExpression, **kwargs):
        """ApiUsageCountQueryConfigQueryFilter

        :param expression: expression
        :type expression: ApiUsageCountExpression
        """
        self.expression = ApiUsageCountExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ApiUsageCountQueryConfig(BaseModel):
    """ApiUsageCountQueryConfig

    :param query_filter: query_filter
    :type query_filter: ApiUsageCountQueryConfigQueryFilter
    """

    def __init__(self, query_filter: ApiUsageCountQueryConfigQueryFilter, **kwargs):
        """ApiUsageCountQueryConfig

        :param query_filter: query_filter
        :type query_filter: ApiUsageCountQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ApiUsageCountQueryConfigQueryFilter
        )
        self._kwargs = kwargs
