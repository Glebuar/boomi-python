
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .as2_basic_auth_info import As2BasicAuthInfo
from .private_certificate import PrivateCertificate
from .public_certificate import PublicCertificate


class As2SendSettingsAuthenticationType(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "NONE"
    :vartype NONE: str
    :cvar BASIC: "BASIC"
    :vartype BASIC: str
    """

    NONE = "NONE"
    BASIC = "BASIC"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                As2SendSettingsAuthenticationType._member_map_.values(),
            )
        )


@JsonMap(
    {
        "auth_settings": "AuthSettings",
        "authentication_type": "authenticationType",
        "client_ssl_certificate": "clientSSLCertificate",
        "ssl_certificate": "sslCertificate",
        "use_default_settings": "useDefaultSettings",
        "verify_hostname": "verifyHostname",
    }
)
class As2SendSettings(BaseModel):
    """As2SendSettings

    :param auth_settings: auth_settings, defaults to None
    :type auth_settings: As2BasicAuthInfo, optional
    :param authentication_type: authentication_type, defaults to None
    :type authentication_type: As2SendSettingsAuthenticationType, optional
    :param client_ssl_certificate: client_ssl_certificate
    :type client_ssl_certificate: PrivateCertificate
    :param ssl_certificate: ssl_certificate
    :type ssl_certificate: PublicCertificate
    :param url: url
    :type url: str
    :param use_default_settings: use_default_settings, defaults to None
    :type use_default_settings: bool, optional
    :param verify_hostname: verify_hostname, defaults to None
    :type verify_hostname: bool, optional
    """

    def __init__(
        self,
        client_ssl_certificate: PrivateCertificate,
        ssl_certificate: PublicCertificate,
        url: str,
        auth_settings: As2BasicAuthInfo = SENTINEL,
        authentication_type: As2SendSettingsAuthenticationType = SENTINEL,
        use_default_settings: bool = SENTINEL,
        verify_hostname: bool = SENTINEL,
        **kwargs,
    ):
        """As2SendSettings

        :param auth_settings: auth_settings, defaults to None
        :type auth_settings: As2BasicAuthInfo, optional
        :param authentication_type: authentication_type, defaults to None
        :type authentication_type: As2SendSettingsAuthenticationType, optional
        :param client_ssl_certificate: client_ssl_certificate
        :type client_ssl_certificate: PrivateCertificate
        :param ssl_certificate: ssl_certificate
        :type ssl_certificate: PublicCertificate
        :param url: url
        :type url: str
        :param use_default_settings: use_default_settings, defaults to None
        :type use_default_settings: bool, optional
        :param verify_hostname: verify_hostname, defaults to None
        :type verify_hostname: bool, optional
        """
        if auth_settings is not SENTINEL:
            self.auth_settings = self._define_object(auth_settings, As2BasicAuthInfo)
        if authentication_type is not SENTINEL:
            self.authentication_type = self._enum_matching(
                authentication_type,
                As2SendSettingsAuthenticationType.list(),
                "authentication_type",
            )
        self.client_ssl_certificate = self._define_object(
            client_ssl_certificate, PrivateCertificate
        )
        self.ssl_certificate = self._define_object(ssl_certificate, PublicCertificate)
        self.url = url
        if use_default_settings is not SENTINEL:
            self.use_default_settings = use_default_settings
        if verify_hostname is not SENTINEL:
            self.verify_hostname = verify_hostname
        self._kwargs = kwargs
