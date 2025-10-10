
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .branch_expression import BranchExpression, BranchExpressionGuard
from .branch_simple_expression import BranchSimpleExpression

class BranchGroupingExpressionOperator(Enum):
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
                BranchGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class BranchGroupingExpression(BaseModel):
    """BranchGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["BranchExpression"], optional
    :param operator: operator
    :type operator: BranchGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: BranchGroupingExpressionOperator,
        nested_expression: List["BranchExpression"] = SENTINEL,
        **kwargs,
    ):
        """BranchGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["BranchExpression"], optional
        :param operator: operator
        :type operator: BranchGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .branch_expression import BranchExpression

            self.nested_expression = self._define_list(
                nested_expression, BranchExpression
            )
        self.operator = self._enum_matching(
            operator, BranchGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
