
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .hl7_connector_record_simple_expression import Hl7ConnectorRecordSimpleExpression
from .hl7_connector_record_grouping_expression import (
    Hl7ConnectorRecordGroupingExpression,
)


class Hl7ConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "Hl7ConnectorRecordSimpleExpression": Hl7ConnectorRecordSimpleExpression,
        "Hl7ConnectorRecordGroupingExpression": Hl7ConnectorRecordGroupingExpression,
    }


Hl7ConnectorRecordExpression = Union[
    Hl7ConnectorRecordSimpleExpression, Hl7ConnectorRecordGroupingExpression
]
