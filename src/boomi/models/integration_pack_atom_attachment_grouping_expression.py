
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .integration_pack_atom_attachment_expression import IntegrationPackAtomAttachmentExpression, IntegrationPackAtomAttachmentExpressionGuard
from .integration_pack_atom_attachment_simple_expression import (
    IntegrationPackAtomAttachmentSimpleExpression,
)

class IntegrationPackAtomAttachmentGroupingExpressionOperator(Enum):
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
                IntegrationPackAtomAttachmentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class IntegrationPackAtomAttachmentGroupingExpression(BaseModel):
    """IntegrationPackAtomAttachmentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[IntegrationPackAtomAttachmentExpression], optional
    :param operator: operator
    :type operator: IntegrationPackAtomAttachmentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: IntegrationPackAtomAttachmentGroupingExpressionOperator,
        nested_expression: List[IntegrationPackAtomAttachmentExpression] = SENTINEL,
        **kwargs,
    ):
        """IntegrationPackAtomAttachmentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[IntegrationPackAtomAttachmentExpression], optional
        :param operator: operator
        :type operator: IntegrationPackAtomAttachmentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, IntegrationPackAtomAttachmentExpression
            )
        self.operator = self._enum_matching(
            operator,
            IntegrationPackAtomAttachmentGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
