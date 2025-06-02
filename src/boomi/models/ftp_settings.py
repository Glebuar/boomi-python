
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .ftpssl_options import FtpsslOptions


class ConnectionMode(Enum):
    """An enumeration representing different categories.

    :cvar ACTIVE: "active"
    :vartype ACTIVE: str
    :cvar PASSIVE: "passive"
    :vartype PASSIVE: str
    """

    ACTIVE = "active"
    PASSIVE = "passive"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ConnectionMode._member_map_.values()))


@JsonMap(
    {
        "ftpssl_options": "FTPSSLOptions",
        "connection_mode": "connectionMode",
        "use_default_settings": "useDefaultSettings",
    }
)
class FtpSettings(BaseModel):
    """FtpSettings

    :param ftpssl_options: ftpssl_options
    :type ftpssl_options: FtpsslOptions
    :param connection_mode: connection_mode, defaults to None
    :type connection_mode: ConnectionMode, optional
    :param host: host
    :type host: str
    :param password: password
    :type password: str
    :param port: port
    :type port: int
    :param use_default_settings: use_default_settings, defaults to None
    :type use_default_settings: bool, optional
    :param user: user
    :type user: str
    """

    def __init__(
        self,
        ftpssl_options: FtpsslOptions,
        host: str,
        password: str,
        port: int,
        user: str,
        connection_mode: ConnectionMode = SENTINEL,
        use_default_settings: bool = SENTINEL,
        **kwargs,
    ):
        """FtpSettings

        :param ftpssl_options: ftpssl_options
        :type ftpssl_options: FtpsslOptions
        :param connection_mode: connection_mode, defaults to None
        :type connection_mode: ConnectionMode, optional
        :param host: host
        :type host: str
        :param password: password
        :type password: str
        :param port: port
        :type port: int
        :param use_default_settings: use_default_settings, defaults to None
        :type use_default_settings: bool, optional
        :param user: user
        :type user: str
        """
        self.ftpssl_options = self._define_object(ftpssl_options, FtpsslOptions)
        if connection_mode is not SENTINEL:
            self.connection_mode = self._enum_matching(
                connection_mode, ConnectionMode.list(), "connection_mode"
            )
        self.host = host
        self.password = password
        self.port = port
        if use_default_settings is not SENTINEL:
            self.use_default_settings = use_default_settings
        self.user = user
        self._kwargs = kwargs
