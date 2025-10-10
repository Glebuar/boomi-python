
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .x12_connector_record_expression import (
    X12ConnectorRecordExpression,
    X12ConnectorRecordExpressionGuard,
)
from .x12_connector_record_simple_expression import X12ConnectorRecordSimpleExpression
from .x12_connector_record_grouping_expression import (
    X12ConnectorRecordGroupingExpression,
)


@JsonMap({})
class X12ConnectorRecordQueryConfigQueryFilter(BaseModel):
    """X12ConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: X12ConnectorRecordExpression
    """

    def __init__(self, expression: X12ConnectorRecordExpression, **kwargs):
        """X12ConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: X12ConnectorRecordExpression
        """
        self.expression = X12ConnectorRecordExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class X12ConnectorRecordQueryConfig(BaseModel):
    """X12ConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: X12ConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: X12ConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """X12ConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: X12ConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, X12ConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
