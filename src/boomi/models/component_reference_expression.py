
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .component_reference_simple_expression import ComponentReferenceSimpleExpression
from .component_reference_grouping_expression import (
    ComponentReferenceGroupingExpression,
)


class ComponentReferenceExpressionGuard(OneOfBaseModel):
    class_list = {
        "ComponentReferenceSimpleExpression": ComponentReferenceSimpleExpression,
        "ComponentReferenceGroupingExpression": ComponentReferenceGroupingExpression,
    }


ComponentReferenceExpression = Union[
    ComponentReferenceSimpleExpression, ComponentReferenceGroupingExpression
]
