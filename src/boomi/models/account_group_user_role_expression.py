
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .account_group_user_role_simple_expression import (
    AccountGroupUserRoleSimpleExpression,
)
from .account_group_user_role_grouping_expression import (
    AccountGroupUserRoleGroupingExpression,
)


class AccountGroupUserRoleExpressionGuard(OneOfBaseModel):
    class_list = {
        "AccountGroupUserRoleSimpleExpression": AccountGroupUserRoleSimpleExpression,
        "AccountGroupUserRoleGroupingExpression": AccountGroupUserRoleGroupingExpression,
    }


AccountGroupUserRoleExpression = Union[
    AccountGroupUserRoleSimpleExpression, AccountGroupUserRoleGroupingExpression
]
