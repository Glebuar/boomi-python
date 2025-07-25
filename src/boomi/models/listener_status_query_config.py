
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .listener_status_expression import (
    ListenerStatusExpression,
    ListenerStatusExpressionGuard,
)
from .listener_status_simple_expression import ListenerStatusSimpleExpression
from .listener_status_grouping_expression import ListenerStatusGroupingExpression


@JsonMap({})
class ListenerStatusQueryConfigQueryFilter(BaseModel):
    """ListenerStatusQueryConfigQueryFilter

    :param expression: expression
    :type expression: ListenerStatusExpression
    """

    def __init__(self, expression: ListenerStatusExpression, **kwargs):
        """ListenerStatusQueryConfigQueryFilter

        :param expression: expression
        :type expression: ListenerStatusExpression
        """
        self.expression = ListenerStatusExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ListenerStatusQueryConfig(BaseModel):
    """ListenerStatusQueryConfig

    :param query_filter: query_filter
    :type query_filter: ListenerStatusQueryConfigQueryFilter
    """

    def __init__(self, query_filter: ListenerStatusQueryConfigQueryFilter, **kwargs):
        """ListenerStatusQueryConfig

        :param query_filter: query_filter
        :type query_filter: ListenerStatusQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ListenerStatusQueryConfigQueryFilter
        )
        self._kwargs = kwargs
