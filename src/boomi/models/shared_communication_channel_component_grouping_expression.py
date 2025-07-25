
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .shared_communication_channel_component_expression import SharedCommunicationChannelComponentExpression, SharedCommunicationChannelComponentExpressionGuard
from .shared_communication_channel_component_simple_expression import (
    SharedCommunicationChannelComponentSimpleExpression,
)

class SharedCommunicationChannelComponentGroupingExpressionOperator(Enum):
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
                SharedCommunicationChannelComponentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class SharedCommunicationChannelComponentGroupingExpression(BaseModel):
    """SharedCommunicationChannelComponentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[SharedCommunicationChannelComponentExpression], optional
    :param operator: operator
    :type operator: SharedCommunicationChannelComponentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: SharedCommunicationChannelComponentGroupingExpressionOperator,
        nested_expression: List[
            SharedCommunicationChannelComponentExpression
        ] = SENTINEL,
        **kwargs,
    ):
        """SharedCommunicationChannelComponentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[SharedCommunicationChannelComponentExpression], optional
        :param operator: operator
        :type operator: SharedCommunicationChannelComponentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, SharedCommunicationChannelComponentExpression
            )
        self.operator = self._enum_matching(
            operator,
            SharedCommunicationChannelComponentGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
