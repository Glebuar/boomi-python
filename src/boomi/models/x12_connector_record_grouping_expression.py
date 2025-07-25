
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .x12_connector_record_expression import X12ConnectorRecordExpression, X12ConnectorRecordExpressionGuard
from .x12_connector_record_simple_expression import X12ConnectorRecordSimpleExpression

class X12ConnectorRecordGroupingExpressionOperator(Enum):
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
                X12ConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class X12ConnectorRecordGroupingExpression(BaseModel):
    """X12ConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[X12ConnectorRecordExpression], optional
    :param operator: operator
    :type operator: X12ConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: X12ConnectorRecordGroupingExpressionOperator,
        nested_expression: List[X12ConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """X12ConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[X12ConnectorRecordExpression], optional
        :param operator: operator
        :type operator: X12ConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, X12ConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator, X12ConnectorRecordGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
