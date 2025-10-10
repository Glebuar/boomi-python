
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .integration_pack_expression import IntegrationPackExpression, IntegrationPackExpressionGuard
from .integration_pack_simple_expression import IntegrationPackSimpleExpression

class IntegrationPackGroupingExpressionOperator(Enum):
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
                IntegrationPackGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class IntegrationPackGroupingExpression(BaseModel):
    """IntegrationPackGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[IntegrationPackExpression], optional
    :param operator: operator
    :type operator: IntegrationPackGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: IntegrationPackGroupingExpressionOperator,
        nested_expression: List[IntegrationPackExpression] = SENTINEL,
        **kwargs,
    ):
        """IntegrationPackGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[IntegrationPackExpression], optional
        :param operator: operator
        :type operator: IntegrationPackGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, IntegrationPackExpression
            )
        self.operator = self._enum_matching(
            operator, IntegrationPackGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
