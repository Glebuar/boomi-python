
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class InstallType(Enum):
    """An enumeration representing different categories.

    :cvar CLOUD: "CLOUD"
    :vartype CLOUD: str
    :cvar ATOM: "ATOM"
    :vartype ATOM: str
    :cvar MOLECULE: "MOLECULE"
    :vartype MOLECULE: str
    :cvar BROKER: "BROKER"
    :vartype BROKER: str
    :cvar GATEWAY: "GATEWAY"
    :vartype GATEWAY: str
    """

    CLOUD = "CLOUD"
    ATOM = "ATOM"
    MOLECULE = "MOLECULE"
    BROKER = "BROKER"
    GATEWAY = "GATEWAY"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, InstallType._member_map_.values()))


@JsonMap(
    {
        "account_id": "accountId",
        "cloud_id": "cloudId",
        "duration_minutes": "durationMinutes",
        "install_type": "installType",
    }
)
class InstallerToken(BaseModel):
    """InstallerToken

    :param account_id: account_id, defaults to None
    :type account_id: str, optional
    :param cloud_id: \(For Runtime cloud installation\) A unique ID assigned by the system to the Runtime cloud., defaults to None
    :type cloud_id: str, optional
    :param created: created, defaults to None
    :type created: str, optional
    :param duration_minutes: The number of minutes for which the installer token is valid, from 30 to 1440., defaults to None
    :type duration_minutes: int, optional
    :param expiration: expiration, defaults to None
    :type expiration: str, optional
    :param install_type: -   ATOM\<br /\>-   MOLECULE\<br /\>-   CLOUD\<br /\>-   BROKER, defaults to None
    :type install_type: InstallType, optional
    :param token: token, defaults to None
    :type token: str, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        cloud_id: str = SENTINEL,
        created: str = SENTINEL,
        duration_minutes: int = SENTINEL,
        expiration: str = SENTINEL,
        install_type: InstallType = SENTINEL,
        token: str = SENTINEL,
        **kwargs
    ):
        """InstallerToken

        :param account_id: account_id, defaults to None
        :type account_id: str, optional
        :param cloud_id: \(For Runtime cloud installation\) A unique ID assigned by the system to the Runtime cloud., defaults to None
        :type cloud_id: str, optional
        :param created: created, defaults to None
        :type created: str, optional
        :param duration_minutes: The number of minutes for which the installer token is valid, from 30 to 1440., defaults to None
        :type duration_minutes: int, optional
        :param expiration: expiration, defaults to None
        :type expiration: str, optional
        :param install_type: -   ATOM\<br /\>-   MOLECULE\<br /\>-   CLOUD\<br /\>-   BROKER, defaults to None
        :type install_type: InstallType, optional
        :param token: token, defaults to None
        :type token: str, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if cloud_id is not SENTINEL:
            self.cloud_id = cloud_id
        if created is not SENTINEL:
            self.created = created
        if duration_minutes is not SENTINEL:
            self.duration_minutes = duration_minutes
        if expiration is not SENTINEL:
            self.expiration = expiration
        if install_type is not SENTINEL:
            self.install_type = self._enum_matching(
                install_type, InstallType.list(), "install_type"
            )
        if token is not SENTINEL:
            self.token = token
        self._kwargs = kwargs
