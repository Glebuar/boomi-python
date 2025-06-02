
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .organization_component_expression import (
    OrganizationComponentExpression,
    OrganizationComponentExpressionGuard,
)
from .organization_component_simple_expression import (
    OrganizationComponentSimpleExpression,
)
from .organization_component_grouping_expression import (
    OrganizationComponentGroupingExpression,
)


@JsonMap({})
class OrganizationComponentQueryConfigQueryFilter(BaseModel):
    """OrganizationComponentQueryConfigQueryFilter

    :param expression: expression
    :type expression: OrganizationComponentExpression
    """

    def __init__(self, expression: OrganizationComponentExpression, **kwargs):
        """OrganizationComponentQueryConfigQueryFilter

        :param expression: expression
        :type expression: OrganizationComponentExpression
        """
        self.expression = OrganizationComponentExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class OrganizationComponentQueryConfig(BaseModel):
    """OrganizationComponentQueryConfig

    :param query_filter: query_filter
    :type query_filter: OrganizationComponentQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: OrganizationComponentQueryConfigQueryFilter, **kwargs
    ):
        """OrganizationComponentQueryConfig

        :param query_filter: query_filter
        :type query_filter: OrganizationComponentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, OrganizationComponentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
