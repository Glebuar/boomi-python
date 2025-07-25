
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .execution_count_account_group_expression import (
    ExecutionCountAccountGroupExpression,
    ExecutionCountAccountGroupExpressionGuard,
)
from .execution_count_account_group_simple_expression import (
    ExecutionCountAccountGroupSimpleExpression,
)
from .execution_count_account_group_grouping_expression import (
    ExecutionCountAccountGroupGroupingExpression,
)


@JsonMap({})
class ExecutionCountAccountGroupQueryConfigQueryFilter(BaseModel):
    """ExecutionCountAccountGroupQueryConfigQueryFilter

    :param expression: expression
    :type expression: ExecutionCountAccountGroupExpression
    """

    def __init__(self, expression: ExecutionCountAccountGroupExpression, **kwargs):
        """ExecutionCountAccountGroupQueryConfigQueryFilter

        :param expression: expression
        :type expression: ExecutionCountAccountGroupExpression
        """
        self.expression = ExecutionCountAccountGroupExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ExecutionCountAccountGroupQueryConfig(BaseModel):
    """ExecutionCountAccountGroupQueryConfig

    :param query_filter: query_filter
    :type query_filter: ExecutionCountAccountGroupQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ExecutionCountAccountGroupQueryConfigQueryFilter, **kwargs
    ):
        """ExecutionCountAccountGroupQueryConfig

        :param query_filter: query_filter
        :type query_filter: ExecutionCountAccountGroupQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ExecutionCountAccountGroupQueryConfigQueryFilter
        )
        self._kwargs = kwargs
