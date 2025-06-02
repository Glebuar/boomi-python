
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .environment_atom_attachment_expression import EnvironmentAtomAttachmentExpression, EnvironmentAtomAttachmentExpressionGuard
from .environment_atom_attachment_simple_expression import (
    EnvironmentAtomAttachmentSimpleExpression,
)

class EnvironmentAtomAttachmentGroupingExpressionOperator(Enum):
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
                EnvironmentAtomAttachmentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class EnvironmentAtomAttachmentGroupingExpression(BaseModel):
    """EnvironmentAtomAttachmentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[EnvironmentAtomAttachmentExpression], optional
    :param operator: operator
    :type operator: EnvironmentAtomAttachmentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: EnvironmentAtomAttachmentGroupingExpressionOperator,
        nested_expression: List[EnvironmentAtomAttachmentExpression] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentAtomAttachmentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[EnvironmentAtomAttachmentExpression], optional
        :param operator: operator
        :type operator: EnvironmentAtomAttachmentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, EnvironmentAtomAttachmentExpression
            )
        self.operator = self._enum_matching(
            operator,
            EnvironmentAtomAttachmentGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
