
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .process_schedule_status_simple_expression import (
    ProcessScheduleStatusSimpleExpression,
)
from .process_schedule_status_grouping_expression import (
    ProcessScheduleStatusGroupingExpression,
)


class ProcessScheduleStatusExpressionGuard(OneOfBaseModel):
    class_list = {
        "ProcessScheduleStatusSimpleExpression": ProcessScheduleStatusSimpleExpression,
        "ProcessScheduleStatusGroupingExpression": ProcessScheduleStatusGroupingExpression,
    }


ProcessScheduleStatusExpression = Union[
    ProcessScheduleStatusSimpleExpression, ProcessScheduleStatusGroupingExpression
]
