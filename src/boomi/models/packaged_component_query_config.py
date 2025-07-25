
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .packaged_component_expression import (
    PackagedComponentExpression,
    PackagedComponentExpressionGuard,
)
from .packaged_component_simple_expression import PackagedComponentSimpleExpression
from .packaged_component_grouping_expression import PackagedComponentGroupingExpression


@JsonMap({})
class PackagedComponentQueryConfigQueryFilter(BaseModel):
    """PackagedComponentQueryConfigQueryFilter

    :param expression: expression
    :type expression: PackagedComponentExpression
    """

    def __init__(self, expression: PackagedComponentExpression, **kwargs):
        """PackagedComponentQueryConfigQueryFilter

        :param expression: expression
        :type expression: PackagedComponentExpression
        """
        self.expression = PackagedComponentExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class PackagedComponentQueryConfig(BaseModel):
    """PackagedComponentQueryConfig

    :param query_filter: query_filter
    :type query_filter: PackagedComponentQueryConfigQueryFilter
    """

    def __init__(self, query_filter: PackagedComponentQueryConfigQueryFilter, **kwargs):
        """PackagedComponentQueryConfig

        :param query_filter: query_filter
        :type query_filter: PackagedComponentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, PackagedComponentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
