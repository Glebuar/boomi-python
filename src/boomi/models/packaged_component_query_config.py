
from __future__ import annotations
from typing import Optional
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

    :param query_filter: query_filter (optional)
    :type query_filter: Optional[PackagedComponentQueryConfigQueryFilter]
    """

    def __init__(self, query_filter: Optional[PackagedComponentQueryConfigQueryFilter] = None, **kwargs):
        """PackagedComponentQueryConfig

        :param query_filter: query_filter (optional)
        :type query_filter: Optional[PackagedComponentQueryConfigQueryFilter]
        """
        self.query_filter = self._define_object(
            query_filter, PackagedComponentQueryConfigQueryFilter
        ) if query_filter is not None else None
        self._kwargs = kwargs
