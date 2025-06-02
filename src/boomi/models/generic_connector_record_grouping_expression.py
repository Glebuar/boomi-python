
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .generic_connector_record_expression import GenericConnectorRecordExpression, GenericConnectorRecordExpressionGuard
from .generic_connector_record_simple_expression import (
    GenericConnectorRecordSimpleExpression,
)

class GenericConnectorRecordGroupingExpressionOperator(Enum):
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
                GenericConnectorRecordGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class GenericConnectorRecordGroupingExpression(BaseModel):
    """GenericConnectorRecordGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[GenericConnectorRecordExpression], optional
    :param operator: operator
    :type operator: GenericConnectorRecordGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: GenericConnectorRecordGroupingExpressionOperator,
        nested_expression: List[GenericConnectorRecordExpression] = SENTINEL,
        **kwargs,
    ):
        """GenericConnectorRecordGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[GenericConnectorRecordExpression], optional
        :param operator: operator
        :type operator: GenericConnectorRecordGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, GenericConnectorRecordExpression
            )
        self.operator = self._enum_matching(
            operator,
            GenericConnectorRecordGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
