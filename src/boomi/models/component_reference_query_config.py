
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .component_reference_expression import (
    ComponentReferenceExpression,
    ComponentReferenceExpressionGuard,
)
from .component_reference_simple_expression import ComponentReferenceSimpleExpression
from .component_reference_grouping_expression import (
    ComponentReferenceGroupingExpression,
)


@JsonMap({})
class ComponentReferenceQueryConfigQueryFilter(BaseModel):
    """ComponentReferenceQueryConfigQueryFilter

    :param expression: expression
    :type expression: ComponentReferenceExpression
    """

    def __init__(self, expression: ComponentReferenceExpression, **kwargs):
        """ComponentReferenceQueryConfigQueryFilter

        :param expression: expression
        :type expression: ComponentReferenceExpression
        """
        self.expression = ComponentReferenceExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ComponentReferenceQueryConfig(BaseModel):
    """ComponentReferenceQueryConfig

    :param query_filter: query_filter
    :type query_filter: ComponentReferenceQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ComponentReferenceQueryConfigQueryFilter, **kwargs
    ):
        """ComponentReferenceQueryConfig

        :param query_filter: query_filter
        :type query_filter: ComponentReferenceQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ComponentReferenceQueryConfigQueryFilter
        )
        self._kwargs = kwargs
