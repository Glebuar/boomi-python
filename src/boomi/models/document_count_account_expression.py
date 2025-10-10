
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .document_count_account_simple_expression import (
    DocumentCountAccountSimpleExpression,
)
from .document_count_account_grouping_expression import (
    DocumentCountAccountGroupingExpression,
)


class DocumentCountAccountExpressionGuard(OneOfBaseModel):
    class_list = {
        "DocumentCountAccountSimpleExpression": DocumentCountAccountSimpleExpression,
        "DocumentCountAccountGroupingExpression": DocumentCountAccountGroupingExpression,
    }


DocumentCountAccountExpression = Union[
    DocumentCountAccountSimpleExpression, DocumentCountAccountGroupingExpression
]
