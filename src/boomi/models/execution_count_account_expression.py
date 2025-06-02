
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .execution_count_account_simple_expression import (
    ExecutionCountAccountSimpleExpression,
)
from .execution_count_account_grouping_expression import (
    ExecutionCountAccountGroupingExpression,
)


class ExecutionCountAccountExpressionGuard(OneOfBaseModel):
    class_list = {
        "ExecutionCountAccountSimpleExpression": ExecutionCountAccountSimpleExpression,
        "ExecutionCountAccountGroupingExpression": ExecutionCountAccountGroupingExpression,
    }


ExecutionCountAccountExpression = Union[
    ExecutionCountAccountSimpleExpression, ExecutionCountAccountGroupingExpression
]
