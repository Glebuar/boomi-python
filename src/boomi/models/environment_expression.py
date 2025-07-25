
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .environment_simple_expression import EnvironmentSimpleExpression
from .environment_grouping_expression import EnvironmentGroupingExpression


class EnvironmentExpressionGuard(OneOfBaseModel):
    class_list = {
        "EnvironmentSimpleExpression": EnvironmentSimpleExpression,
        "EnvironmentGroupingExpression": EnvironmentGroupingExpression,
    }


EnvironmentExpression = Union[
    EnvironmentSimpleExpression, EnvironmentGroupingExpression
]
