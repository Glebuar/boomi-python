
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .x12_connector_record_simple_expression import X12ConnectorRecordSimpleExpression
from .x12_connector_record_grouping_expression import (
    X12ConnectorRecordGroupingExpression,
)


class X12ConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "X12ConnectorRecordSimpleExpression": X12ConnectorRecordSimpleExpression,
        "X12ConnectorRecordGroupingExpression": X12ConnectorRecordGroupingExpression,
    }


X12ConnectorRecordExpression = Union[
    X12ConnectorRecordSimpleExpression, X12ConnectorRecordGroupingExpression
]
