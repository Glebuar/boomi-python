
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .odette_connector_record_simple_expression import (
    OdetteConnectorRecordSimpleExpression,
)
from .odette_connector_record_grouping_expression import (
    OdetteConnectorRecordGroupingExpression,
)


class OdetteConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "OdetteConnectorRecordSimpleExpression": OdetteConnectorRecordSimpleExpression,
        "OdetteConnectorRecordGroupingExpression": OdetteConnectorRecordGroupingExpression,
    }


OdetteConnectorRecordExpression = Union[
    OdetteConnectorRecordSimpleExpression, OdetteConnectorRecordGroupingExpression
]
