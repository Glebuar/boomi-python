
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .process_environment_attachment_expression import ProcessEnvironmentAttachmentExpression, ProcessEnvironmentAttachmentExpressionGuard
from .process_environment_attachment_simple_expression import (
    ProcessEnvironmentAttachmentSimpleExpression,
)

class ProcessEnvironmentAttachmentGroupingExpressionOperator(Enum):
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
                ProcessEnvironmentAttachmentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ProcessEnvironmentAttachmentGroupingExpression(BaseModel):
    """ProcessEnvironmentAttachmentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ProcessEnvironmentAttachmentExpression], optional
    :param operator: operator
    :type operator: ProcessEnvironmentAttachmentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ProcessEnvironmentAttachmentGroupingExpressionOperator,
        nested_expression: List[ProcessEnvironmentAttachmentExpression] = SENTINEL,
        **kwargs,
    ):
        """ProcessEnvironmentAttachmentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ProcessEnvironmentAttachmentExpression], optional
        :param operator: operator
        :type operator: ProcessEnvironmentAttachmentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ProcessEnvironmentAttachmentExpression
            )
        self.operator = self._enum_matching(
            operator,
            ProcessEnvironmentAttachmentGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
