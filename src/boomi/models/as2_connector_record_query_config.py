
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .as2_connector_record_expression import (
    As2ConnectorRecordExpression,
    As2ConnectorRecordExpressionGuard,
)
from .as2_connector_record_simple_expression import As2ConnectorRecordSimpleExpression
from .as2_connector_record_grouping_expression import (
    As2ConnectorRecordGroupingExpression,
)


@JsonMap({})
class As2ConnectorRecordQueryConfigQueryFilter(BaseModel):
    """As2ConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: As2ConnectorRecordExpression
    """

    def __init__(self, expression: As2ConnectorRecordExpression, **kwargs):
        """As2ConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: As2ConnectorRecordExpression
        """
        self.expression = As2ConnectorRecordExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class As2ConnectorRecordQueryConfig(BaseModel):
    """As2ConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: As2ConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: As2ConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """As2ConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: As2ConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, As2ConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
