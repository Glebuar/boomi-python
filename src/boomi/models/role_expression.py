
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .role_simple_expression import RoleSimpleExpression
from .role_grouping_expression import RoleGroupingExpression


class RoleExpressionGuard(OneOfBaseModel):
    class_list = {
        "RoleSimpleExpression": RoleSimpleExpression,
        "RoleGroupingExpression": RoleGroupingExpression,
    }


RoleExpression = Union[RoleSimpleExpression, RoleGroupingExpression]
