
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .process_environment_attachment_simple_expression import (
    ProcessEnvironmentAttachmentSimpleExpression,
)
from .process_environment_attachment_grouping_expression import (
    ProcessEnvironmentAttachmentGroupingExpression,
)


class ProcessEnvironmentAttachmentExpressionGuard(OneOfBaseModel):
    class_list = {
        "ProcessEnvironmentAttachmentSimpleExpression": ProcessEnvironmentAttachmentSimpleExpression,
        "ProcessEnvironmentAttachmentGroupingExpression": ProcessEnvironmentAttachmentGroupingExpression,
    }


ProcessEnvironmentAttachmentExpression = Union[
    ProcessEnvironmentAttachmentSimpleExpression,
    ProcessEnvironmentAttachmentGroupingExpression,
]
