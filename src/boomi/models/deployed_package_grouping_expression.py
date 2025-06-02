
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .deployed_package_expression import DeployedPackageExpression, DeployedPackageExpressionGuard
from .deployed_package_simple_expression import DeployedPackageSimpleExpression

class DeployedPackageGroupingExpressionOperator(Enum):
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
                DeployedPackageGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class DeployedPackageGroupingExpression(BaseModel):
    """DeployedPackageGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[DeployedPackageExpression], optional
    :param operator: operator
    :type operator: DeployedPackageGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: DeployedPackageGroupingExpressionOperator,
        nested_expression: List[DeployedPackageExpression] = SENTINEL,
        **kwargs,
    ):
        """DeployedPackageGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[DeployedPackageExpression], optional
        :param operator: operator
        :type operator: DeployedPackageGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, DeployedPackageExpression
            )
        self.operator = self._enum_matching(
            operator, DeployedPackageGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
