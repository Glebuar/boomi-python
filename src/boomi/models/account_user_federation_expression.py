
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .account_user_federation_simple_expression import (
    AccountUserFederationSimpleExpression,
)
from .account_user_federation_grouping_expression import (
    AccountUserFederationGroupingExpression,
)


class AccountUserFederationExpressionGuard(OneOfBaseModel):
    class_list = {
        "AccountUserFederationSimpleExpression": AccountUserFederationSimpleExpression,
        "AccountUserFederationGroupingExpression": AccountUserFederationGroupingExpression,
    }


AccountUserFederationExpression = Union[
    AccountUserFederationSimpleExpression, AccountUserFederationGroupingExpression
]
