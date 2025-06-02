
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .private_certificate import PrivateCertificate


class Sslmode(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "none"
    :vartype NONE: str
    :cvar EXPLICIT: "explicit"
    :vartype EXPLICIT: str
    :cvar IMPLICIT: "implicit"
    :vartype IMPLICIT: str
    """

    NONE = "none"
    EXPLICIT = "explicit"
    IMPLICIT = "implicit"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Sslmode._member_map_.values()))


@JsonMap(
    {
        "client_ssl_certificate": "clientSSLCertificate",
        "use_client_authentication": "useClientAuthentication",
    }
)
class FtpsslOptions(BaseModel):
    """FtpsslOptions

    :param client_ssl_certificate: client_ssl_certificate
    :type client_ssl_certificate: PrivateCertificate
    :param sslmode: sslmode, defaults to None
    :type sslmode: Sslmode, optional
    :param use_client_authentication: use_client_authentication, defaults to None
    :type use_client_authentication: bool, optional
    """

    def __init__(
        self,
        client_ssl_certificate: PrivateCertificate,
        sslmode: Sslmode = SENTINEL,
        use_client_authentication: bool = SENTINEL,
        **kwargs,
    ):
        """FtpsslOptions

        :param client_ssl_certificate: client_ssl_certificate
        :type client_ssl_certificate: PrivateCertificate
        :param sslmode: sslmode, defaults to None
        :type sslmode: Sslmode, optional
        :param use_client_authentication: use_client_authentication, defaults to None
        :type use_client_authentication: bool, optional
        """
        self.client_ssl_certificate = self._define_object(
            client_ssl_certificate, PrivateCertificate
        )
        if sslmode is not SENTINEL:
            self.sslmode = self._enum_matching(sslmode, Sslmode.list(), "sslmode")
        if use_client_authentication is not SENTINEL:
            self.use_client_authentication = use_client_authentication
        self._kwargs = kwargs
