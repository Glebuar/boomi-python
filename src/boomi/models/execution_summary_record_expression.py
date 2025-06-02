
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .execution_summary_record_simple_expression import (
    ExecutionSummaryRecordSimpleExpression,
)
from .execution_summary_record_grouping_expression import (
    ExecutionSummaryRecordGroupingExpression,
)


class ExecutionSummaryRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "ExecutionSummaryRecordSimpleExpression": ExecutionSummaryRecordSimpleExpression,
        "ExecutionSummaryRecordGroupingExpression": ExecutionSummaryRecordGroupingExpression,
    }


ExecutionSummaryRecordExpression = Union[
    ExecutionSummaryRecordSimpleExpression, ExecutionSummaryRecordGroupingExpression
]
