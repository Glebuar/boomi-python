
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .component_metadata_expression import (
    ComponentMetadataExpression,
    ComponentMetadataExpressionGuard,
)
from .component_metadata_simple_expression import ComponentMetadataSimpleExpression
from .component_metadata_grouping_expression import ComponentMetadataGroupingExpression


@JsonMap({})
class ComponentMetadataQueryConfigQueryFilter(BaseModel):
    """ComponentMetadataQueryConfigQueryFilter

    :param expression: expression
    :type expression: ComponentMetadataExpression
    """

    def __init__(self, expression: ComponentMetadataExpression, **kwargs):
        """ComponentMetadataQueryConfigQueryFilter

        :param expression: expression
        :type expression: ComponentMetadataExpression
        """
        self.expression = ComponentMetadataExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ComponentMetadataQueryConfig(BaseModel):
    """ComponentMetadataQueryConfig

    :param query_filter: query_filter
    :type query_filter: ComponentMetadataQueryConfigQueryFilter
    """

    def __init__(self, query_filter: ComponentMetadataQueryConfigQueryFilter, **kwargs):
        """ComponentMetadataQueryConfig

        :param query_filter: query_filter
        :type query_filter: ComponentMetadataQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ComponentMetadataQueryConfigQueryFilter
        )
        self._kwargs = kwargs
