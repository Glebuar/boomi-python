
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .document_count_account_group_expression import (
    DocumentCountAccountGroupExpression,
    DocumentCountAccountGroupExpressionGuard,
)
from .document_count_account_group_simple_expression import (
    DocumentCountAccountGroupSimpleExpression,
)
from .document_count_account_group_grouping_expression import (
    DocumentCountAccountGroupGroupingExpression,
)


@JsonMap({})
class DocumentCountAccountGroupQueryConfigQueryFilter(BaseModel):
    """DocumentCountAccountGroupQueryConfigQueryFilter

    :param expression: expression
    :type expression: DocumentCountAccountGroupExpression
    """

    def __init__(self, expression: DocumentCountAccountGroupExpression, **kwargs):
        """DocumentCountAccountGroupQueryConfigQueryFilter

        :param expression: expression
        :type expression: DocumentCountAccountGroupExpression
        """
        self.expression = DocumentCountAccountGroupExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class DocumentCountAccountGroupQueryConfig(BaseModel):
    """DocumentCountAccountGroupQueryConfig

    :param query_filter: query_filter
    :type query_filter: DocumentCountAccountGroupQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: DocumentCountAccountGroupQueryConfigQueryFilter, **kwargs
    ):
        """DocumentCountAccountGroupQueryConfig

        :param query_filter: query_filter
        :type query_filter: DocumentCountAccountGroupQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, DocumentCountAccountGroupQueryConfigQueryFilter
        )
        self._kwargs = kwargs
