
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .resources import Resources


class AutoSubscribeAlertLevel(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "none"
    :vartype NONE: str
    :cvar INFO: "info"
    :vartype INFO: str
    :cvar WARNING: "warning"
    :vartype WARNING: str
    :cvar ERROR: "error"
    :vartype ERROR: str
    """

    NONE = "none"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, AutoSubscribeAlertLevel._member_map_.values())
        )


@JsonMap(
    {
        "resources": "Resources",
        "account_id": "accountId",
        "auto_subscribe_alert_level": "autoSubscribeAlertLevel",
        "default_group": "defaultGroup",
        "id_": "id",
    }
)
class AccountGroup(BaseModel):
    """AccountGroup

    :param resources: resources, defaults to None
    :type resources: Resources, optional
    :param account_id: The ID of the primary account under which the account group exists., defaults to None
    :type account_id: str, optional
    :param auto_subscribe_alert_level: The severity level of email alerts sent to member users in the account group., defaults to None
    :type auto_subscribe_alert_level: AutoSubscribeAlertLevel, optional
    :param default_group: true — The account group is All Accounts, which the system creates automatically.\<br /\> false — The account group is not All Accounts., defaults to None
    :type default_group: bool, optional
    :param id_: The ID of the account group., defaults to None
    :type id_: str, optional
    :param name: The name of the account group as displayed on the **Account Information** tab of the **Setup** page., defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        resources: Resources = SENTINEL,
        account_id: str = SENTINEL,
        auto_subscribe_alert_level: AutoSubscribeAlertLevel = SENTINEL,
        default_group: bool = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        **kwargs,
    ):
        """AccountGroup

        :param resources: resources, defaults to None
        :type resources: Resources, optional
        :param account_id: The ID of the primary account under which the account group exists., defaults to None
        :type account_id: str, optional
        :param auto_subscribe_alert_level: The severity level of email alerts sent to member users in the account group., defaults to None
        :type auto_subscribe_alert_level: AutoSubscribeAlertLevel, optional
        :param default_group: true — The account group is All Accounts, which the system creates automatically.\<br /\> false — The account group is not All Accounts., defaults to None
        :type default_group: bool, optional
        :param id_: The ID of the account group., defaults to None
        :type id_: str, optional
        :param name: The name of the account group as displayed on the **Account Information** tab of the **Setup** page., defaults to None
        :type name: str, optional
        """
        if resources is not SENTINEL:
            self.resources = self._define_object(resources, Resources)
        if account_id is not SENTINEL:
            self.account_id = account_id
        if auto_subscribe_alert_level is not SENTINEL:
            self.auto_subscribe_alert_level = self._enum_matching(
                auto_subscribe_alert_level,
                AutoSubscribeAlertLevel.list(),
                "auto_subscribe_alert_level",
            )
        if default_group is not SENTINEL:
            self.default_group = default_group
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
