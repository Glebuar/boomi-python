
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .merge_request_expression import MergeRequestExpression, MergeRequestExpressionGuard
from .merge_request_simple_expression import MergeRequestSimpleExpression

class MergeRequestGroupingExpressionOperator(Enum):
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
                MergeRequestGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class MergeRequestGroupingExpression(BaseModel):
    """MergeRequestGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[MergeRequestExpression], optional
    :param operator: operator
    :type operator: MergeRequestGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: MergeRequestGroupingExpressionOperator,
        nested_expression: List[MergeRequestExpression] = SENTINEL,
        **kwargs,
    ):
        """MergeRequestGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[MergeRequestExpression], optional
        :param operator: operator
        :type operator: MergeRequestGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, MergeRequestExpression
            )
        self.operator = self._enum_matching(
            operator, MergeRequestGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
