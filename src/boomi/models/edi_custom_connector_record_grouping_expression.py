
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .edi_custom_connector_record_expression import EdiCustomConnectorRecordExpression, EdiCustomConnectorRecordExpressionGuard
from .edi_custom_connector_record_simple_expression import (
    EdiCustomConnectorRecordSimpleExpression,
)

class EdiCustomConnectorRecordGroupingExpressionOperator(Enum):
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
                EdiCustomConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EdiCustomConnectorRecordGroupingExpression(BaseModel):
    """EdiCustomConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[EdiCustomConnectorRecordExpression], optional
    :param operator: operator
    :type operator: EdiCustomConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EdiCustomConnectorRecordGroupingExpressionOperator,
        nested_expression: List[EdiCustomConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """EdiCustomConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[EdiCustomConnectorRecordExpression], optional
        :param operator: operator
        :type operator: EdiCustomConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, EdiCustomConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator,
            EdiCustomConnectorRecordGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
