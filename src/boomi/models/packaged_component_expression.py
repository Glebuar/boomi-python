
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .packaged_component_simple_expression import PackagedComponentSimpleExpression
from .packaged_component_grouping_expression import PackagedComponentGroupingExpression


class PackagedComponentExpressionGuard(OneOfBaseModel):
    class_list = {
        "PackagedComponentSimpleExpression": PackagedComponentSimpleExpression,
        "PackagedComponentGroupingExpression": PackagedComponentGroupingExpression,
    }


PackagedComponentExpression = Union[
    PackagedComponentSimpleExpression, PackagedComponentGroupingExpression
]
