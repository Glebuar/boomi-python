
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .listener_status_simple_expression import ListenerStatusSimpleExpression
from .listener_status_grouping_expression import ListenerStatusGroupingExpression


class ListenerStatusExpressionGuard(OneOfBaseModel):
    class_list = {
        "ListenerStatusSimpleExpression": ListenerStatusSimpleExpression,
        "ListenerStatusGroupingExpression": ListenerStatusGroupingExpression,
    }


ListenerStatusExpression = Union[
    ListenerStatusSimpleExpression, ListenerStatusGroupingExpression
]
