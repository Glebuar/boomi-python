
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .integration_pack_environment_attachment_simple_expression import (
    IntegrationPackEnvironmentAttachmentSimpleExpression,
)
from .integration_pack_environment_attachment_grouping_expression import (
    IntegrationPackEnvironmentAttachmentGroupingExpression,
)


class IntegrationPackEnvironmentAttachmentExpressionGuard(OneOfBaseModel):
    class_list = {
        "IntegrationPackEnvironmentAttachmentSimpleExpression": IntegrationPackEnvironmentAttachmentSimpleExpression,
        "IntegrationPackEnvironmentAttachmentGroupingExpression": IntegrationPackEnvironmentAttachmentGroupingExpression,
    }


IntegrationPackEnvironmentAttachmentExpression = Union[
    IntegrationPackEnvironmentAttachmentSimpleExpression,
    IntegrationPackEnvironmentAttachmentGroupingExpression,
]
