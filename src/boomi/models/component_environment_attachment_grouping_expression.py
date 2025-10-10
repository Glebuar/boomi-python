
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .component_environment_attachment_expression import ComponentEnvironmentAttachmentExpression, ComponentEnvironmentAttachmentExpressionGuard
from .component_environment_attachment_simple_expression import (
    ComponentEnvironmentAttachmentSimpleExpression,
)

class ComponentEnvironmentAttachmentGroupingExpressionOperator(Enum):
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
                ComponentEnvironmentAttachmentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ComponentEnvironmentAttachmentGroupingExpression(BaseModel):
    """ComponentEnvironmentAttachmentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ComponentEnvironmentAttachmentExpression], optional
    :param operator: operator
    :type operator: ComponentEnvironmentAttachmentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ComponentEnvironmentAttachmentGroupingExpressionOperator,
        nested_expression: List[ComponentEnvironmentAttachmentExpression] = SENTINEL,
        **kwargs,
    ):
        """ComponentEnvironmentAttachmentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ComponentEnvironmentAttachmentExpression], optional
        :param operator: operator
        :type operator: ComponentEnvironmentAttachmentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ComponentEnvironmentAttachmentExpression
            )
        self.operator = self._enum_matching(
            operator,
            ComponentEnvironmentAttachmentGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
