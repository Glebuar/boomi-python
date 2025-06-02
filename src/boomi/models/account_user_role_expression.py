
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .account_user_role_simple_expression import AccountUserRoleSimpleExpression
from .account_user_role_grouping_expression import AccountUserRoleGroupingExpression


class AccountUserRoleExpressionGuard(OneOfBaseModel):
    class_list = {
        "AccountUserRoleSimpleExpression": AccountUserRoleSimpleExpression,
        "AccountUserRoleGroupingExpression": AccountUserRoleGroupingExpression,
    }


AccountUserRoleExpression = Union[
    AccountUserRoleSimpleExpression, AccountUserRoleGroupingExpression
]
