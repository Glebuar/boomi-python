
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .account_group_account_simple_expression import AccountGroupAccountSimpleExpression
from .account_group_account_grouping_expression import (
    AccountGroupAccountGroupingExpression,
)


class AccountGroupAccountExpressionGuard(OneOfBaseModel):
    class_list = {
        "AccountGroupAccountSimpleExpression": AccountGroupAccountSimpleExpression,
        "AccountGroupAccountGroupingExpression": AccountGroupAccountGroupingExpression,
    }


AccountGroupAccountExpression = Union[
    AccountGroupAccountSimpleExpression, AccountGroupAccountGroupingExpression
]
