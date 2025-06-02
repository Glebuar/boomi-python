
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .process_atom_attachment_expression import ProcessAtomAttachmentExpression, ProcessAtomAttachmentExpressionGuard
from .process_atom_attachment_simple_expression import (
    ProcessAtomAttachmentSimpleExpression,
)

class ProcessAtomAttachmentGroupingExpressionOperator(Enum):
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
                ProcessAtomAttachmentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ProcessAtomAttachmentGroupingExpression(BaseModel):
    """ProcessAtomAttachmentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[ProcessAtomAttachmentExpression], optional
    :param operator: operator
    :type operator: ProcessAtomAttachmentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ProcessAtomAttachmentGroupingExpressionOperator,
        nested_expression: List[ProcessAtomAttachmentExpression] = SENTINEL,
        **kwargs,
    ):
        """ProcessAtomAttachmentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[ProcessAtomAttachmentExpression], optional
        :param operator: operator
        :type operator: ProcessAtomAttachmentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, ProcessAtomAttachmentExpression
            )
        self.operator = self._enum_matching(
            operator, ProcessAtomAttachmentGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
