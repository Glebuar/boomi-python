
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .edifact_connector_record_expression import (
    EdifactConnectorRecordExpression,
    EdifactConnectorRecordExpressionGuard,
)
from .edifact_connector_record_simple_expression import (
    EdifactConnectorRecordSimpleExpression,
)
from .edifact_connector_record_grouping_expression import (
    EdifactConnectorRecordGroupingExpression,
)


@JsonMap({})
class EdifactConnectorRecordQueryConfigQueryFilter(BaseModel):
    """EdifactConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: EdifactConnectorRecordExpression
    """

    def __init__(self, expression: EdifactConnectorRecordExpression, **kwargs):
        """EdifactConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: EdifactConnectorRecordExpression
        """
        self.expression = EdifactConnectorRecordExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class EdifactConnectorRecordQueryConfig(BaseModel):
    """EdifactConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: EdifactConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: EdifactConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """EdifactConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: EdifactConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, EdifactConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
