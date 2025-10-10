
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ComponentMetadataSimpleExpressionOperator(Enum):
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
                ComponentMetadataSimpleExpressionOperator._member_map_.values(),
            )
        )


class ComponentMetadataSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar ACCOUNTID: "accountId"
    :vartype ACCOUNTID: str
    :cvar COMPONENTID: "componentId"
    :vartype COMPONENTID: str
    :cvar VERSION: "version"
    :vartype VERSION: str
    :cvar NAME: "name"
    :vartype NAME: str
    :cvar TYPE: "type"
    :vartype TYPE: str
    :cvar SUBTYPE: "subType"
    :vartype SUBTYPE: str
    :cvar CREATEDDATE: "createdDate"
    :vartype CREATEDDATE: str
    :cvar CREATEDBY: "createdBy"
    :vartype CREATEDBY: str
    :cvar MODIFIEDDATE: "modifiedDate"
    :vartype MODIFIEDDATE: str
    :cvar MODIFIEDBY: "modifiedBy"
    :vartype MODIFIEDBY: str
    :cvar DELETED: "deleted"
    :vartype DELETED: str
    :cvar CURRENTVERSION: "currentVersion"
    :vartype CURRENTVERSION: str
    :cvar FOLDERNAME: "folderName"
    :vartype FOLDERNAME: str
    :cvar FOLDERID: "folderId"
    :vartype FOLDERID: str
    :cvar COPIEDFROMCOMPONENTID: "copiedFromComponentId"
    :vartype COPIEDFROMCOMPONENTID: str
    :cvar COPIEDFROMCOMPONENTVERSION: "copiedFromComponentVersion"
    :vartype COPIEDFROMCOMPONENTVERSION: str
    :cvar BRANCHNAME: "branchName"
    :vartype BRANCHNAME: str
    :cvar BRANCHID: "branchId"
    :vartype BRANCHID: str
    """

    ACCOUNTID = "accountId"
    COMPONENTID = "componentId"
    VERSION = "version"
    NAME = "name"
    TYPE = "type"
    SUBTYPE = "subType"
    CREATEDDATE = "createdDate"
    CREATEDBY = "createdBy"
    MODIFIEDDATE = "modifiedDate"
    MODIFIEDBY = "modifiedBy"
    DELETED = "deleted"
    CURRENTVERSION = "currentVersion"
    FOLDERNAME = "folderName"
    FOLDERID = "folderId"
    COPIEDFROMCOMPONENTID = "copiedFromComponentId"
    COPIEDFROMCOMPONENTVERSION = "copiedFromComponentVersion"
    BRANCHNAME = "branchName"
    BRANCHID = "branchId"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                ComponentMetadataSimpleExpressionProperty._member_map_.values(),
            )
        )


@JsonMap({})
class ComponentMetadataSimpleExpression(BaseModel):
    """ComponentMetadataSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: ComponentMetadataSimpleExpressionOperator
    :param property: property
    :type property: ComponentMetadataSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: ComponentMetadataSimpleExpressionOperator,
        property: ComponentMetadataSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """ComponentMetadataSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: ComponentMetadataSimpleExpressionOperator
        :param property: property
        :type property: ComponentMetadataSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, ComponentMetadataSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, ComponentMetadataSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
