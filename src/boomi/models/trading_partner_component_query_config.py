
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .trading_partner_component_expression import (
    TradingPartnerComponentExpression,
    TradingPartnerComponentExpressionGuard,
)
from .trading_partner_component_simple_expression import (
    TradingPartnerComponentSimpleExpression,
)
from .trading_partner_component_grouping_expression import (
    TradingPartnerComponentGroupingExpression,
)


@JsonMap({})
class TradingPartnerComponentQueryConfigQueryFilter(BaseModel):
    """TradingPartnerComponentQueryConfigQueryFilter

    :param expression: expression
    :type expression: TradingPartnerComponentExpression
    """

    def __init__(self, expression: TradingPartnerComponentExpression, **kwargs):
        """TradingPartnerComponentQueryConfigQueryFilter

        :param expression: expression
        :type expression: TradingPartnerComponentExpression
        """
        self.expression = TradingPartnerComponentExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class TradingPartnerComponentQueryConfig(BaseModel):
    """TradingPartnerComponentQueryConfig

    :param query_filter: query_filter
    :type query_filter: TradingPartnerComponentQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: TradingPartnerComponentQueryConfigQueryFilter, **kwargs
    ):
        """TradingPartnerComponentQueryConfig

        :param query_filter: query_filter
        :type query_filter: TradingPartnerComponentQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, TradingPartnerComponentQueryConfigQueryFilter
        )
        self._kwargs = kwargs
