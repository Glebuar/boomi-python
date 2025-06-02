
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .deployed_expired_certificate_expression import DeployedExpiredCertificateExpression, DeployedExpiredCertificateExpressionGuard
from .deployed_expired_certificate_simple_expression import (
    DeployedExpiredCertificateSimpleExpression,
)

class DeployedExpiredCertificateGroupingExpressionOperator(Enum):
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
                DeployedExpiredCertificateGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class DeployedExpiredCertificateGroupingExpression(BaseModel):
    """DeployedExpiredCertificateGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[DeployedExpiredCertificateExpression], optional
    :param operator: operator
    :type operator: DeployedExpiredCertificateGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: DeployedExpiredCertificateGroupingExpressionOperator,
        nested_expression: List[DeployedExpiredCertificateExpression] = SENTINEL,
        **kwargs,
    ):
        """DeployedExpiredCertificateGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[DeployedExpiredCertificateExpression], optional
        :param operator: operator
        :type operator: DeployedExpiredCertificateGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, DeployedExpiredCertificateExpression
            )
        self.operator = self._enum_matching(
            operator,
            DeployedExpiredCertificateGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
