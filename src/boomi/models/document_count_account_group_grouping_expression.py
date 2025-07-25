
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .document_count_account_group_expression import DocumentCountAccountGroupExpression, DocumentCountAccountGroupExpressionGuard
from .document_count_account_group_simple_expression import (
    DocumentCountAccountGroupSimpleExpression,
)

class DocumentCountAccountGroupGroupingExpressionOperator(Enum):
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
                DocumentCountAccountGroupGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class DocumentCountAccountGroupGroupingExpression(BaseModel):
    """DocumentCountAccountGroupGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[DocumentCountAccountGroupExpression], optional
    :param operator: operator
    :type operator: DocumentCountAccountGroupGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: DocumentCountAccountGroupGroupingExpressionOperator,
        nested_expression: List[DocumentCountAccountGroupExpression] = SENTINEL,
        **kwargs,
    ):
        """DocumentCountAccountGroupGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[DocumentCountAccountGroupExpression], optional
        :param operator: operator
        :type operator: DocumentCountAccountGroupGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, DocumentCountAccountGroupExpression
            )
        self.operator = self._enum_matching(
            operator,
            DocumentCountAccountGroupGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
