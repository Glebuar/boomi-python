
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .rosetta_net_connector_record_expression import RosettaNetConnectorRecordExpression, RosettaNetConnectorRecordExpressionGuard
from .rosetta_net_connector_record_simple_expression import (
    RosettaNetConnectorRecordSimpleExpression,
)

class RosettaNetConnectorRecordGroupingExpressionOperator(Enum):
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
                RosettaNetConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class RosettaNetConnectorRecordGroupingExpression(BaseModel):
    """RosettaNetConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[RosettaNetConnectorRecordExpression], optional
    :param operator: operator
    :type operator: RosettaNetConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: RosettaNetConnectorRecordGroupingExpressionOperator,
        nested_expression: List[RosettaNetConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """RosettaNetConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[RosettaNetConnectorRecordExpression], optional
        :param operator: operator
        :type operator: RosettaNetConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, RosettaNetConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator,
            RosettaNetConnectorRecordGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
