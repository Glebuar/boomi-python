
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .account_simple_expression import AccountSimpleExpression
from .account_grouping_expression import AccountGroupingExpression


class AccountExpressionGuard(OneOfBaseModel):
    class_list = {
        "AccountSimpleExpression": AccountSimpleExpression,
        "AccountGroupingExpression": AccountGroupingExpression,
    }


AccountExpression = Union[AccountSimpleExpression, AccountGroupingExpression]
