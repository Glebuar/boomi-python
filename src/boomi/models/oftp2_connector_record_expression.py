
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .oftp2_connector_record_simple_expression import (
    Oftp2ConnectorRecordSimpleExpression,
)
from .oftp2_connector_record_grouping_expression import (
    Oftp2ConnectorRecordGroupingExpression,
)


class Oftp2ConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "Oftp2ConnectorRecordSimpleExpression": Oftp2ConnectorRecordSimpleExpression,
        "Oftp2ConnectorRecordGroupingExpression": Oftp2ConnectorRecordGroupingExpression,
    }


Oftp2ConnectorRecordExpression = Union[
    Oftp2ConnectorRecordSimpleExpression, Oftp2ConnectorRecordGroupingExpression
]
