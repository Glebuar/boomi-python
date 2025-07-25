
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .component_metadata_simple_expression import ComponentMetadataSimpleExpression
from .component_metadata_grouping_expression import ComponentMetadataGroupingExpression


class ComponentMetadataExpressionGuard(OneOfBaseModel):
    class_list = {
        "ComponentMetadataSimpleExpression": ComponentMetadataSimpleExpression,
        "ComponentMetadataGroupingExpression": ComponentMetadataGroupingExpression,
    }


ComponentMetadataExpression = Union[
    ComponentMetadataSimpleExpression, ComponentMetadataGroupingExpression
]
