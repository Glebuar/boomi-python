
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .hl7_connector_record_expression import Hl7ConnectorRecordExpression, Hl7ConnectorRecordExpressionGuard
from .hl7_connector_record_simple_expression import Hl7ConnectorRecordSimpleExpression

class Hl7ConnectorRecordGroupingExpressionOperator(Enum):
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
                Hl7ConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class Hl7ConnectorRecordGroupingExpression(BaseModel):
    """Hl7ConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[Hl7ConnectorRecordExpression], optional
    :param operator: operator
    :type operator: Hl7ConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: Hl7ConnectorRecordGroupingExpressionOperator,
        nested_expression: List[Hl7ConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """Hl7ConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[Hl7ConnectorRecordExpression], optional
        :param operator: operator
        :type operator: Hl7ConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, Hl7ConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator, Hl7ConnectorRecordGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
