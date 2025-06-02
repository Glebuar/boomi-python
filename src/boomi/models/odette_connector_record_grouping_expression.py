
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .odette_connector_record_expression import OdetteConnectorRecordExpression, OdetteConnectorRecordExpressionGuard
from .odette_connector_record_simple_expression import (
    OdetteConnectorRecordSimpleExpression,
)

class OdetteConnectorRecordGroupingExpressionOperator(Enum):
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
                OdetteConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class OdetteConnectorRecordGroupingExpression(BaseModel):
    """OdetteConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[OdetteConnectorRecordExpression], optional
    :param operator: operator
    :type operator: OdetteConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: OdetteConnectorRecordGroupingExpressionOperator,
        nested_expression: List[OdetteConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """OdetteConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[OdetteConnectorRecordExpression], optional
        :param operator: operator
        :type operator: OdetteConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, OdetteConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator, OdetteConnectorRecordGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
