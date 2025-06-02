
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class DeployedExpiredCertificateSimpleExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar LESSTHANOREQUAL: "LESS_THAN_OR_EQUAL"
    :vartype LESSTHANOREQUAL: str
    """

    LESSTHANOREQUAL = "LESS_THAN_OR_EQUAL"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                DeployedExpiredCertificateSimpleExpressionOperator._member_map_.values(),
            )
        )


class DeployedExpiredCertificateSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar CONTAINERID: "containerId"
    :vartype CONTAINERID: str
    :cvar CONTAINERNAME: "containerName"
    :vartype CONTAINERNAME: str
    :cvar ENVIRONMENTID: "environmentId"
    :vartype ENVIRONMENTID: str
    :cvar ENVIRONMENTNAME: "environmentName"
    :vartype ENVIRONMENTNAME: str
    :cvar EXPIRATIONBOUNDARY: "expirationBoundary"
    :vartype EXPIRATIONBOUNDARY: str
    """

    CONTAINERID = "containerId"
    CONTAINERNAME = "containerName"
    ENVIRONMENTID = "environmentId"
    ENVIRONMENTNAME = "environmentName"
    EXPIRATIONBOUNDARY = "expirationBoundary"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                DeployedExpiredCertificateSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class DeployedExpiredCertificateSimpleExpression(BaseModel):
    """DeployedExpiredCertificateSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: DeployedExpiredCertificateSimpleExpressionOperator
    :param property: property
    :type property: DeployedExpiredCertificateSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: DeployedExpiredCertificateSimpleExpressionOperator,
        property: DeployedExpiredCertificateSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """DeployedExpiredCertificateSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: DeployedExpiredCertificateSimpleExpressionOperator
        :param property: property
        :type property: DeployedExpiredCertificateSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator,
            DeployedExpiredCertificateSimpleExpressionOperator.list(),
            "operator",
        )
        self.property = self._enum_matching(
            property,
            DeployedExpiredCertificateSimpleExpressionProperty.list(),
            "property",
        )
        self._kwargs = kwargs
