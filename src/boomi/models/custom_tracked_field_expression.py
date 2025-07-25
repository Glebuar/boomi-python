
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .custom_tracked_field_simple_expression import CustomTrackedFieldSimpleExpression
from .custom_tracked_field_grouping_expression import (
    CustomTrackedFieldGroupingExpression,
)


class CustomTrackedFieldExpressionGuard(OneOfBaseModel):
    class_list = {
        "CustomTrackedFieldSimpleExpression": CustomTrackedFieldSimpleExpression,
        "CustomTrackedFieldGroupingExpression": CustomTrackedFieldGroupingExpression,
    }


CustomTrackedFieldExpression = Union[
    CustomTrackedFieldSimpleExpression, CustomTrackedFieldGroupingExpression
]
