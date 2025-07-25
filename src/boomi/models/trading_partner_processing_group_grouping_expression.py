
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .trading_partner_processing_group_expression import TradingPartnerProcessingGroupExpression, TradingPartnerProcessingGroupExpressionGuard
from .trading_partner_processing_group_simple_expression import (
    TradingPartnerProcessingGroupSimpleExpression,
)

class TradingPartnerProcessingGroupGroupingExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar AND: "and"
    :vartype AND: str
    :cvar OR: "or"
    :vartype OR: str
    """

    AND = "and"
    OR = "or"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                TradingPartnerProcessingGroupGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class TradingPartnerProcessingGroupGroupingExpression(BaseModel):
    """TradingPartnerProcessingGroupGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[TradingPartnerProcessingGroupExpression], optional
    :param operator: operator
    :type operator: TradingPartnerProcessingGroupGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: TradingPartnerProcessingGroupGroupingExpressionOperator,
        nested_expression: List[TradingPartnerProcessingGroupExpression] = SENTINEL,
        **kwargs,
    ):
        """TradingPartnerProcessingGroupGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[TradingPartnerProcessingGroupExpression], optional
        :param operator: operator
        :type operator: TradingPartnerProcessingGroupGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, TradingPartnerProcessingGroupExpression
            )
        self.operator = self._enum_matching(
            operator,
            TradingPartnerProcessingGroupGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
