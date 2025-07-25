
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .hl7_connector_record_expression import (
    Hl7ConnectorRecordExpression,
    Hl7ConnectorRecordExpressionGuard,
)
from .hl7_connector_record_simple_expression import Hl7ConnectorRecordSimpleExpression
from .hl7_connector_record_grouping_expression import (
    Hl7ConnectorRecordGroupingExpression,
)


@JsonMap({})
class Hl7ConnectorRecordQueryConfigQueryFilter(BaseModel):
    """Hl7ConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: Hl7ConnectorRecordExpression
    """

    def __init__(self, expression: Hl7ConnectorRecordExpression, **kwargs):
        """Hl7ConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: Hl7ConnectorRecordExpression
        """
        self.expression = Hl7ConnectorRecordExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class Hl7ConnectorRecordQueryConfig(BaseModel):
    """Hl7ConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: Hl7ConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: Hl7ConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """Hl7ConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: Hl7ConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, Hl7ConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
