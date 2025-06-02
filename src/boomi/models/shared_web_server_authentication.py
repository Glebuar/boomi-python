
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_login_module_configuration import (
    SharedWebServerLoginModuleConfiguration,
)


@JsonMap(
    {
        "auth_type": "authType",
        "cache_authentication_timeout": "cacheAuthenticationTimeout",
        "cache_authorization_credentials": "cacheAuthorizationCredentials",
        "client_certificate_header_name": "clientCertificateHeaderName",
        "login_module_class_name": "loginModuleClassName",
        "login_module_options": "loginModuleOptions",
    }
)
class SharedWebServerAuthentication(BaseModel):
    """SharedWebServerAuthentication

    :param auth_type: auth_type
    :type auth_type: str
    :param cache_authentication_timeout: cache_authentication_timeout, defaults to None
    :type cache_authentication_timeout: int, optional
    :param cache_authorization_credentials: cache_authorization_credentials, defaults to None
    :type cache_authorization_credentials: bool, optional
    :param client_certificate_header_name: client_certificate_header_name
    :type client_certificate_header_name: str
    :param login_module_class_name: login_module_class_name
    :type login_module_class_name: str
    :param login_module_options: login_module_options
    :type login_module_options: SharedWebServerLoginModuleConfiguration
    """

    def __init__(
        self,
        auth_type: str,
        client_certificate_header_name: str,
        login_module_class_name: str,
        login_module_options: SharedWebServerLoginModuleConfiguration,
        cache_authentication_timeout: int = SENTINEL,
        cache_authorization_credentials: bool = SENTINEL,
        **kwargs,
    ):
        """SharedWebServerAuthentication

        :param auth_type: auth_type
        :type auth_type: str
        :param cache_authentication_timeout: cache_authentication_timeout, defaults to None
        :type cache_authentication_timeout: int, optional
        :param cache_authorization_credentials: cache_authorization_credentials, defaults to None
        :type cache_authorization_credentials: bool, optional
        :param client_certificate_header_name: client_certificate_header_name
        :type client_certificate_header_name: str
        :param login_module_class_name: login_module_class_name
        :type login_module_class_name: str
        :param login_module_options: login_module_options
        :type login_module_options: SharedWebServerLoginModuleConfiguration
        """
        self.auth_type = auth_type
        if cache_authentication_timeout is not SENTINEL:
            self.cache_authentication_timeout = cache_authentication_timeout
        if cache_authorization_credentials is not SENTINEL:
            self.cache_authorization_credentials = cache_authorization_credentials
        self.client_certificate_header_name = client_certificate_header_name
        self.login_module_class_name = login_module_class_name
        self.login_module_options = self._define_object(
            login_module_options, SharedWebServerLoginModuleConfiguration
        )
        self._kwargs = kwargs
