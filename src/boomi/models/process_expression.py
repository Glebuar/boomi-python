
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .process_simple_expression import ProcessSimpleExpression
from .process_grouping_expression import ProcessGroupingExpression


class ProcessExpressionGuard(OneOfBaseModel):
    class_list = {
        "ProcessSimpleExpression": ProcessSimpleExpression,
        "ProcessGroupingExpression": ProcessGroupingExpression,
    }


ProcessExpression = Union[ProcessSimpleExpression, ProcessGroupingExpression]
