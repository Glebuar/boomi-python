
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .event_simple_expression import EventSimpleExpression
from .event_grouping_expression import EventGroupingExpression


class EventExpressionGuard(OneOfBaseModel):
    class_list = {
        "EventSimpleExpression": EventSimpleExpression,
        "EventGroupingExpression": EventGroupingExpression,
    }


EventExpression = Union[EventSimpleExpression, EventGroupingExpression]
