
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .integration_pack_atom_attachment_simple_expression import (
    IntegrationPackAtomAttachmentSimpleExpression,
)
from .integration_pack_atom_attachment_grouping_expression import (
    IntegrationPackAtomAttachmentGroupingExpression,
)


class IntegrationPackAtomAttachmentExpressionGuard(OneOfBaseModel):
    class_list = {
        "IntegrationPackAtomAttachmentSimpleExpression": IntegrationPackAtomAttachmentSimpleExpression,
        "IntegrationPackAtomAttachmentGroupingExpression": IntegrationPackAtomAttachmentGroupingExpression,
    }


IntegrationPackAtomAttachmentExpression = Union[
    IntegrationPackAtomAttachmentSimpleExpression,
    IntegrationPackAtomAttachmentGroupingExpression,
]
