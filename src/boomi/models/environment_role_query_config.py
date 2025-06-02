
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .environment_role_expression import (
    EnvironmentRoleExpression,
    EnvironmentRoleExpressionGuard,
)
from .environment_role_simple_expression import EnvironmentRoleSimpleExpression
from .environment_role_grouping_expression import EnvironmentRoleGroupingExpression


@JsonMap({})
class EnvironmentRoleQueryConfigQueryFilter(BaseModel):
    """EnvironmentRoleQueryConfigQueryFilter

    :param expression: expression
    :type expression: EnvironmentRoleExpression
    """

    def __init__(self, expression: EnvironmentRoleExpression, **kwargs):
        """EnvironmentRoleQueryConfigQueryFilter

        :param expression: expression
        :type expression: EnvironmentRoleExpression
        """
        self.expression = EnvironmentRoleExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EnvironmentRoleQueryConfig(BaseModel):
    """EnvironmentRoleQueryConfig

    :param query_filter: query_filter
    :type query_filter: EnvironmentRoleQueryConfigQueryFilter
    """

    def __init__(self, query_filter: EnvironmentRoleQueryConfigQueryFilter, **kwargs):
        """EnvironmentRoleQueryConfig

        :param query_filter: query_filter
        :type query_filter: EnvironmentRoleQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, EnvironmentRoleQueryConfigQueryFilter
        )
        self._kwargs = kwargs
