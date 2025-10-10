
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .edi_custom_connector_record_simple_expression import (
    EdiCustomConnectorRecordSimpleExpression,
)
from .edi_custom_connector_record_grouping_expression import (
    EdiCustomConnectorRecordGroupingExpression,
)


class EdiCustomConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "EdiCustomConnectorRecordSimpleExpression": EdiCustomConnectorRecordSimpleExpression,
        "EdiCustomConnectorRecordGroupingExpression": EdiCustomConnectorRecordGroupingExpression,
    }


EdiCustomConnectorRecordExpression = Union[
    EdiCustomConnectorRecordSimpleExpression, EdiCustomConnectorRecordGroupingExpression
]
