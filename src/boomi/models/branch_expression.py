
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .branch_simple_expression import BranchSimpleExpression
from .branch_grouping_expression import BranchGroupingExpression


class BranchExpressionGuard(OneOfBaseModel):
    class_list = {
        "BranchSimpleExpression": BranchSimpleExpression,
        "BranchGroupingExpression": BranchGroupingExpression,
    }


BranchExpression = Union[BranchSimpleExpression, BranchGroupingExpression]
