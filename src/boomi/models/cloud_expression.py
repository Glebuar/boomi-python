
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .cloud_simple_expression import CloudSimpleExpression
from .cloud_grouping_expression import CloudGroupingExpression


class CloudExpressionGuard(OneOfBaseModel):
    class_list = {
        "CloudSimpleExpression": CloudSimpleExpression,
        "CloudGroupingExpression": CloudGroupingExpression,
    }


CloudExpression = Union[CloudSimpleExpression, CloudGroupingExpression]
