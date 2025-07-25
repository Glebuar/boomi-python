
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .environment_map_extension_user_defined_function_summary_expression import (
    EnvironmentMapExtensionUserDefinedFunctionSummaryExpression,
    EnvironmentMapExtensionUserDefinedFunctionSummaryExpressionGuard,
)
from .environment_map_extension_user_defined_function_summary_simple_expression import (
    EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpression,
)
from .environment_map_extension_user_defined_function_summary_grouping_expression import (
    EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression,
)


@JsonMap({})
class EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfigQueryFilter(
    BaseModel
):
    """EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfigQueryFilter

    :param expression: expression
    :type expression: EnvironmentMapExtensionUserDefinedFunctionSummaryExpression
    """

    def __init__(
        self,
        expression: EnvironmentMapExtensionUserDefinedFunctionSummaryExpression,
        **kwargs,
    ):
        """EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfigQueryFilter

        :param expression: expression
        :type expression: EnvironmentMapExtensionUserDefinedFunctionSummaryExpression
        """
        self.expression = EnvironmentMapExtensionUserDefinedFunctionSummaryExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig(BaseModel):
    """EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig

    :param query_filter: query_filter
    :type query_filter: EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfigQueryFilter,
        **kwargs,
    ):
        """EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfig

        :param query_filter: query_filter
        :type query_filter: EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter,
            EnvironmentMapExtensionUserDefinedFunctionSummaryQueryConfigQueryFilter,
        )
        self._kwargs = kwargs
