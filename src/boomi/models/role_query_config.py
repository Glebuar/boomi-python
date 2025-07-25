
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .role_expression import RoleExpression, RoleExpressionGuard
from .role_simple_expression import RoleSimpleExpression
from .role_grouping_expression import RoleGroupingExpression


@JsonMap({})
class RoleQueryConfigQueryFilter(BaseModel):
    """RoleQueryConfigQueryFilter

    :param expression: expression
    :type expression: RoleExpression
    """

    def __init__(self, expression: RoleExpression, **kwargs):
        """RoleQueryConfigQueryFilter

        :param expression: expression
        :type expression: RoleExpression
        """
        self.expression = RoleExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class RoleQueryConfig(BaseModel):
    """RoleQueryConfig

    :param query_filter: query_filter
    :type query_filter: RoleQueryConfigQueryFilter
    """

    def __init__(self, query_filter: RoleQueryConfigQueryFilter, **kwargs):
        """RoleQueryConfig

        :param query_filter: query_filter
        :type query_filter: RoleQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, RoleQueryConfigQueryFilter
        )
        self._kwargs = kwargs
