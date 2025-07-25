
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .account_group_simple_expression import AccountGroupSimpleExpression
from .account_group_grouping_expression import AccountGroupGroupingExpression


class AccountGroupExpressionGuard(OneOfBaseModel):
    class_list = {
        "AccountGroupSimpleExpression": AccountGroupSimpleExpression,
        "AccountGroupGroupingExpression": AccountGroupGroupingExpression,
    }


AccountGroupExpression = Union[
    AccountGroupSimpleExpression, AccountGroupGroupingExpression
]
