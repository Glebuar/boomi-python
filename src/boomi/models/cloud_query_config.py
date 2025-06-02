
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .cloud_expression import CloudExpression, CloudExpressionGuard
from .cloud_simple_expression import CloudSimpleExpression
from .cloud_grouping_expression import CloudGroupingExpression


@JsonMap({})
class CloudQueryConfigQueryFilter(BaseModel):
    """CloudQueryConfigQueryFilter

    :param expression: expression
    :type expression: CloudExpression
    """

    def __init__(self, expression: CloudExpression, **kwargs):
        """CloudQueryConfigQueryFilter

        :param expression: expression
        :type expression: CloudExpression
        """
        self.expression = CloudExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class CloudQueryConfig(BaseModel):
    """CloudQueryConfig

    :param query_filter: query_filter
    :type query_filter: CloudQueryConfigQueryFilter
    """

    def __init__(self, query_filter: CloudQueryConfigQueryFilter, **kwargs):
        """CloudQueryConfig

        :param query_filter: query_filter
        :type query_filter: CloudQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, CloudQueryConfigQueryFilter
        )
        self._kwargs = kwargs
