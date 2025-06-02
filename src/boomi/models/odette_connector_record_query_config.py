
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .odette_connector_record_expression import (
    OdetteConnectorRecordExpression,
    OdetteConnectorRecordExpressionGuard,
)
from .odette_connector_record_simple_expression import (
    OdetteConnectorRecordSimpleExpression,
)
from .odette_connector_record_grouping_expression import (
    OdetteConnectorRecordGroupingExpression,
)


@JsonMap({})
class OdetteConnectorRecordQueryConfigQueryFilter(BaseModel):
    """OdetteConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: OdetteConnectorRecordExpression
    """

    def __init__(self, expression: OdetteConnectorRecordExpression, **kwargs):
        """OdetteConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: OdetteConnectorRecordExpression
        """
        self.expression = OdetteConnectorRecordExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class OdetteConnectorRecordQueryConfig(BaseModel):
    """OdetteConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: OdetteConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: OdetteConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """OdetteConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: OdetteConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, OdetteConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
