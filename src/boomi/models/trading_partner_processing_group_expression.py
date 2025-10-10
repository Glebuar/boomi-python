
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .trading_partner_processing_group_simple_expression import (
    TradingPartnerProcessingGroupSimpleExpression,
)
from .trading_partner_processing_group_grouping_expression import (
    TradingPartnerProcessingGroupGroupingExpression,
)


class TradingPartnerProcessingGroupExpressionGuard(OneOfBaseModel):
    class_list = {
        "TradingPartnerProcessingGroupSimpleExpression": TradingPartnerProcessingGroupSimpleExpression,
        "TradingPartnerProcessingGroupGroupingExpression": TradingPartnerProcessingGroupGroupingExpression,
    }


TradingPartnerProcessingGroupExpression = Union[
    TradingPartnerProcessingGroupSimpleExpression,
    TradingPartnerProcessingGroupGroupingExpression,
]
