
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .throughput_account_group_simple_expression import (
    ThroughputAccountGroupSimpleExpression,
)
from .throughput_account_group_grouping_expression import (
    ThroughputAccountGroupGroupingExpression,
)


class ThroughputAccountGroupExpressionGuard(OneOfBaseModel):
    class_list = {
        "ThroughputAccountGroupSimpleExpression": ThroughputAccountGroupSimpleExpression,
        "ThroughputAccountGroupGroupingExpression": ThroughputAccountGroupGroupingExpression,
    }


ThroughputAccountGroupExpression = Union[
    ThroughputAccountGroupSimpleExpression, ThroughputAccountGroupGroupingExpression
]
