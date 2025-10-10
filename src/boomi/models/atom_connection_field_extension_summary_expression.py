
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .atom_connection_field_extension_summary_simple_expression import (
    AtomConnectionFieldExtensionSummarySimpleExpression,
)
from .atom_connection_field_extension_summary_grouping_expression import (
    AtomConnectionFieldExtensionSummaryGroupingExpression,
)


class AtomConnectionFieldExtensionSummaryExpressionGuard(OneOfBaseModel):
    class_list = {
        "AtomConnectionFieldExtensionSummarySimpleExpression": AtomConnectionFieldExtensionSummarySimpleExpression,
        "AtomConnectionFieldExtensionSummaryGroupingExpression": AtomConnectionFieldExtensionSummaryGroupingExpression,
    }


AtomConnectionFieldExtensionSummaryExpression = Union[
    AtomConnectionFieldExtensionSummarySimpleExpression,
    AtomConnectionFieldExtensionSummaryGroupingExpression,
]
