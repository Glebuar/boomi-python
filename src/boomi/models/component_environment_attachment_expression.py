
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .component_environment_attachment_simple_expression import (
    ComponentEnvironmentAttachmentSimpleExpression,
)
from .component_environment_attachment_grouping_expression import (
    ComponentEnvironmentAttachmentGroupingExpression,
)


class ComponentEnvironmentAttachmentExpressionGuard(OneOfBaseModel):
    class_list = {
        "ComponentEnvironmentAttachmentSimpleExpression": ComponentEnvironmentAttachmentSimpleExpression,
        "ComponentEnvironmentAttachmentGroupingExpression": ComponentEnvironmentAttachmentGroupingExpression,
    }


ComponentEnvironmentAttachmentExpression = Union[
    ComponentEnvironmentAttachmentSimpleExpression,
    ComponentEnvironmentAttachmentGroupingExpression,
]
