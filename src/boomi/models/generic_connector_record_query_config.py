
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .generic_connector_record_expression import (
    GenericConnectorRecordExpression,
    GenericConnectorRecordExpressionGuard,
)
from .generic_connector_record_simple_expression import (
    GenericConnectorRecordSimpleExpression,
)
from .generic_connector_record_grouping_expression import (
    GenericConnectorRecordGroupingExpression,
)


@JsonMap({})
class GenericConnectorRecordQueryConfigQueryFilter(BaseModel):
    """GenericConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: GenericConnectorRecordExpression
    """

    def __init__(self, expression: GenericConnectorRecordExpression, **kwargs):
        """GenericConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: GenericConnectorRecordExpression
        """
        self.expression = GenericConnectorRecordExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class GenericConnectorRecordQueryConfig(BaseModel):
    """GenericConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: GenericConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: GenericConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """GenericConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: GenericConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, GenericConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
