
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .oftp2_connector_record_expression import Oftp2ConnectorRecordExpression, Oftp2ConnectorRecordExpressionGuard
from .oftp2_connector_record_simple_expression import (
    Oftp2ConnectorRecordSimpleExpression,
)

class Oftp2ConnectorRecordGroupingExpressionOperator(Enum):
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
                Oftp2ConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class Oftp2ConnectorRecordGroupingExpression(BaseModel):
    """Oftp2ConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[Oftp2ConnectorRecordExpression], optional
    :param operator: operator
    :type operator: Oftp2ConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: Oftp2ConnectorRecordGroupingExpressionOperator,
        nested_expression: List[Oftp2ConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """Oftp2ConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[Oftp2ConnectorRecordExpression], optional
        :param operator: operator
        :type operator: Oftp2ConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, Oftp2ConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator, Oftp2ConnectorRecordGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
