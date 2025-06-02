
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .default_oftp_connection_settings import DefaultOftpConnectionSettings
from .oftp_partner_info import OftpPartnerInfo


@JsonMap(
    {
        "client_ssl_alias": "clientSSLAlias",
        "default_oftp_connection_settings": "defaultOFTPConnectionSettings",
        "my_partner_info": "myPartnerInfo",
        "use_client_ssl": "useClientSSL",
        "use_gateway": "useGateway",
    }
)
class OftpConnectionSettings(BaseModel):
    """OftpConnectionSettings

    :param client_ssl_alias: client_ssl_alias, defaults to None
    :type client_ssl_alias: str, optional
    :param default_oftp_connection_settings: default_oftp_connection_settings, defaults to None
    :type default_oftp_connection_settings: DefaultOftpConnectionSettings, optional
    :param host: host, defaults to None
    :type host: str, optional
    :param my_partner_info: my_partner_info
    :type my_partner_info: OftpPartnerInfo
    :param port: port, defaults to None
    :type port: int, optional
    :param sfidciph: sfidciph, defaults to None
    :type sfidciph: int, optional
    :param ssidauth: ssidauth, defaults to None
    :type ssidauth: bool, optional
    :param tls: tls, defaults to None
    :type tls: bool, optional
    :param use_client_ssl: use_client_ssl, defaults to None
    :type use_client_ssl: bool, optional
    :param use_gateway: use_gateway, defaults to None
    :type use_gateway: bool, optional
    """

    def __init__(
        self,
        my_partner_info: OftpPartnerInfo,
        client_ssl_alias: str = SENTINEL,
        default_oftp_connection_settings: DefaultOftpConnectionSettings = SENTINEL,
        host: str = SENTINEL,
        port: int = SENTINEL,
        sfidciph: int = SENTINEL,
        ssidauth: bool = SENTINEL,
        tls: bool = SENTINEL,
        use_client_ssl: bool = SENTINEL,
        use_gateway: bool = SENTINEL,
        **kwargs,
    ):
        """OftpConnectionSettings

        :param client_ssl_alias: client_ssl_alias, defaults to None
        :type client_ssl_alias: str, optional
        :param default_oftp_connection_settings: default_oftp_connection_settings, defaults to None
        :type default_oftp_connection_settings: DefaultOftpConnectionSettings, optional
        :param host: host, defaults to None
        :type host: str, optional
        :param my_partner_info: my_partner_info
        :type my_partner_info: OftpPartnerInfo
        :param port: port, defaults to None
        :type port: int, optional
        :param sfidciph: sfidciph, defaults to None
        :type sfidciph: int, optional
        :param ssidauth: ssidauth, defaults to None
        :type ssidauth: bool, optional
        :param tls: tls, defaults to None
        :type tls: bool, optional
        :param use_client_ssl: use_client_ssl, defaults to None
        :type use_client_ssl: bool, optional
        :param use_gateway: use_gateway, defaults to None
        :type use_gateway: bool, optional
        """
        if client_ssl_alias is not SENTINEL:
            self.client_ssl_alias = client_ssl_alias
        if default_oftp_connection_settings is not SENTINEL:
            self.default_oftp_connection_settings = self._define_object(
                default_oftp_connection_settings, DefaultOftpConnectionSettings
            )
        if host is not SENTINEL:
            self.host = host
        self.my_partner_info = self._define_object(my_partner_info, OftpPartnerInfo)
        if port is not SENTINEL:
            self.port = port
        if sfidciph is not SENTINEL:
            self.sfidciph = sfidciph
        if ssidauth is not SENTINEL:
            self.ssidauth = ssidauth
        if tls is not SENTINEL:
            self.tls = tls
        if use_client_ssl is not SENTINEL:
            self.use_client_ssl = use_client_ssl
        if use_gateway is not SENTINEL:
            self.use_gateway = use_gateway
        self._kwargs = kwargs
