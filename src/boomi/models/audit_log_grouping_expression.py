
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .audit_log_expression import AuditLogExpression, AuditLogExpressionGuard
from .audit_log_simple_expression import AuditLogSimpleExpression

class AuditLogGroupingExpressionOperator(Enum):
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
                AuditLogGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AuditLogGroupingExpression(BaseModel):
    """AuditLogGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["AuditLogExpression"], optional
    :param operator: operator
    :type operator: AuditLogGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AuditLogGroupingExpressionOperator,
        nested_expression: List["AuditLogExpression"] = SENTINEL,
        **kwargs,
    ):
        """AuditLogGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["AuditLogExpression"], optional
        :param operator: operator
        :type operator: AuditLogGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .audit_log_expression import AuditLogExpression

            self.nested_expression = self._define_list(
                nested_expression, AuditLogExpression
            )
        self.operator = self._enum_matching(
            operator, AuditLogGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
