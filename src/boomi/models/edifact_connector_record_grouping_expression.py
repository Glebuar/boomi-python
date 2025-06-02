
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .edifact_connector_record_expression import EdifactConnectorRecordExpression, EdifactConnectorRecordExpressionGuard
from .edifact_connector_record_simple_expression import (
    EdifactConnectorRecordSimpleExpression,
)

class EdifactConnectorRecordGroupingExpressionOperator(Enum):
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
                EdifactConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EdifactConnectorRecordGroupingExpression(BaseModel):
    """EdifactConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[EdifactConnectorRecordExpression], optional
    :param operator: operator
    :type operator: EdifactConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EdifactConnectorRecordGroupingExpressionOperator,
        nested_expression: List[EdifactConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """EdifactConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[EdifactConnectorRecordExpression], optional
        :param operator: operator
        :type operator: EdifactConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, EdifactConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator,
            EdifactConnectorRecordGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
