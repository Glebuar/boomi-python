
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .tradacoms_connector_record_simple_expression import (
    TradacomsConnectorRecordSimpleExpression,
)
from .tradacoms_connector_record_grouping_expression import (
    TradacomsConnectorRecordGroupingExpression,
)


class TradacomsConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "TradacomsConnectorRecordSimpleExpression": TradacomsConnectorRecordSimpleExpression,
        "TradacomsConnectorRecordGroupingExpression": TradacomsConnectorRecordGroupingExpression,
    }


TradacomsConnectorRecordExpression = Union[
    TradacomsConnectorRecordSimpleExpression, TradacomsConnectorRecordGroupingExpression
]
