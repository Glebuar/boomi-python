
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .folder_expression import FolderExpression, FolderExpressionGuard
from .folder_simple_expression import FolderSimpleExpression
from .folder_grouping_expression import FolderGroupingExpression


@JsonMap({})
class FolderQueryConfigQueryFilter(BaseModel):
    """FolderQueryConfigQueryFilter

    :param expression: expression
    :type expression: FolderExpression
    """

    def __init__(self, expression: FolderExpression, **kwargs):
        """FolderQueryConfigQueryFilter

        :param expression: expression
        :type expression: FolderExpression
        """
        self.expression = FolderExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class FolderQueryConfig(BaseModel):
    """FolderQueryConfig

    :param query_filter: query_filter
    :type query_filter: FolderQueryConfigQueryFilter
    """

    def __init__(self, query_filter: FolderQueryConfigQueryFilter, **kwargs):
        """FolderQueryConfig

        :param query_filter: query_filter
        :type query_filter: FolderQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, FolderQueryConfigQueryFilter
        )
        self._kwargs = kwargs
