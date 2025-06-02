
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .as2_connector_record_simple_expression import As2ConnectorRecordSimpleExpression
from .as2_connector_record_grouping_expression import (
    As2ConnectorRecordGroupingExpression,
)


class As2ConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "As2ConnectorRecordSimpleExpression": As2ConnectorRecordSimpleExpression,
        "As2ConnectorRecordGroupingExpression": As2ConnectorRecordGroupingExpression,
    }


As2ConnectorRecordExpression = Union[
    As2ConnectorRecordSimpleExpression, As2ConnectorRecordGroupingExpression
]
