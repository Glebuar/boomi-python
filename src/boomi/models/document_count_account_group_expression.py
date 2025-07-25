
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .document_count_account_group_simple_expression import (
    DocumentCountAccountGroupSimpleExpression,
)
from .document_count_account_group_grouping_expression import (
    DocumentCountAccountGroupGroupingExpression,
)


class DocumentCountAccountGroupExpressionGuard(OneOfBaseModel):
    class_list = {
        "DocumentCountAccountGroupSimpleExpression": DocumentCountAccountGroupSimpleExpression,
        "DocumentCountAccountGroupGroupingExpression": DocumentCountAccountGroupGroupingExpression,
    }


DocumentCountAccountGroupExpression = Union[
    DocumentCountAccountGroupSimpleExpression,
    DocumentCountAccountGroupGroupingExpression,
]
