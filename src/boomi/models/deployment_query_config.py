
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .deployment_expression import DeploymentExpression, DeploymentExpressionGuard
from .deployment_simple_expression import DeploymentSimpleExpression
from .deployment_grouping_expression import DeploymentGroupingExpression


@JsonMap({})
class DeploymentQueryConfigQueryFilter(BaseModel):
    """DeploymentQueryConfigQueryFilter

    :param expression: expression
    :type expression: DeploymentExpression
    """

    def __init__(self, expression: DeploymentExpression, **kwargs):
        """DeploymentQueryConfigQueryFilter

        :param expression: expression
        :type expression: DeploymentExpression
        """
        self.expression = DeploymentExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class DeploymentQueryConfig(BaseModel):
    """DeploymentQueryConfig

    :param query_filter: query_filter
    :type query_filter: DeploymentQueryConfigQueryFilter
    """

    def __init__(self, query_filter: DeploymentQueryConfigQueryFilter, **kwargs):
        """DeploymentQueryConfig

        :param query_filter: query_filter
        :type query_filter: DeploymentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, DeploymentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
