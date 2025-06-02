
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .tradacoms_connector_record_expression import TradacomsConnectorRecordExpression, TradacomsConnectorRecordExpressionGuard
from .tradacoms_connector_record_simple_expression import (
    TradacomsConnectorRecordSimpleExpression,
)

class TradacomsConnectorRecordGroupingExpressionOperator(Enum):
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
                TradacomsConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class TradacomsConnectorRecordGroupingExpression(BaseModel):
    """TradacomsConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[TradacomsConnectorRecordExpression], optional
    :param operator: operator
    :type operator: TradacomsConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: TradacomsConnectorRecordGroupingExpressionOperator,
        nested_expression: List[TradacomsConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """TradacomsConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[TradacomsConnectorRecordExpression], optional
        :param operator: operator
        :type operator: TradacomsConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, TradacomsConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator,
            TradacomsConnectorRecordGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
