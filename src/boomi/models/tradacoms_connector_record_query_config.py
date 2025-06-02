
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .tradacoms_connector_record_expression import (
    TradacomsConnectorRecordExpression,
    TradacomsConnectorRecordExpressionGuard,
)
from .tradacoms_connector_record_simple_expression import (
    TradacomsConnectorRecordSimpleExpression,
)
from .tradacoms_connector_record_grouping_expression import (
    TradacomsConnectorRecordGroupingExpression,
)


@JsonMap({})
class TradacomsConnectorRecordQueryConfigQueryFilter(BaseModel):
    """TradacomsConnectorRecordQueryConfigQueryFilter

    :param expression: expression
    :type expression: TradacomsConnectorRecordExpression
    """

    def __init__(self, expression: TradacomsConnectorRecordExpression, **kwargs):
        """TradacomsConnectorRecordQueryConfigQueryFilter

        :param expression: expression
        :type expression: TradacomsConnectorRecordExpression
        """
        self.expression = TradacomsConnectorRecordExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class TradacomsConnectorRecordQueryConfig(BaseModel):
    """TradacomsConnectorRecordQueryConfig

    :param query_filter: query_filter
    :type query_filter: TradacomsConnectorRecordQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: TradacomsConnectorRecordQueryConfigQueryFilter, **kwargs
    ):
        """TradacomsConnectorRecordQueryConfig

        :param query_filter: query_filter
        :type query_filter: TradacomsConnectorRecordQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, TradacomsConnectorRecordQueryConfigQueryFilter
        )
        self._kwargs = kwargs
