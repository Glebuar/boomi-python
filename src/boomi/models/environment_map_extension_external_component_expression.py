
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .environment_map_extension_external_component_simple_expression import (
    EnvironmentMapExtensionExternalComponentSimpleExpression,
)
from .environment_map_extension_external_component_grouping_expression import (
    EnvironmentMapExtensionExternalComponentGroupingExpression,
)


class EnvironmentMapExtensionExternalComponentExpressionGuard(OneOfBaseModel):
    class_list = {
        "EnvironmentMapExtensionExternalComponentSimpleExpression": EnvironmentMapExtensionExternalComponentSimpleExpression,
        "EnvironmentMapExtensionExternalComponentGroupingExpression": EnvironmentMapExtensionExternalComponentGroupingExpression,
    }


EnvironmentMapExtensionExternalComponentExpression = Union[
    EnvironmentMapExtensionExternalComponentSimpleExpression,
    EnvironmentMapExtensionExternalComponentGroupingExpression,
]
