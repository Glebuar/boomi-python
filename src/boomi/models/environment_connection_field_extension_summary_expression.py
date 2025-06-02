
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .environment_connection_field_extension_summary_simple_expression import (
    EnvironmentConnectionFieldExtensionSummarySimpleExpression,
)
from .environment_connection_field_extension_summary_grouping_expression import (
    EnvironmentConnectionFieldExtensionSummaryGroupingExpression,
)


class EnvironmentConnectionFieldExtensionSummaryExpressionGuard(OneOfBaseModel):
    class_list = {
        "EnvironmentConnectionFieldExtensionSummarySimpleExpression": EnvironmentConnectionFieldExtensionSummarySimpleExpression,
        "EnvironmentConnectionFieldExtensionSummaryGroupingExpression": EnvironmentConnectionFieldExtensionSummaryGroupingExpression,
    }


EnvironmentConnectionFieldExtensionSummaryExpression = Union[
    EnvironmentConnectionFieldExtensionSummarySimpleExpression,
    EnvironmentConnectionFieldExtensionSummaryGroupingExpression,
]
