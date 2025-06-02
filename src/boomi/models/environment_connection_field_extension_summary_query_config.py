
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .environment_connection_field_extension_summary_expression import (
    EnvironmentConnectionFieldExtensionSummaryExpression,
    EnvironmentConnectionFieldExtensionSummaryExpressionGuard,
)
from .environment_connection_field_extension_summary_simple_expression import (
    EnvironmentConnectionFieldExtensionSummarySimpleExpression,
)
from .environment_connection_field_extension_summary_grouping_expression import (
    EnvironmentConnectionFieldExtensionSummaryGroupingExpression,
)


@JsonMap({})
class EnvironmentConnectionFieldExtensionSummaryQueryConfigQueryFilter(BaseModel):
    """EnvironmentConnectionFieldExtensionSummaryQueryConfigQueryFilter

    :param expression: expression
    :type expression: EnvironmentConnectionFieldExtensionSummaryExpression
    """

    def __init__(
        self, expression: EnvironmentConnectionFieldExtensionSummaryExpression, **kwargs
    ):
        """EnvironmentConnectionFieldExtensionSummaryQueryConfigQueryFilter

        :param expression: expression
        :type expression: EnvironmentConnectionFieldExtensionSummaryExpression
        """
        self.expression = (
            EnvironmentConnectionFieldExtensionSummaryExpressionGuard.return_one_of(
                expression
            )
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EnvironmentConnectionFieldExtensionSummaryQueryConfig(BaseModel):
    """EnvironmentConnectionFieldExtensionSummaryQueryConfig

    :param query_filter: query_filter
    :type query_filter: EnvironmentConnectionFieldExtensionSummaryQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: EnvironmentConnectionFieldExtensionSummaryQueryConfigQueryFilter,
        **kwargs,
    ):
        """EnvironmentConnectionFieldExtensionSummaryQueryConfig

        :param query_filter: query_filter
        :type query_filter: EnvironmentConnectionFieldExtensionSummaryQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter,
            EnvironmentConnectionFieldExtensionSummaryQueryConfigQueryFilter,
        )
        self._kwargs = kwargs
