
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .integration_pack_simple_expression import IntegrationPackSimpleExpression
from .integration_pack_grouping_expression import IntegrationPackGroupingExpression


class IntegrationPackExpressionGuard(OneOfBaseModel):
    class_list = {
        "IntegrationPackSimpleExpression": IntegrationPackSimpleExpression,
        "IntegrationPackGroupingExpression": IntegrationPackGroupingExpression,
    }


IntegrationPackExpression = Union[
    IntegrationPackSimpleExpression, IntegrationPackGroupingExpression
]
