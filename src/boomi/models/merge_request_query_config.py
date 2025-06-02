
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .merge_request_expression import (
    MergeRequestExpression,
    MergeRequestExpressionGuard,
)
from .merge_request_simple_expression import MergeRequestSimpleExpression
from .merge_request_grouping_expression import MergeRequestGroupingExpression


@JsonMap({})
class MergeRequestQueryConfigQueryFilter(BaseModel):
    """MergeRequestQueryConfigQueryFilter

    :param expression: expression
    :type expression: MergeRequestExpression
    """

    def __init__(self, expression: MergeRequestExpression, **kwargs):
        """MergeRequestQueryConfigQueryFilter

        :param expression: expression
        :type expression: MergeRequestExpression
        """
        self.expression = MergeRequestExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class MergeRequestQueryConfig(BaseModel):
    """MergeRequestQueryConfig

    :param query_filter: query_filter
    :type query_filter: MergeRequestQueryConfigQueryFilter
    """

    def __init__(self, query_filter: MergeRequestQueryConfigQueryFilter, **kwargs):
        """MergeRequestQueryConfig

        :param query_filter: query_filter
        :type query_filter: MergeRequestQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, MergeRequestQueryConfigQueryFilter
        )
        self._kwargs = kwargs
