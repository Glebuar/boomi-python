
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .atom_connection_field_extension_summary_expression import AtomConnectionFieldExtensionSummaryExpression, AtomConnectionFieldExtensionSummaryExpressionGuard
from .atom_connection_field_extension_summary_simple_expression import (
    AtomConnectionFieldExtensionSummarySimpleExpression,
)

class AtomConnectionFieldExtensionSummaryGroupingExpressionOperator(Enum):
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
                AtomConnectionFieldExtensionSummaryGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AtomConnectionFieldExtensionSummaryGroupingExpression(BaseModel):
    """AtomConnectionFieldExtensionSummaryGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[AtomConnectionFieldExtensionSummaryExpression], optional
    :param operator: operator
    :type operator: AtomConnectionFieldExtensionSummaryGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AtomConnectionFieldExtensionSummaryGroupingExpressionOperator,
        nested_expression: List[
            AtomConnectionFieldExtensionSummaryExpression
        ] = SENTINEL,
        **kwargs,
    ):
        """AtomConnectionFieldExtensionSummaryGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[AtomConnectionFieldExtensionSummaryExpression], optional
        :param operator: operator
        :type operator: AtomConnectionFieldExtensionSummaryGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, AtomConnectionFieldExtensionSummaryExpression
            )
        self.operator = self._enum_matching(
            operator,
            AtomConnectionFieldExtensionSummaryGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
