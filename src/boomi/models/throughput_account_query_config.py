
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .throughput_account_expression import (
    ThroughputAccountExpression,
    ThroughputAccountExpressionGuard,
)
from .throughput_account_simple_expression import ThroughputAccountSimpleExpression
from .throughput_account_grouping_expression import ThroughputAccountGroupingExpression


@JsonMap({})
class ThroughputAccountQueryConfigQueryFilter(BaseModel):
    """ThroughputAccountQueryConfigQueryFilter

    :param expression: expression
    :type expression: ThroughputAccountExpression
    """

    def __init__(self, expression: ThroughputAccountExpression, **kwargs):
        """ThroughputAccountQueryConfigQueryFilter

        :param expression: expression
        :type expression: ThroughputAccountExpression
        """
        self.expression = ThroughputAccountExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ThroughputAccountQueryConfig(BaseModel):
    """ThroughputAccountQueryConfig

    :param query_filter: query_filter
    :type query_filter: ThroughputAccountQueryConfigQueryFilter
    """

    def __init__(self, query_filter: ThroughputAccountQueryConfigQueryFilter, **kwargs):
        """ThroughputAccountQueryConfig

        :param query_filter: query_filter
        :type query_filter: ThroughputAccountQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ThroughputAccountQueryConfigQueryFilter
        )
        self._kwargs = kwargs
