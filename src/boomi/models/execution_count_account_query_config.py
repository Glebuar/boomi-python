
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .execution_count_account_expression import (
    ExecutionCountAccountExpression,
    ExecutionCountAccountExpressionGuard,
)
from .execution_count_account_simple_expression import (
    ExecutionCountAccountSimpleExpression,
)
from .execution_count_account_grouping_expression import (
    ExecutionCountAccountGroupingExpression,
)


@JsonMap({})
class ExecutionCountAccountQueryConfigQueryFilter(BaseModel):
    """ExecutionCountAccountQueryConfigQueryFilter

    :param expression: expression
    :type expression: ExecutionCountAccountExpression
    """

    def __init__(self, expression: ExecutionCountAccountExpression, **kwargs):
        """ExecutionCountAccountQueryConfigQueryFilter

        :param expression: expression
        :type expression: ExecutionCountAccountExpression
        """
        self.expression = ExecutionCountAccountExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ExecutionCountAccountQueryConfig(BaseModel):
    """ExecutionCountAccountQueryConfig

    :param query_filter: query_filter
    :type query_filter: ExecutionCountAccountQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ExecutionCountAccountQueryConfigQueryFilter, **kwargs
    ):
        """ExecutionCountAccountQueryConfig

        :param query_filter: query_filter
        :type query_filter: ExecutionCountAccountQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ExecutionCountAccountQueryConfigQueryFilter
        )
        self._kwargs = kwargs
