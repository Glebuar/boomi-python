
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class SftpProxySettingsType(Enum):
    """An enumeration representing different categories.

    :cvar ATOM: "ATOM"
    :vartype ATOM: str
    :cvar HTTP: "HTTP"
    :vartype HTTP: str
    :cvar SOCKS4: "SOCKS4"
    :vartype SOCKS4: str
    :cvar SOCKS5: "SOCKS5"
    :vartype SOCKS5: str
    """

    ATOM = "ATOM"
    HTTP = "HTTP"
    SOCKS4 = "SOCKS4"
    SOCKS5 = "SOCKS5"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SftpProxySettingsType._member_map_.values()))


@JsonMap({"proxy_enabled": "proxyEnabled", "type_": "type"})
class SftpProxySettings(BaseModel):
    """SftpProxySettings

    :param host: host
    :type host: str
    :param password: password
    :type password: str
    :param port: port
    :type port: int
    :param proxy_enabled: proxy_enabled, defaults to None
    :type proxy_enabled: bool, optional
    :param type_: type_, defaults to None
    :type type_: SftpProxySettingsType, optional
    :param user: user
    :type user: str
    """

    def __init__(
        self,
        host: str,
        password: str,
        port: int,
        user: str,
        proxy_enabled: bool = SENTINEL,
        type_: SftpProxySettingsType = SENTINEL,
        **kwargs
    ):
        """SftpProxySettings

        :param host: host
        :type host: str
        :param password: password
        :type password: str
        :param port: port
        :type port: int
        :param proxy_enabled: proxy_enabled, defaults to None
        :type proxy_enabled: bool, optional
        :param type_: type_, defaults to None
        :type type_: SftpProxySettingsType, optional
        :param user: user
        :type user: str
        """
        self.host = host
        self.password = password
        self.port = port
        if proxy_enabled is not SENTINEL:
            self.proxy_enabled = proxy_enabled
        if type_ is not SENTINEL:
            self.type_ = self._enum_matching(
                type_, SftpProxySettingsType.list(), "type_"
            )
        self.user = user
        self._kwargs = kwargs
