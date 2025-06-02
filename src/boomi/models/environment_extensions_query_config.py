
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .environment_extensions_expression import (
    EnvironmentExtensionsExpression,
    EnvironmentExtensionsExpressionGuard,
)
from .environment_extensions_simple_expression import (
    EnvironmentExtensionsSimpleExpression,
)
from .environment_extensions_grouping_expression import (
    EnvironmentExtensionsGroupingExpression,
)


@JsonMap({})
class EnvironmentExtensionsQueryConfigQueryFilter(BaseModel):
    """EnvironmentExtensionsQueryConfigQueryFilter

    :param expression: expression
    :type expression: EnvironmentExtensionsExpression
    """

    def __init__(self, expression: EnvironmentExtensionsExpression, **kwargs):
        """EnvironmentExtensionsQueryConfigQueryFilter

        :param expression: expression
        :type expression: EnvironmentExtensionsExpression
        """
        self.expression = EnvironmentExtensionsExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EnvironmentExtensionsQueryConfig(BaseModel):
    """EnvironmentExtensionsQueryConfig

    :param query_filter: query_filter
    :type query_filter: EnvironmentExtensionsQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: EnvironmentExtensionsQueryConfigQueryFilter, **kwargs
    ):
        """EnvironmentExtensionsQueryConfig

        :param query_filter: query_filter
        :type query_filter: EnvironmentExtensionsQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, EnvironmentExtensionsQueryConfigQueryFilter
        )
        self._kwargs = kwargs
