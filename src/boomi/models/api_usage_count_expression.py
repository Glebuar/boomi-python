
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .api_usage_count_simple_expression import ApiUsageCountSimpleExpression
from .api_usage_count_grouping_expression import ApiUsageCountGroupingExpression


class ApiUsageCountExpressionGuard(OneOfBaseModel):
    class_list = {
        "ApiUsageCountSimpleExpression": ApiUsageCountSimpleExpression,
        "ApiUsageCountGroupingExpression": ApiUsageCountGroupingExpression,
    }


ApiUsageCountExpression = Union[
    ApiUsageCountSimpleExpression, ApiUsageCountGroupingExpression
]
