
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .execution_record_expression import (
    ExecutionRecordExpression,
    ExecutionRecordExpressionGuard,
)
from .execution_record_simple_expression import ExecutionRecordSimpleExpression
from .execution_record_grouping_expression import ExecutionRecordGroupingExpression


@JsonMap({})
class ExecutionRecordQueryConfigQueryFilter(BaseModel):
    """ExecutionRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: ExecutionRecordExpression
    """

    def __init__(self, expression: ExecutionRecordExpression, **kwargs):
        """ExecutionRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: ExecutionRecordExpression
        """
        self.expression = ExecutionRecordExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"field_name": "fieldName", "sort_order": "sortOrder"})
class SortField(BaseModel):
    """SortField

    :param field_name: field_name, defaults to None
    :type field_name: str, optional
    :param sort_order: sort_order, defaults to None
    :type sort_order: str, optional
    """

    def __init__(
        self, field_name: str = SENTINEL, sort_order: str = SENTINEL, **kwargs
    ):
        """SortField

        :param field_name: field_name, defaults to None
        :type field_name: str, optional
        :param sort_order: sort_order, defaults to None
        :type sort_order: str, optional
        """
        if field_name is not SENTINEL:
            self.field_name = field_name
        if sort_order is not SENTINEL:
            self.sort_order = sort_order
        self._kwargs = kwargs


@JsonMap({"sort_field": "sortField"})
class QuerySort(BaseModel):
    """QuerySort

    :param sort_field: sort_field
    :type sort_field: List[SortField]
    """

    def __init__(self, sort_field: List[SortField], **kwargs):
        """QuerySort

        :param sort_field: sort_field
        :type sort_field: List[SortField]
        """
        self.sort_field = self._define_list(sort_field, SortField)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter", "query_sort": "QuerySort"})
class ExecutionRecordQueryConfig(BaseModel):
    """ExecutionRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: ExecutionRecordQueryConfigQueryFilter
    :param query_sort: query_sort, defaults to None
    :type query_sort: QuerySort, optional
    """

    def __init__(
        self,
        query_filter: ExecutionRecordQueryConfigQueryFilter,
        query_sort: QuerySort = SENTINEL,
        **kwargs,
    ):
        """ExecutionRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: ExecutionRecordQueryConfigQueryFilter
        :param query_sort: query_sort, defaults to None
        :type query_sort: QuerySort, optional
        """
        self.query_filter = self._define_object(
            query_filter, ExecutionRecordQueryConfigQueryFilter
        )
        if query_sort is not SENTINEL:
            self.query_sort = self._define_object(query_sort, QuerySort)
        self._kwargs = kwargs
