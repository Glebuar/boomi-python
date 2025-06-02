
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .document_count_account_expression import (
    DocumentCountAccountExpression,
    DocumentCountAccountExpressionGuard,
)
from .document_count_account_simple_expression import (
    DocumentCountAccountSimpleExpression,
)
from .document_count_account_grouping_expression import (
    DocumentCountAccountGroupingExpression,
)


@JsonMap({})
class DocumentCountAccountQueryConfigQueryFilter(BaseModel):
    """DocumentCountAccountQueryConfigQueryFilter

    :param expression: expression
    :type expression: DocumentCountAccountExpression
    """

    def __init__(self, expression: DocumentCountAccountExpression, **kwargs):
        """DocumentCountAccountQueryConfigQueryFilter

        :param expression: expression
        :type expression: DocumentCountAccountExpression
        """
        self.expression = DocumentCountAccountExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class DocumentCountAccountQueryConfig(BaseModel):
    """DocumentCountAccountQueryConfig

    :param query_filter: query_filter
    :type query_filter: DocumentCountAccountQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: DocumentCountAccountQueryConfigQueryFilter, **kwargs
    ):
        """DocumentCountAccountQueryConfig

        :param query_filter: query_filter
        :type query_filter: DocumentCountAccountQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, DocumentCountAccountQueryConfigQueryFilter
        )
        self._kwargs = kwargs
