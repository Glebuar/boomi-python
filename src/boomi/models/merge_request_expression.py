
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .merge_request_simple_expression import MergeRequestSimpleExpression
from .merge_request_grouping_expression import MergeRequestGroupingExpression


class MergeRequestExpressionGuard(OneOfBaseModel):
    class_list = {
        "MergeRequestSimpleExpression": MergeRequestSimpleExpression,
        "MergeRequestGroupingExpression": MergeRequestGroupingExpression,
    }


MergeRequestExpression = Union[
    MergeRequestSimpleExpression, MergeRequestGroupingExpression
]
