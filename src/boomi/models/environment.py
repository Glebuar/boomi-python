
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class EnvironmentClassification(Enum):
    """An enumeration representing different categories.

    :cvar PROD: "PROD"
    :vartype PROD: str
    :cvar TEST: "TEST"
    :vartype TEST: str
    """

    PROD = "PROD"
    TEST = "TEST"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, EnvironmentClassification._member_map_.values())
        )


@JsonMap(
    {
        "id_": "id",
        "parent_account": "parentAccount",
        "parent_environment": "parentEnvironment",
    }
)
class Environment(BaseModel):
    """Environment

    :param classification: \(Optional\) For accounts with Unlimited environment support, the type of environment.The choices are PROD \(Production\) and TEST. The environment classification determines the type of license used when deploying a process to the environment. The default classification is PROD.\<br /\>You can assign the value TEST only if the requesting account has Test Connection Licensing enabled.\<br /\>You can set the classification only when you add an environment. You cannot change the classification later.\<br /\>Environments added prior to the January 2014 release have their classification set to PROD.   \>**Note:** The classification field is invalid for requests from accounts with Basic environment support because all environments are production environments., defaults to None
    :type classification: EnvironmentClassification, optional
    :param id_: A unique ID assigned by the system to the environment., defaults to None
    :type id_: str, optional
    :param name: A user-defined name for the environment., defaults to None
    :type name: str, optional
    :param parent_account: parent_account, defaults to None
    :type parent_account: str, optional
    :param parent_environment: parent_environment, defaults to None
    :type parent_environment: str, optional
    """

    def __init__(
        self,
        classification: EnvironmentClassification = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        parent_account: str = SENTINEL,
        parent_environment: str = SENTINEL,
        **kwargs
    ):
        """Environment

        :param classification: \(Optional\) For accounts with Unlimited environment support, the type of environment.The choices are PROD \(Production\) and TEST. The environment classification determines the type of license used when deploying a process to the environment. The default classification is PROD.\<br /\>You can assign the value TEST only if the requesting account has Test Connection Licensing enabled.\<br /\>You can set the classification only when you add an environment. You cannot change the classification later.\<br /\>Environments added prior to the January 2014 release have their classification set to PROD.   \>**Note:** The classification field is invalid for requests from accounts with Basic environment support because all environments are production environments., defaults to None
        :type classification: EnvironmentClassification, optional
        :param id_: A unique ID assigned by the system to the environment., defaults to None
        :type id_: str, optional
        :param name: A user-defined name for the environment., defaults to None
        :type name: str, optional
        :param parent_account: parent_account, defaults to None
        :type parent_account: str, optional
        :param parent_environment: parent_environment, defaults to None
        :type parent_environment: str, optional
        """
        if classification is not SENTINEL:
            self.classification = self._enum_matching(
                classification, EnvironmentClassification.list(), "classification"
            )
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        if parent_account is not SENTINEL:
            self.parent_account = parent_account
        if parent_environment is not SENTINEL:
            self.parent_environment = parent_environment
        self._kwargs = kwargs
