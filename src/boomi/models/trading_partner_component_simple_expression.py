
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class TradingPartnerComponentSimpleExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar EQUALS: "EQUALS"
    :vartype EQUALS: str
    :cvar LIKE: "LIKE"
    :vartype LIKE: str
    :cvar NOTEQUALS: "NOT_EQUALS"
    :vartype NOTEQUALS: str
    :cvar ISNULL: "IS_NULL"
    :vartype ISNULL: str
    :cvar ISNOTNULL: "IS_NOT_NULL"
    :vartype ISNOTNULL: str
    :cvar BETWEEN: "BETWEEN"
    :vartype BETWEEN: str
    :cvar GREATERTHAN: "GREATER_THAN"
    :vartype GREATERTHAN: str
    :cvar GREATERTHANOREQUAL: "GREATER_THAN_OR_EQUAL"
    :vartype GREATERTHANOREQUAL: str
    :cvar LESSTHAN: "LESS_THAN"
    :vartype LESSTHAN: str
    :cvar LESSTHANOREQUAL: "LESS_THAN_OR_EQUAL"
    :vartype LESSTHANOREQUAL: str
    :cvar CONTAINS: "CONTAINS"
    :vartype CONTAINS: str
    :cvar NOTCONTAINS: "NOT_CONTAINS"
    :vartype NOTCONTAINS: str
    """

    EQUALS = "EQUALS"
    LIKE = "LIKE"
    NOTEQUALS = "NOT_EQUALS"
    ISNULL = "IS_NULL"
    ISNOTNULL = "IS_NOT_NULL"
    BETWEEN = "BETWEEN"
    GREATERTHAN = "GREATER_THAN"
    GREATERTHANOREQUAL = "GREATER_THAN_OR_EQUAL"
    LESSTHAN = "LESS_THAN"
    LESSTHANOREQUAL = "LESS_THAN_OR_EQUAL"
    CONTAINS = "CONTAINS"
    NOTCONTAINS = "NOT_CONTAINS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                TradingPartnerComponentSimpleExpressionOperator._member_map_.values(),
            )
        )


class TradingPartnerComponentSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar NAME: "name"
    :vartype NAME: str
    :cvar CLASSIFICATION: "classification"
    :vartype CLASSIFICATION: str
    :cvar STANDARD: "standard"
    :vartype STANDARD: str
    :cvar IDENTIFIER: "identifier"
    :vartype IDENTIFIER: str
    :cvar AS2: "as2"
    :vartype AS2: str
    :cvar DISK: "disk"
    :vartype DISK: str
    :cvar FTP: "ftp"
    :vartype FTP: str
    :cvar MLLP: "mllp"
    :vartype MLLP: str
    :cvar SFTP: "sftp"
    :vartype SFTP: str
    :cvar HTTP: "http"
    :vartype HTTP: str
    :cvar OFTP: "oftp"
    :vartype OFTP: str
    """

    NAME = "name"
    CLASSIFICATION = "classification"
    STANDARD = "standard"
    IDENTIFIER = "identifier"
    AS2 = "as2"
    DISK = "disk"
    FTP = "ftp"
    MLLP = "mllp"
    SFTP = "sftp"
    HTTP = "http"
    OFTP = "oftp"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                TradingPartnerComponentSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class TradingPartnerComponentSimpleExpression(BaseModel):
    """TradingPartnerComponentSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: TradingPartnerComponentSimpleExpressionOperator
    :param property: property
    :type property: TradingPartnerComponentSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: TradingPartnerComponentSimpleExpressionOperator,
        property: TradingPartnerComponentSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """TradingPartnerComponentSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: TradingPartnerComponentSimpleExpressionOperator
        :param property: property
        :type property: TradingPartnerComponentSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, TradingPartnerComponentSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, TradingPartnerComponentSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
