
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .component_atom_attachment_expression import ComponentAtomAttachmentExpression, ComponentAtomAttachmentExpressionGuard
from .component_atom_attachment_simple_expression import (
    ComponentAtomAttachmentSimpleExpression,
)

class ComponentAtomAttachmentGroupingExpressionOperator(Enum):
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
                ComponentAtomAttachmentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ComponentAtomAttachmentGroupingExpression(BaseModel):
    """ComponentAtomAttachmentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ComponentAtomAttachmentExpression], optional
    :param operator: operator
    :type operator: ComponentAtomAttachmentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ComponentAtomAttachmentGroupingExpressionOperator,
        nested_expression: List[ComponentAtomAttachmentExpression] = SENTINEL,
        **kwargs,
    ):
        """ComponentAtomAttachmentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ComponentAtomAttachmentExpression], optional
        :param operator: operator
        :type operator: ComponentAtomAttachmentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ComponentAtomAttachmentExpression
            )
        self.operator = self._enum_matching(
            operator,
            ComponentAtomAttachmentGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
