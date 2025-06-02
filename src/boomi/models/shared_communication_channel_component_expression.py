
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .shared_communication_channel_component_simple_expression import (
    SharedCommunicationChannelComponentSimpleExpression,
)
from .shared_communication_channel_component_grouping_expression import (
    SharedCommunicationChannelComponentGroupingExpression,
)


class SharedCommunicationChannelComponentExpressionGuard(OneOfBaseModel):
    class_list = {
        "SharedCommunicationChannelComponentSimpleExpression": SharedCommunicationChannelComponentSimpleExpression,
        "SharedCommunicationChannelComponentGroupingExpression": SharedCommunicationChannelComponentGroupingExpression,
    }


SharedCommunicationChannelComponentExpression = Union[
    SharedCommunicationChannelComponentSimpleExpression,
    SharedCommunicationChannelComponentGroupingExpression,
]
