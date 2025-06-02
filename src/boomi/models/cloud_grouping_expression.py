
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .cloud_expression import CloudExpression, CloudExpressionGuard
from .cloud_simple_expression import CloudSimpleExpression

class CloudGroupingExpressionOperator(Enum):
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
                lambda x: x.value, CloudGroupingExpressionOperator._member_map_.values()
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class CloudGroupingExpression(BaseModel):
    """CloudGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["CloudExpression"], optional
    :param operator: operator
    :type operator: CloudGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: CloudGroupingExpressionOperator,
        nested_expression: List["CloudExpression"] = SENTINEL,
        **kwargs,
    ):
        """CloudGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["CloudExpression"], optional
        :param operator: operator
        :type operator: CloudGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .cloud_expression import CloudExpression

            self.nested_expression = self._define_list(
                nested_expression, CloudExpression
            )
        self.operator = self._enum_matching(
            operator, CloudGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
