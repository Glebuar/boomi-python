
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .document_count_account_expression import DocumentCountAccountExpression, DocumentCountAccountExpressionGuard
from .document_count_account_simple_expression import (
    DocumentCountAccountSimpleExpression,
)

class DocumentCountAccountGroupingExpressionOperator(Enum):
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
                DocumentCountAccountGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class DocumentCountAccountGroupingExpression(BaseModel):
    """DocumentCountAccountGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[DocumentCountAccountExpression], optional
    :param operator: operator
    :type operator: DocumentCountAccountGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: DocumentCountAccountGroupingExpressionOperator,
        nested_expression: List[DocumentCountAccountExpression] = SENTINEL,
        **kwargs,
    ):
        """DocumentCountAccountGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[DocumentCountAccountExpression], optional
        :param operator: operator
        :type operator: DocumentCountAccountGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, DocumentCountAccountExpression
            )
        self.operator = self._enum_matching(
            operator, DocumentCountAccountGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
