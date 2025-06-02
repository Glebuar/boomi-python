
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .process_schedule_status_expression import (
    ProcessScheduleStatusExpression,
    ProcessScheduleStatusExpressionGuard,
)
from .process_schedule_status_simple_expression import (
    ProcessScheduleStatusSimpleExpression,
)
from .process_schedule_status_grouping_expression import (
    ProcessScheduleStatusGroupingExpression,
)


@JsonMap({})
class ProcessScheduleStatusQueryConfigQueryFilter(BaseModel):
    """ProcessScheduleStatusQueryConfigQueryFilter

    :param expression: expression
    :type expression: ProcessScheduleStatusExpression
    """

    def __init__(self, expression: ProcessScheduleStatusExpression, **kwargs):
        """ProcessScheduleStatusQueryConfigQueryFilter

        :param expression: expression
        :type expression: ProcessScheduleStatusExpression
        """
        self.expression = ProcessScheduleStatusExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ProcessScheduleStatusQueryConfig(BaseModel):
    """ProcessScheduleStatusQueryConfig

    :param query_filter: query_filter
    :type query_filter: ProcessScheduleStatusQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ProcessScheduleStatusQueryConfigQueryFilter, **kwargs
    ):
        """ProcessScheduleStatusQueryConfig

        :param query_filter: query_filter
        :type query_filter: ProcessScheduleStatusQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ProcessScheduleStatusQueryConfigQueryFilter
        )
        self._kwargs = kwargs
