
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .environment_role_simple_expression import EnvironmentRoleSimpleExpression
from .environment_role_grouping_expression import EnvironmentRoleGroupingExpression


class EnvironmentRoleExpressionGuard(OneOfBaseModel):
    class_list = {
        "EnvironmentRoleSimpleExpression": EnvironmentRoleSimpleExpression,
        "EnvironmentRoleGroupingExpression": EnvironmentRoleGroupingExpression,
    }


EnvironmentRoleExpression = Union[
    EnvironmentRoleSimpleExpression, EnvironmentRoleGroupingExpression
]
