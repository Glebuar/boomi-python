
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class AtomSimpleExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar EQUALS: "EQUALS"
    :vartype EQUALS: str
    :cvar NOTEQUALS: "NOT_EQUALS"
    :vartype NOTEQUALS: str
    :cvar CONTAINS: "CONTAINS"
    :vartype CONTAINS: str
    :cvar NOTCONTAINS: "NOT_CONTAINS"
    :vartype NOTCONTAINS: str
    """

    EQUALS = "EQUALS"
    NOTEQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOTCONTAINS = "NOT_CONTAINS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, AtomSimpleExpressionOperator._member_map_.values())
        )


class AtomSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar NAME: "name"
    :vartype NAME: str
    :cvar ID: "id"
    :vartype ID: str
    :cvar HOSTNAME: "hostname"
    :vartype HOSTNAME: str
    :cvar STATUS: "status"
    :vartype STATUS: str
    :cvar TYPE: "type"
    :vartype TYPE: str
    :cvar CAPABILITIES: "capabilities"
    :vartype CAPABILITIES: str
    """

    NAME = "name"
    ID = "id"
    HOSTNAME = "hostname"
    STATUS = "status"
    TYPE = "type"
    CAPABILITIES = "capabilities"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, AtomSimpleExpressionProperty._member_map_.values())
        )


@JsonMap({})
class AtomSimpleExpression(BaseModel):
    """AtomSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: AtomSimpleExpressionOperator
    :param property: property
    :type property: AtomSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: AtomSimpleExpressionOperator,
        property: AtomSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """AtomSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: AtomSimpleExpressionOperator
        :param property: property
        :type property: AtomSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, AtomSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, AtomSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
