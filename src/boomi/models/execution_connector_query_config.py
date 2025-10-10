
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .execution_connector_expression import (
    ExecutionConnectorExpression,
    ExecutionConnectorExpressionGuard,
)
from .execution_connector_simple_expression import ExecutionConnectorSimpleExpression
from .execution_connector_grouping_expression import (
    ExecutionConnectorGroupingExpression,
)


@JsonMap({})
class ExecutionConnectorQueryConfigQueryFilter(BaseModel):
    """ExecutionConnectorQueryConfigQueryFilter

    :param expression: expression
    :type expression: ExecutionConnectorExpression
    """

    def __init__(self, expression: ExecutionConnectorExpression, **kwargs):
        """ExecutionConnectorQueryConfigQueryFilter

        :param expression: expression
        :type expression: ExecutionConnectorExpression
        """
        self.expression = ExecutionConnectorExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ExecutionConnectorQueryConfig(BaseModel):
    """ExecutionConnectorQueryConfig

    :param query_filter: query_filter
    :type query_filter: ExecutionConnectorQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ExecutionConnectorQueryConfigQueryFilter, **kwargs
    ):
        """ExecutionConnectorQueryConfig

        :param query_filter: query_filter
        :type query_filter: ExecutionConnectorQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ExecutionConnectorQueryConfigQueryFilter
        )
        self._kwargs = kwargs
