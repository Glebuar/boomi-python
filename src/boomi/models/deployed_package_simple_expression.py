
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class DeployedPackageSimpleExpressionOperator(Enum):
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
                DeployedPackageSimpleExpressionOperator._member_map_.values(),
            )
        )


class DeployedPackageSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar UID: "uid"
    :vartype UID: str
    :cvar NOTES: "notes"
    :vartype NOTES: str
    :cvar CURRENT: "current"
    :vartype CURRENT: str
    :cvar PACKAGENOTES: "packageNotes"
    :vartype PACKAGENOTES: str
    :cvar ACTIVE: "active"
    :vartype ACTIVE: str
    :cvar COMPONENTID: "componentId"
    :vartype COMPONENTID: str
    :cvar COMPONENTVERSION: "componentVersion"
    :vartype COMPONENTVERSION: str
    :cvar COMPONENTNAME: "componentName"
    :vartype COMPONENTNAME: str
    :cvar COMPONENTTYPE: "componentType"
    :vartype COMPONENTTYPE: str
    :cvar DEPLOYEDBY: "deployedBy"
    :vartype DEPLOYEDBY: str
    :cvar DEPLOYEDDATE: "deployedDate"
    :vartype DEPLOYEDDATE: str
    :cvar DEPLOYMENTID: "deploymentId"
    :vartype DEPLOYMENTID: str
    :cvar ENVIRONMENTID: "environmentId"
    :vartype ENVIRONMENTID: str
    :cvar ENVIRONMENTNAME: "environmentName"
    :vartype ENVIRONMENTNAME: str
    :cvar PACKAGEID: "packageId"
    :vartype PACKAGEID: str
    :cvar PACKAGEVERSION: "packageVersion"
    :vartype PACKAGEVERSION: str
    :cvar VERSION: "version"
    :vartype VERSION: str
    :cvar ACCOUNTID: "accountId"
    :vartype ACCOUNTID: str
    :cvar BRANCH: "branch"
    :vartype BRANCH: str
    """

    UID = "uid"
    NOTES = "notes"
    CURRENT = "current"
    PACKAGENOTES = "packageNotes"
    ACTIVE = "active"
    COMPONENTID = "componentId"
    COMPONENTVERSION = "componentVersion"
    COMPONENTNAME = "componentName"
    COMPONENTTYPE = "componentType"
    DEPLOYEDBY = "deployedBy"
    DEPLOYEDDATE = "deployedDate"
    DEPLOYMENTID = "deploymentId"
    ENVIRONMENTID = "environmentId"
    ENVIRONMENTNAME = "environmentName"
    PACKAGEID = "packageId"
    PACKAGEVERSION = "packageVersion"
    VERSION = "version"
    ACCOUNTID = "accountId"
    BRANCH = "branch"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                DeployedPackageSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class DeployedPackageSimpleExpression(BaseModel):
    """DeployedPackageSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: DeployedPackageSimpleExpressionOperator
    :param property: property
    :type property: DeployedPackageSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: DeployedPackageSimpleExpressionOperator,
        property: DeployedPackageSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """DeployedPackageSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: DeployedPackageSimpleExpressionOperator
        :param property: property
        :type property: DeployedPackageSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, DeployedPackageSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, DeployedPackageSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
