
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .deployment_expression import DeploymentExpression, DeploymentExpressionGuard
from .deployment_simple_expression import DeploymentSimpleExpression

class DeploymentGroupingExpressionOperator(Enum):
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
                DeploymentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class DeploymentGroupingExpression(BaseModel):
    """DeploymentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["DeploymentExpression"], optional
    :param operator: operator
    :type operator: DeploymentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: DeploymentGroupingExpressionOperator,
        nested_expression: List["DeploymentExpression"] = SENTINEL,
        **kwargs,
    ):
        """DeploymentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["DeploymentExpression"], optional
        :param operator: operator
        :type operator: DeploymentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .deployment_expression import DeploymentExpression

            self.nested_expression = self._define_list(
                nested_expression, DeploymentExpression
            )
        self.operator = self._enum_matching(
            operator, DeploymentGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
