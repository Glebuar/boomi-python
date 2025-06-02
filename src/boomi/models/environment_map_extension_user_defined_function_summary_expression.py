
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .environment_map_extension_user_defined_function_summary_simple_expression import (
    EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpression,
)
from .environment_map_extension_user_defined_function_summary_grouping_expression import (
    EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression,
)


class EnvironmentMapExtensionUserDefinedFunctionSummaryExpressionGuard(OneOfBaseModel):
    class_list = {
        "EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpression": EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpression,
        "EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression": EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression,
    }


EnvironmentMapExtensionUserDefinedFunctionSummaryExpression = Union[
    EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpression,
    EnvironmentMapExtensionUserDefinedFunctionSummaryGroupingExpression,
]
