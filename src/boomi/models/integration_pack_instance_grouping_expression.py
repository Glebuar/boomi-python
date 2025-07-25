
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .integration_pack_instance_expression import IntegrationPackInstanceExpression, IntegrationPackInstanceExpressionGuard
from .integration_pack_instance_simple_expression import (
    IntegrationPackInstanceSimpleExpression,
)

class IntegrationPackInstanceGroupingExpressionOperator(Enum):
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
                IntegrationPackInstanceGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class IntegrationPackInstanceGroupingExpression(BaseModel):
    """IntegrationPackInstanceGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[IntegrationPackInstanceExpression], optional
    :param operator: operator
    :type operator: IntegrationPackInstanceGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: IntegrationPackInstanceGroupingExpressionOperator,
        nested_expression: List[IntegrationPackInstanceExpression] = SENTINEL,
        **kwargs,
    ):
        """IntegrationPackInstanceGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[IntegrationPackInstanceExpression], optional
        :param operator: operator
        :type operator: IntegrationPackInstanceGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, IntegrationPackInstanceExpression
            )
        self.operator = self._enum_matching(
            operator,
            IntegrationPackInstanceGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
