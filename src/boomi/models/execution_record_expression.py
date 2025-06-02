
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .execution_record_simple_expression import ExecutionRecordSimpleExpression
from .execution_record_grouping_expression import ExecutionRecordGroupingExpression


class ExecutionRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "ExecutionRecordSimpleExpression": ExecutionRecordSimpleExpression,
        "ExecutionRecordGroupingExpression": ExecutionRecordGroupingExpression,
    }


ExecutionRecordExpression = Union[
    ExecutionRecordSimpleExpression, ExecutionRecordGroupingExpression
]
