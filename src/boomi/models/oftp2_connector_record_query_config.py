
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .oftp2_connector_record_expression import (
    Oftp2ConnectorRecordExpression,
    Oftp2ConnectorRecordExpressionGuard,
)
from .oftp2_connector_record_simple_expression import (
    Oftp2ConnectorRecordSimpleExpression,
)
from .oftp2_connector_record_grouping_expression import (
    Oftp2ConnectorRecordGroupingExpression,
)


@JsonMap({})
class Oftp2ConnectorRecordQueryConfigQueryFilter(BaseModel):
    """Oftp2ConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: Oftp2ConnectorRecordExpression
    """

    def __init__(self, expression: Oftp2ConnectorRecordExpression, **kwargs):
        """Oftp2ConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: Oftp2ConnectorRecordExpression
        """
        self.expression = Oftp2ConnectorRecordExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class Oftp2ConnectorRecordQueryConfig(BaseModel):
    """Oftp2ConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: Oftp2ConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: Oftp2ConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """Oftp2ConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: Oftp2ConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, Oftp2ConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
