
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .generic_connector_record_simple_expression import (
    GenericConnectorRecordSimpleExpression,
)
from .generic_connector_record_grouping_expression import (
    GenericConnectorRecordGroupingExpression,
)


class GenericConnectorRecordExpressionGuard(OneOfBaseModel):
    class_list = {
        "GenericConnectorRecordSimpleExpression": GenericConnectorRecordSimpleExpression,
        "GenericConnectorRecordGroupingExpression": GenericConnectorRecordGroupingExpression,
    }


GenericConnectorRecordExpression = Union[
    GenericConnectorRecordSimpleExpression, GenericConnectorRecordGroupingExpression
]
