
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .connector_expression import ConnectorExpression, ConnectorExpressionGuard
from .connector_simple_expression import ConnectorSimpleExpression

class ConnectorGroupingExpressionOperator(Enum):
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
                ConnectorGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class ConnectorGroupingExpression(BaseModel):
    """ConnectorGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["ConnectorExpression"], optional
    :param operator: operator
    :type operator: ConnectorGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: ConnectorGroupingExpressionOperator,
        nested_expression: List["ConnectorExpression"] = SENTINEL,
        **kwargs,
    ):
        """ConnectorGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["ConnectorExpression"], optional
        :param operator: operator
        :type operator: ConnectorGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .connector_expression import ConnectorExpression

            self.nested_expression = self._define_list(
                nested_expression, ConnectorExpression
            )
        self.operator = self._enum_matching(
            operator, ConnectorGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
