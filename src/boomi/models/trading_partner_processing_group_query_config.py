
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .trading_partner_processing_group_expression import (
    TradingPartnerProcessingGroupExpression,
    TradingPartnerProcessingGroupExpressionGuard,
)
from .trading_partner_processing_group_simple_expression import (
    TradingPartnerProcessingGroupSimpleExpression,
)
from .trading_partner_processing_group_grouping_expression import (
    TradingPartnerProcessingGroupGroupingExpression,
)


@JsonMap({})
class TradingPartnerProcessingGroupQueryConfigQueryFilter(BaseModel):
    """TradingPartnerProcessingGroupQueryConfigQueryFilter

    :param expression: expression
    :type expression: TradingPartnerProcessingGroupExpression
    """

    def __init__(self, expression: TradingPartnerProcessingGroupExpression, **kwargs):
        """TradingPartnerProcessingGroupQueryConfigQueryFilter

        :param expression: expression
        :type expression: TradingPartnerProcessingGroupExpression
        """
        self.expression = TradingPartnerProcessingGroupExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class TradingPartnerProcessingGroupQueryConfig(BaseModel):
    """TradingPartnerProcessingGroupQueryConfig

    :param query_filter: query_filter
    :type query_filter: TradingPartnerProcessingGroupQueryConfigQueryFilter
    """

    def __init__(
        self,
        query_filter: TradingPartnerProcessingGroupQueryConfigQueryFilter,
        **kwargs,
    ):
        """TradingPartnerProcessingGroupQueryConfig

        :param query_filter: query_filter
        :type query_filter: TradingPartnerProcessingGroupQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, TradingPartnerProcessingGroupQueryConfigQueryFilter
        )
        self._kwargs = kwargs
