
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .as2_connector_record_expression import As2ConnectorRecordExpression, As2ConnectorRecordExpressionGuard
from .as2_connector_record_simple_expression import As2ConnectorRecordSimpleExpression

class As2ConnectorRecordGroupingExpressionOperator(Enum):
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
                As2ConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class As2ConnectorRecordGroupingExpression(BaseModel):
    """As2ConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[As2ConnectorRecordExpression], optional
    :param operator: operator
    :type operator: As2ConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: As2ConnectorRecordGroupingExpressionOperator,
        nested_expression: List[As2ConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """As2ConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[As2ConnectorRecordExpression], optional
        :param operator: operator
        :type operator: As2ConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, As2ConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator, As2ConnectorRecordGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
