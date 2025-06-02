
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .component_atom_attachment_simple_expression import (
    ComponentAtomAttachmentSimpleExpression,
)
from .component_atom_attachment_grouping_expression import (
    ComponentAtomAttachmentGroupingExpression,
)


class ComponentAtomAttachmentExpressionGuard(OneOfBaseModel):
    class_list = {
        "ComponentAtomAttachmentSimpleExpression": ComponentAtomAttachmentSimpleExpression,
        "ComponentAtomAttachmentGroupingExpression": ComponentAtomAttachmentGroupingExpression,
    }


ComponentAtomAttachmentExpression = Union[
    ComponentAtomAttachmentSimpleExpression, ComponentAtomAttachmentGroupingExpression
]
