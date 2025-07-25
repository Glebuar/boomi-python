
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .sftp_proxy_settings import SftpProxySettings
from .sftpssh_options import SftpsshOptions


@JsonMap(
    {
        "host": "host",
        "password": "password",
        "port": "port",
        "sftp_proxy_settings": "SFTPProxySettings",
        "sftpssh_options": "SFTPSSHOptions",
        "use_default_settings": "useDefaultSettings",
        "user": "user",
    }
)
class SftpSettings(BaseModel):
    """SftpSettings

    :param sftp_proxy_settings: sftp_proxy_settings
    :type sftp_proxy_settings: SftpProxySettings
    :param sftpssh_options: sftpssh_options
    :type sftpssh_options: SftpsshOptions
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
        sftp_proxy_settings: SftpProxySettings,
        sftpssh_options: SftpsshOptions,
        host: str,
        password: str,
        port: int,
        user: str,
        use_default_settings: bool = SENTINEL,
        **kwargs,
    ):
        """SftpSettings

        :param sftp_proxy_settings: sftp_proxy_settings
        :type sftp_proxy_settings: SftpProxySettings
        :param sftpssh_options: sftpssh_options
        :type sftpssh_options: SftpsshOptions
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
        self.sftp_proxy_settings = self._define_object(
            sftp_proxy_settings, SftpProxySettings
        )
        self.sftpssh_options = self._define_object(sftpssh_options, SftpsshOptions)
        self.host = host
        self.password = password
        self.port = port
        if use_default_settings is not SENTINEL:
            self.use_default_settings = use_default_settings
        self.user = user
        self._kwargs = kwargs
