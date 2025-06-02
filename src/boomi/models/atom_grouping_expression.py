
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .atom_expression import AtomExpression, AtomExpressionGuard
from .atom_simple_expression import AtomSimpleExpression

class AtomGroupingExpressionOperator(Enum):
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
            map(lambda x: x.value, AtomGroupingExpressionOperator._member_map_.values())
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AtomGroupingExpression(BaseModel):
    """AtomGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["AtomExpression"], optional
    :param operator: operator
    :type operator: AtomGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AtomGroupingExpressionOperator,
        nested_expression: List["AtomExpression"] = SENTINEL,
        **kwargs,
    ):
        """AtomGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["AtomExpression"], optional
        :param operator: operator
        :type operator: AtomGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .atom_expression import AtomExpression

            self.nested_expression = self._define_list(
                nested_expression, AtomExpression
            )
        self.operator = self._enum_matching(
            operator, AtomGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
