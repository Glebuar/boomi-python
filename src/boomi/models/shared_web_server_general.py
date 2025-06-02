
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_authentication import SharedWebServerAuthentication
from .listener_port_configuration import ListenerPortConfiguration
from .shared_web_server_protected_headers import SharedWebServerProtectedHeaders


@JsonMap(
    {
        "api_type": "apiType",
        "base_url": "baseUrl",
        "examine_forward_headers": "examineForwardHeaders",
        "external_host": "externalHost",
        "internal_host": "internalHost",
        "listener_ports": "listenerPorts",
        "max_number_of_threads": "maxNumberOfThreads",
        "override_url": "overrideUrl",
        "protected_headers": "protectedHeaders",
        "ssl_certificate": "sslCertificate",
    }
)
class SharedWebServerGeneral(BaseModel):
    """SharedWebServerGeneral

    :param api_type: api_type
    :type api_type: str
    :param authentication: authentication
    :type authentication: SharedWebServerAuthentication
    :param base_url: base_url
    :type base_url: str
    :param examine_forward_headers: examine_forward_headers, defaults to None
    :type examine_forward_headers: bool, optional
    :param external_host: external_host
    :type external_host: str
    :param internal_host: internal_host
    :type internal_host: str
    :param listener_ports: listener_ports
    :type listener_ports: ListenerPortConfiguration
    :param max_number_of_threads: max_number_of_threads, defaults to None
    :type max_number_of_threads: int, optional
    :param override_url: override_url, defaults to None
    :type override_url: bool, optional
    :param protected_headers: protected_headers
    :type protected_headers: SharedWebServerProtectedHeaders
    :param ssl_certificate: ssl_certificate
    :type ssl_certificate: str
    """

    def __init__(
        self,
        api_type: str,
        authentication: SharedWebServerAuthentication,
        base_url: str,
        external_host: str,
        internal_host: str,
        listener_ports: ListenerPortConfiguration,
        protected_headers: SharedWebServerProtectedHeaders,
        ssl_certificate: str,
        examine_forward_headers: bool = SENTINEL,
        max_number_of_threads: int = SENTINEL,
        override_url: bool = SENTINEL,
        **kwargs,
    ):
        """SharedWebServerGeneral

        :param api_type: api_type
        :type api_type: str
        :param authentication: authentication
        :type authentication: SharedWebServerAuthentication
        :param base_url: base_url
        :type base_url: str
        :param examine_forward_headers: examine_forward_headers, defaults to None
        :type examine_forward_headers: bool, optional
        :param external_host: external_host
        :type external_host: str
        :param internal_host: internal_host
        :type internal_host: str
        :param listener_ports: listener_ports
        :type listener_ports: ListenerPortConfiguration
        :param max_number_of_threads: max_number_of_threads, defaults to None
        :type max_number_of_threads: int, optional
        :param override_url: override_url, defaults to None
        :type override_url: bool, optional
        :param protected_headers: protected_headers
        :type protected_headers: SharedWebServerProtectedHeaders
        :param ssl_certificate: ssl_certificate
        :type ssl_certificate: str
        """
        self.api_type = api_type
        self.authentication = self._define_object(
            authentication, SharedWebServerAuthentication
        )
        self.base_url = base_url
        if examine_forward_headers is not SENTINEL:
            self.examine_forward_headers = examine_forward_headers
        self.external_host = external_host
        self.internal_host = internal_host
        self.listener_ports = self._define_object(
            listener_ports, ListenerPortConfiguration
        )
        if max_number_of_threads is not SENTINEL:
            self.max_number_of_threads = max_number_of_threads
        if override_url is not SENTINEL:
            self.override_url = override_url
        self.protected_headers = self._define_object(
            protected_headers, SharedWebServerProtectedHeaders
        )
        self.ssl_certificate = ssl_certificate
        self._kwargs = kwargs
