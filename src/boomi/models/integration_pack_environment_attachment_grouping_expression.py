
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .integration_pack_environment_attachment_expression import IntegrationPackEnvironmentAttachmentExpression, IntegrationPackEnvironmentAttachmentExpressionGuard
from .integration_pack_environment_attachment_simple_expression import (
    IntegrationPackEnvironmentAttachmentSimpleExpression,
)

class IntegrationPackEnvironmentAttachmentGroupingExpressionOperator(Enum):
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
                IntegrationPackEnvironmentAttachmentGroupingExpressionOperator._member_map_.values(),
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class IntegrationPackEnvironmentAttachmentGroupingExpression(BaseModel):
    """IntegrationPackEnvironmentAttachmentGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[IntegrationPackEnvironmentAttachmentExpression], optional
    :param operator: operator
    :type operator: IntegrationPackEnvironmentAttachmentGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: IntegrationPackEnvironmentAttachmentGroupingExpressionOperator,
        nested_expression: List[
            IntegrationPackEnvironmentAttachmentExpression
        ] = SENTINEL,
        **kwargs,
    ):
        """IntegrationPackEnvironmentAttachmentGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[IntegrationPackEnvironmentAttachmentExpression], optional
        :param operator: operator
        :type operator: IntegrationPackEnvironmentAttachmentGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:
            self.nested_expression = self._define_list(
                nested_expression, IntegrationPackEnvironmentAttachmentExpression
            )
        self.operator = self._enum_matching(
            operator,
            IntegrationPackEnvironmentAttachmentGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
