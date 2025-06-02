
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .rosetta_net_connector_record_simple_expression import (
    RosettaNetConnectorRecordSimpleExpression,
)
from .rosetta_net_connector_record_grouping_expression import (
    RosettaNetConnectorRecordGroupingExpression,
)


class RosettaNetConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "RosettaNetConnectorRecordSimpleExpression": RosettaNetConnectorRecordSimpleExpression,
        "RosettaNetConnectorRecordGroupingExpression": RosettaNetConnectorRecordGroupingExpression,
    }


RosettaNetConnectorRecordExpression = Union[
    RosettaNetConnectorRecordSimpleExpression,
    RosettaNetConnectorRecordGroupingExpression,
]
