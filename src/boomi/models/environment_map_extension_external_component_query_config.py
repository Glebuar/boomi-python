
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .environment_map_extension_external_component_expression import (
    EnvironmentMapExtensionExternalComponentExpression,
    EnvironmentMapExtensionExternalComponentExpressionGuard,
)
from .environment_map_extension_external_component_simple_expression import (
    EnvironmentMapExtensionExternalComponentSimpleExpression,
)
from .environment_map_extension_external_component_grouping_expression import (
    EnvironmentMapExtensionExternalComponentGroupingExpression,
)


@JsonMap({})
class EnvironmentMapExtensionExternalComponentQueryConfigQueryFilter(BaseModel):
    """EnvironmentMapExtensionExternalComponentQueryConfigQueryFilter

    :param expression: expression
    :type expression: EnvironmentMapExtensionExternalComponentExpression
    """

    def __init__(
        self, expression: EnvironmentMapExtensionExternalComponentExpression, **kwargs
    ):
        """EnvironmentMapExtensionExternalComponentQueryConfigQueryFilter

        :param expression: expression
        :type expression: EnvironmentMapExtensionExternalComponentExpression
        """
        self.expression = (
            EnvironmentMapExtensionExternalComponentExpressionGuard.return_one_of(
                expression
            )
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EnvironmentMapExtensionExternalComponentQueryConfig(BaseModel):
    """EnvironmentMapExtensionExternalComponentQueryConfig

    :param query_filter: query_filter
    :type query_filter: EnvironmentMapExtensionExternalComponentQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: EnvironmentMapExtensionExternalComponentQueryConfigQueryFilter,
        **kwargs,
    ):
        """EnvironmentMapExtensionExternalComponentQueryConfig

        :param query_filter: query_filter
        :type query_filter: EnvironmentMapExtensionExternalComponentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, EnvironmentMapExtensionExternalComponentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
