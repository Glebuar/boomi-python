
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .environment_extensions_simple_expression import (
    EnvironmentExtensionsSimpleExpression,
)
from .environment_extensions_grouping_expression import (
    EnvironmentExtensionsGroupingExpression,
)


class EnvironmentExtensionsExpressionGuard(OneOfBaseModel):
    class_list = {
        "EnvironmentExtensionsSimpleExpression": EnvironmentExtensionsSimpleExpression,
        "EnvironmentExtensionsGroupingExpression": EnvironmentExtensionsGroupingExpression,
    }


EnvironmentExtensionsExpression = Union[
    EnvironmentExtensionsSimpleExpression, EnvironmentExtensionsGroupingExpression
]
