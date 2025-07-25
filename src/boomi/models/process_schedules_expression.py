
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .process_schedules_simple_expression import ProcessSchedulesSimpleExpression
from .process_schedules_grouping_expression import ProcessSchedulesGroupingExpression


class ProcessSchedulesExpressionGuard(OneOfBaseModel):
    class_list = {
        "ProcessSchedulesSimpleExpression": ProcessSchedulesSimpleExpression,
        "ProcessSchedulesGroupingExpression": ProcessSchedulesGroupingExpression,
    }


ProcessSchedulesExpression = Union[
    ProcessSchedulesSimpleExpression, ProcessSchedulesGroupingExpression
]
