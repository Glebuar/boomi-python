
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .execution_summary_record_expression import (
    ExecutionSummaryRecordExpression,
    ExecutionSummaryRecordExpressionGuard,
)
from .execution_summary_record_simple_expression import (
    ExecutionSummaryRecordSimpleExpression,
)
from .execution_summary_record_grouping_expression import (
    ExecutionSummaryRecordGroupingExpression,
)


@JsonMap({})
class ExecutionSummaryRecordQueryConfigQueryFilter(BaseModel):
    """ExecutionSummaryRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: ExecutionSummaryRecordExpression
    """

    def __init__(self, expression: ExecutionSummaryRecordExpression, **kwargs):
        """ExecutionSummaryRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: ExecutionSummaryRecordExpression
        """
        self.expression = ExecutionSummaryRecordExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class ExecutionSummaryRecordQueryConfig(BaseModel):
    """ExecutionSummaryRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: ExecutionSummaryRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: ExecutionSummaryRecordQueryConfigQueryFilter, **kwargs
    ):
        """ExecutionSummaryRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: ExecutionSummaryRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, ExecutionSummaryRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
