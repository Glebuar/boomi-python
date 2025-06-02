
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .environment_atom_attachment_simple_expression import (
    EnvironmentAtomAttachmentSimpleExpression,
)
from .environment_atom_attachment_grouping_expression import (
    EnvironmentAtomAttachmentGroupingExpression,
)


class EnvironmentAtomAttachmentExpressionGuard(OneOfBaseModel):
    class_list = {
        "EnvironmentAtomAttachmentSimpleExpression": EnvironmentAtomAttachmentSimpleExpression,
        "EnvironmentAtomAttachmentGroupingExpression": EnvironmentAtomAttachmentGroupingExpression,
    }


EnvironmentAtomAttachmentExpression = Union[
    EnvironmentAtomAttachmentSimpleExpression,
    EnvironmentAtomAttachmentGroupingExpression,
]
