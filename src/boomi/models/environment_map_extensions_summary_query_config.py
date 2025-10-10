
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .environment_map_extensions_summary_expression import (
    EnvironmentMapExtensionsSummaryExpression,
    EnvironmentMapExtensionsSummaryExpressionGuard,
)
from .environment_map_extensions_summary_simple_expression import (
    EnvironmentMapExtensionsSummarySimpleExpression,
)
from .environment_map_extensions_summary_grouping_expression import (
    EnvironmentMapExtensionsSummaryGroupingExpression,
)


@JsonMap({})
class EnvironmentMapExtensionsSummaryQueryConfigQueryFilter(BaseModel):
    """EnvironmentMapExtensionsSummaryQueryConfigQueryFilter

    :param expression: expression
    :type expression: EnvironmentMapExtensionsSummaryExpression
    """

    def __init__(self, expression: EnvironmentMapExtensionsSummaryExpression, **kwargs):
        """EnvironmentMapExtensionsSummaryQueryConfigQueryFilter

        :param expression: expression
        :type expression: EnvironmentMapExtensionsSummaryExpression
        """
        self.expression = EnvironmentMapExtensionsSummaryExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EnvironmentMapExtensionsSummaryQueryConfig(BaseModel):
    """EnvironmentMapExtensionsSummaryQueryConfig

    :param query_filter: query_filter
    :type query_filter: EnvironmentMapExtensionsSummaryQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: EnvironmentMapExtensionsSummaryQueryConfigQueryFilter,
        **kwargs,
    ):
        """EnvironmentMapExtensionsSummaryQueryConfig

        :param query_filter: query_filter
        :type query_filter: EnvironmentMapExtensionsSummaryQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, EnvironmentMapExtensionsSummaryQueryConfigQueryFilter
        )
        self._kwargs = kwargs
