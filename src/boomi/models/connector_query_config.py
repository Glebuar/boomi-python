
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .connector_expression import ConnectorExpression, ConnectorExpressionGuard
from .connector_simple_expression import ConnectorSimpleExpression
from .connector_grouping_expression import ConnectorGroupingExpression


@JsonMap({})
class ConnectorQueryConfigQueryFilter(BaseModel):
    """ConnectorQueryConfigQueryFilter

    :param expression: expression
    :type expression: ConnectorExpression
    """

    def __init__(self, expression: ConnectorExpression, **kwargs):
        """ConnectorQueryConfigQueryFilter

        :param expression: expression
        :type expression: ConnectorExpression
        """
        self.expression = ConnectorExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ConnectorQueryConfig(BaseModel):
    """ConnectorQueryConfig

    :param query_filter: query_filter
    :type query_filter: ConnectorQueryConfigQueryFilter
    """

    def __init__(self, query_filter: ConnectorQueryConfigQueryFilter, **kwargs):
        """ConnectorQueryConfig

        :param query_filter: query_filter
        :type query_filter: ConnectorQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ConnectorQueryConfigQueryFilter
        )
        self._kwargs = kwargs
