
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .execution_count_account_group_simple_expression import (
    ExecutionCountAccountGroupSimpleExpression,
)
from .execution_count_account_group_grouping_expression import (
    ExecutionCountAccountGroupGroupingExpression,
)


class ExecutionCountAccountGroupExpressionGuard(OneOfBaseModel):
    class_list = {
        "ExecutionCountAccountGroupSimpleExpression": ExecutionCountAccountGroupSimpleExpression,
        "ExecutionCountAccountGroupGroupingExpression": ExecutionCountAccountGroupGroupingExpression,
    }


ExecutionCountAccountGroupExpression = Union[
    ExecutionCountAccountGroupSimpleExpression,
    ExecutionCountAccountGroupGroupingExpression,
]
