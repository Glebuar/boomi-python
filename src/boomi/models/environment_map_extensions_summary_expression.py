
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .environment_map_extensions_summary_simple_expression import (
    EnvironmentMapExtensionsSummarySimpleExpression,
)
from .environment_map_extensions_summary_grouping_expression import (
    EnvironmentMapExtensionsSummaryGroupingExpression,
)


class EnvironmentMapExtensionsSummaryExpressionGuard(OneOfBaseModel):
    class_list = {
        "EnvironmentMapExtensionsSummarySimpleExpression": EnvironmentMapExtensionsSummarySimpleExpression,
        "EnvironmentMapExtensionsSummaryGroupingExpression": EnvironmentMapExtensionsSummaryGroupingExpression,
    }


EnvironmentMapExtensionsSummaryExpression = Union[
    EnvironmentMapExtensionsSummarySimpleExpression,
    EnvironmentMapExtensionsSummaryGroupingExpression,
]
