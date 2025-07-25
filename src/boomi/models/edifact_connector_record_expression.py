
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .edifact_connector_record_simple_expression import (
    EdifactConnectorRecordSimpleExpression,
)
from .edifact_connector_record_grouping_expression import (
    EdifactConnectorRecordGroupingExpression,
)


class EdifactConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "EdifactConnectorRecordSimpleExpression": EdifactConnectorRecordSimpleExpression,
        "EdifactConnectorRecordGroupingExpression": EdifactConnectorRecordGroupingExpression,
    }


EdifactConnectorRecordExpression = Union[
    EdifactConnectorRecordSimpleExpression, EdifactConnectorRecordGroupingExpression
]
