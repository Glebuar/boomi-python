
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .process_atom_attachment_simple_expression import (
    ProcessAtomAttachmentSimpleExpression,
)
from .process_atom_attachment_grouping_expression import (
    ProcessAtomAttachmentGroupingExpression,
)


class ProcessAtomAttachmentExpressionGuard(OneOfBaseModel):
    class_list = {
        "ProcessAtomAttachmentSimpleExpression": ProcessAtomAttachmentSimpleExpression,
        "ProcessAtomAttachmentGroupingExpression": ProcessAtomAttachmentGroupingExpression,
    }


ProcessAtomAttachmentExpression = Union[
    ProcessAtomAttachmentSimpleExpression, ProcessAtomAttachmentGroupingExpression
]
