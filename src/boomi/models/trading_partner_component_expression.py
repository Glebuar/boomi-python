
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .trading_partner_component_simple_expression import (
    TradingPartnerComponentSimpleExpression,
)
from .trading_partner_component_grouping_expression import (
    TradingPartnerComponentGroupingExpression,
)


class TradingPartnerComponentExpressionGuard(OneOfBaseModel):
    class_list = {
        "TradingPartnerComponentSimpleExpression": TradingPartnerComponentSimpleExpression,
        "TradingPartnerComponentGroupingExpression": TradingPartnerComponentGroupingExpression,
    }


TradingPartnerComponentExpression = Union[
    TradingPartnerComponentSimpleExpression, TradingPartnerComponentGroupingExpression
]
