
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .environment_expression import EnvironmentExpression, EnvironmentExpressionGuard
from .environment_simple_expression import EnvironmentSimpleExpression
from .environment_grouping_expression import EnvironmentGroupingExpression


@JsonMap({})
class EnvironmentQueryConfigQueryFilter(BaseModel):
    """EnvironmentQueryConfigQueryFilter

    :param expression: expression
    :type expression: EnvironmentExpression
    """

    def __init__(self, expression: EnvironmentExpression, **kwargs):
        """EnvironmentQueryConfigQueryFilter

        :param expression: expression
        :type expression: EnvironmentExpression
        """
        self.expression = EnvironmentExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EnvironmentQueryConfig(BaseModel):
    """EnvironmentQueryConfig

    :param query_filter: query_filter
    :type query_filter: EnvironmentQueryConfigQueryFilter
    """

    def __init__(self, query_filter: EnvironmentQueryConfigQueryFilter, **kwargs):
        """EnvironmentQueryConfig

        :param query_filter: query_filter
        :type query_filter: EnvironmentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, EnvironmentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
