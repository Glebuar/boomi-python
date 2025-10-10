
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .process_expression import ProcessExpression, ProcessExpressionGuard
from .process_simple_expression import ProcessSimpleExpression
from .process_grouping_expression import ProcessGroupingExpression


@JsonMap({})
class ProcessQueryConfigQueryFilter(BaseModel):
    """ProcessQueryConfigQueryFilter

    :param expression: expression
    :type expression: ProcessExpression
    """

    def __init__(self, expression: ProcessExpression, **kwargs):
        """ProcessQueryConfigQueryFilter

        :param expression: expression
        :type expression: ProcessExpression
        """
        self.expression = ProcessExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ProcessQueryConfig(BaseModel):
    """ProcessQueryConfig

    :param query_filter: query_filter
    :type query_filter: ProcessQueryConfigQueryFilter
    """

    def __init__(self, query_filter: ProcessQueryConfigQueryFilter, **kwargs):
        """ProcessQueryConfig

        :param query_filter: query_filter
        :type query_filter: ProcessQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ProcessQueryConfigQueryFilter
        )
        self._kwargs = kwargs
