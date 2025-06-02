
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .throughput_account_group_expression import (
    ThroughputAccountGroupExpression,
    ThroughputAccountGroupExpressionGuard,
)
from .throughput_account_group_simple_expression import (
    ThroughputAccountGroupSimpleExpression,
)
from .throughput_account_group_grouping_expression import (
    ThroughputAccountGroupGroupingExpression,
)


@JsonMap({})
class ThroughputAccountGroupQueryConfigQueryFilter(BaseModel):
    """ThroughputAccountGroupQueryConfigQueryFilter

    :param expression: expression
    :type expression: ThroughputAccountGroupExpression
    """

    def __init__(self, expression: ThroughputAccountGroupExpression, **kwargs):
        """ThroughputAccountGroupQueryConfigQueryFilter

        :param expression: expression
        :type expression: ThroughputAccountGroupExpression
        """
        self.expression = ThroughputAccountGroupExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ThroughputAccountGroupQueryConfig(BaseModel):
    """ThroughputAccountGroupQueryConfig

    :param query_filter: query_filter
    :type query_filter: ThroughputAccountGroupQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ThroughputAccountGroupQueryConfigQueryFilter, **kwargs
    ):
        """ThroughputAccountGroupQueryConfig

        :param query_filter: query_filter
        :type query_filter: ThroughputAccountGroupQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ThroughputAccountGroupQueryConfigQueryFilter
        )
        self._kwargs = kwargs
