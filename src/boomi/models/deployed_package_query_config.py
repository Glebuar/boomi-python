
from __future__ import annotations
from typing import Optional
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .deployed_package_expression import (
    DeployedPackageExpression,
    DeployedPackageExpressionGuard,
)
from .deployed_package_simple_expression import DeployedPackageSimpleExpression
from .deployed_package_grouping_expression import DeployedPackageGroupingExpression


@JsonMap({})
class DeployedPackageQueryConfigQueryFilter(BaseModel):
    """DeployedPackageQueryConfigQueryFilter

    :param expression: expression
    :type expression: DeployedPackageExpression
    """

    def __init__(self, expression: DeployedPackageExpression, **kwargs):
        """DeployedPackageQueryConfigQueryFilter

        :param expression: expression
        :type expression: DeployedPackageExpression
        """
        self.expression = DeployedPackageExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class DeployedPackageQueryConfig(BaseModel):
    """DeployedPackageQueryConfig

    :param query_filter: query_filter (optional)
    :type query_filter: Optional[DeployedPackageQueryConfigQueryFilter]
    """

    def __init__(self, query_filter: Optional[DeployedPackageQueryConfigQueryFilter] = None, **kwargs):
        """DeployedPackageQueryConfig

        :param query_filter: query_filter (optional)
        :type query_filter: Optional[DeployedPackageQueryConfigQueryFilter]
        """
        self.query_filter = self._define_object(
            query_filter, DeployedPackageQueryConfigQueryFilter
        ) if query_filter is not None else None
        self._kwargs = kwargs
