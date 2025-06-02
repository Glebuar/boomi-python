
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .http_auth_settings import HttpAuthSettings
from .httpo_auth2_settings import HttpoAuth2Settings
from .httpo_auth_settings import HttpoAuthSettings
from .httpssl_options import HttpsslOptions


class HttpSettingsAuthenticationType(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "NONE"
    :vartype NONE: str
    :cvar BASIC: "BASIC"
    :vartype BASIC: str
    :cvar PASSWORDDIGEST: "PASSWORD_DIGEST"
    :vartype PASSWORDDIGEST: str
    :cvar CUSTOM: "CUSTOM"
    :vartype CUSTOM: str
    :cvar OAUTH: "OAUTH"
    :vartype OAUTH: str
    :cvar OAUTH2: "OAUTH2"
    :vartype OAUTH2: str
    """

    NONE = "NONE"
    BASIC = "BASIC"
    PASSWORDDIGEST = "PASSWORD_DIGEST"
    CUSTOM = "CUSTOM"
    OAUTH = "OAUTH"
    OAUTH2 = "OAUTH2"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, HttpSettingsAuthenticationType._member_map_.values())
        )


class CookieScope(Enum):
    """An enumeration representing different categories.

    :cvar IGNORED: "IGNORED"
    :vartype IGNORED: str
    :cvar GLOBAL: "GLOBAL"
    :vartype GLOBAL: str
    :cvar CONNECTORSHAPE: "CONNECTOR_SHAPE"
    :vartype CONNECTORSHAPE: str
    """

    IGNORED = "IGNORED"
    GLOBAL = "GLOBAL"
    CONNECTORSHAPE = "CONNECTOR_SHAPE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CookieScope._member_map_.values()))


@JsonMap(
    {
        "http_auth_settings": "HTTPAuthSettings",
        "httpo_auth2_settings": "HTTPOAuth2Settings",
        "httpo_auth_settings": "HTTPOAuthSettings",
        "httpssl_options": "HTTPSSLOptions",
        "authentication_type": "authenticationType",
        "connect_timeout": "connectTimeout",
        "cookie_scope": "cookieScope",
        "read_timeout": "readTimeout",
        "use_basic_auth": "useBasicAuth",
        "use_custom_auth": "useCustomAuth",
        "use_default_settings": "useDefaultSettings",
    }
)
class HttpSettings(BaseModel):
    """HttpSettings

    :param http_auth_settings: http_auth_settings
    :type http_auth_settings: HttpAuthSettings
    :param httpo_auth2_settings: httpo_auth2_settings, defaults to None
    :type httpo_auth2_settings: HttpoAuth2Settings, optional
    :param httpo_auth_settings: httpo_auth_settings, defaults to None
    :type httpo_auth_settings: HttpoAuthSettings, optional
    :param httpssl_options: httpssl_options
    :type httpssl_options: HttpsslOptions
    :param authentication_type: authentication_type, defaults to None
    :type authentication_type: HttpSettingsAuthenticationType, optional
    :param connect_timeout: connect_timeout, defaults to None
    :type connect_timeout: int, optional
    :param cookie_scope: cookie_scope, defaults to None
    :type cookie_scope: CookieScope, optional
    :param read_timeout: read_timeout, defaults to None
    :type read_timeout: int, optional
    :param url: url, defaults to None
    :type url: str, optional
    :param use_basic_auth: use_basic_auth, defaults to None
    :type use_basic_auth: bool, optional
    :param use_custom_auth: use_custom_auth, defaults to None
    :type use_custom_auth: bool, optional
    :param use_default_settings: use_default_settings, defaults to None
    :type use_default_settings: bool, optional
    """

    def __init__(
        self,
        http_auth_settings: HttpAuthSettings,
        httpssl_options: HttpsslOptions,
        httpo_auth2_settings: HttpoAuth2Settings = SENTINEL,
        httpo_auth_settings: HttpoAuthSettings = SENTINEL,
        authentication_type: HttpSettingsAuthenticationType = SENTINEL,
        connect_timeout: int = SENTINEL,
        cookie_scope: CookieScope = SENTINEL,
        read_timeout: int = SENTINEL,
        url: str = SENTINEL,
        use_basic_auth: bool = SENTINEL,
        use_custom_auth: bool = SENTINEL,
        use_default_settings: bool = SENTINEL,
        **kwargs,
    ):
        """HttpSettings

        :param http_auth_settings: http_auth_settings
        :type http_auth_settings: HttpAuthSettings
        :param httpo_auth2_settings: httpo_auth2_settings, defaults to None
        :type httpo_auth2_settings: HttpoAuth2Settings, optional
        :param httpo_auth_settings: httpo_auth_settings, defaults to None
        :type httpo_auth_settings: HttpoAuthSettings, optional
        :param httpssl_options: httpssl_options
        :type httpssl_options: HttpsslOptions
        :param authentication_type: authentication_type, defaults to None
        :type authentication_type: HttpSettingsAuthenticationType, optional
        :param connect_timeout: connect_timeout, defaults to None
        :type connect_timeout: int, optional
        :param cookie_scope: cookie_scope, defaults to None
        :type cookie_scope: CookieScope, optional
        :param read_timeout: read_timeout, defaults to None
        :type read_timeout: int, optional
        :param url: url, defaults to None
        :type url: str, optional
        :param use_basic_auth: use_basic_auth, defaults to None
        :type use_basic_auth: bool, optional
        :param use_custom_auth: use_custom_auth, defaults to None
        :type use_custom_auth: bool, optional
        :param use_default_settings: use_default_settings, defaults to None
        :type use_default_settings: bool, optional
        """
        self.http_auth_settings = self._define_object(
            http_auth_settings, HttpAuthSettings
        )
        if httpo_auth2_settings is not SENTINEL:
            self.httpo_auth2_settings = self._define_object(
                httpo_auth2_settings, HttpoAuth2Settings
            )
        if httpo_auth_settings is not SENTINEL:
            self.httpo_auth_settings = self._define_object(
                httpo_auth_settings, HttpoAuthSettings
            )
        self.httpssl_options = self._define_object(httpssl_options, HttpsslOptions)
        if authentication_type is not SENTINEL:
            self.authentication_type = self._enum_matching(
                authentication_type,
                HttpSettingsAuthenticationType.list(),
                "authentication_type",
            )
        if connect_timeout is not SENTINEL:
            self.connect_timeout = connect_timeout
        if cookie_scope is not SENTINEL:
            self.cookie_scope = self._enum_matching(
                cookie_scope, CookieScope.list(), "cookie_scope"
            )
        if read_timeout is not SENTINEL:
            self.read_timeout = read_timeout
        if url is not SENTINEL:
            self.url = url
        if use_basic_auth is not SENTINEL:
            self.use_basic_auth = use_basic_auth
        if use_custom_auth is not SENTINEL:
            self.use_custom_auth = use_custom_auth
        if use_default_settings is not SENTINEL:
            self.use_default_settings = use_default_settings
        self._kwargs = kwargs
