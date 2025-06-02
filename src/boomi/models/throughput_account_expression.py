
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .throughput_account_simple_expression import ThroughputAccountSimpleExpression
from .throughput_account_grouping_expression import ThroughputAccountGroupingExpression


class ThroughputAccountExpressionGuard(OneOfBaseModel):
    class_list = {
        "ThroughputAccountSimpleExpression": ThroughputAccountSimpleExpression,
        "ThroughputAccountGroupingExpression": ThroughputAccountGroupingExpression,
    }


ThroughputAccountExpression = Union[
    ThroughputAccountSimpleExpression, ThroughputAccountGroupingExpression
]
