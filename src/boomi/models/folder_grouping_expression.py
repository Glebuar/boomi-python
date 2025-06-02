
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .folder_expression import FolderExpression, FolderExpressionGuard
from .folder_simple_expression import FolderSimpleExpression

class FolderGroupingExpressionOperator(Enum):
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
                FolderGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class FolderGroupingExpression(BaseModel):
    """FolderGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["FolderExpression"], optional
    :param operator: operator
    :type operator: FolderGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: FolderGroupingExpressionOperator,
        nested_expression: List["FolderExpression"] = SENTINEL,
        **kwargs,
    ):
        """FolderGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["FolderExpression"], optional
        :param operator: operator
        :type operator: FolderGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .folder_expression import FolderExpression

            self.nested_expression = self._define_list(
                nested_expression, FolderExpression
            )
        self.operator = self._enum_matching(
            operator, FolderGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
