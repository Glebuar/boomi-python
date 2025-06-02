
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ApiType(Enum):
    """An enumeration representing different categories.

    :cvar BASIC: "basic"
    :vartype BASIC: str
    :cvar INTERMEDIATE: "intermediate"
    :vartype INTERMEDIATE: str
    :cvar ADVANCED: "advanced"
    :vartype ADVANCED: str
    """

    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ApiType._member_map_.values()))


class Auth(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "none"
    :vartype NONE: str
    :cvar BASIC: "basic"
    :vartype BASIC: str
    """

    NONE = "none"
    BASIC = "basic"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Auth._member_map_.values()))


class MinAuth(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "none"
    :vartype NONE: str
    :cvar BASIC: "basic"
    :vartype BASIC: str
    """

    NONE = "none"
    BASIC = "basic"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MinAuth._member_map_.values()))


@JsonMap(
    {
        "api_type": "apiType",
        "atom_id": "atomId",
        "auth_token": "authToken",
        "check_forwarded_headers": "checkForwardedHeaders",
        "external_host": "externalHost",
        "external_http_port": "externalHttpPort",
        "external_https_port": "externalHttpsPort",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "internal_host": "internalHost",
        "max_threads": "maxThreads",
        "min_auth": "minAuth",
        "override_url": "overrideUrl",
        "ssl_certificate_id": "sslCertificateId",
    }
)
class SharedServerInformation(BaseModel):
    """SharedServerInformation

    :param api_type: The level of user management and API management functionality applicable to the shared web server.Options are basic, intermediate, and advanced. The default is intermediate., defaults to None
    :type api_type: ApiType, optional
    :param atom_id: The ID of the Runtime that is hosting the shared web server., defaults to None
    :type atom_id: str, optional
    :param auth: The authentication required by the web server. Options are none and basic. If minAuth is set to basic, you must also set auth to basic., defaults to None
    :type auth: Auth, optional
    :param auth_token: If you configure BASIC authentication, this is an authentication token for connecting to the shared web server. You cannot update this with the UPDATE operation., defaults to None
    :type auth_token: str, optional
    :param check_forwarded_headers: Information regarding the external host, might be forwarded in headers. The embedded Java technology is capable of examining these headers and extracting external host information for response and callback purposes. Set this to true to enable the server to check for this information. The default is false., defaults to None
    :type check_forwarded_headers: bool, optional
    :param external_host: The external host name or IP for the listener., defaults to None
    :type external_host: str, optional
    :param external_http_port: The external HTTP port routes to the shared web server listener., defaults to None
    :type external_http_port: int, optional
    :param external_https_port: The external HTTPS port routes to the shared web server listener., defaults to None
    :type external_https_port: int, optional
    :param http_port: The HTTP port on which the web server listens. The default port is 9090., defaults to None
    :type http_port: int, optional
    :param https_port: The SSL \(HTTPS\) port on which the web server listens, if applicable. The default port is 9093., defaults to None
    :type https_port: int, optional
    :param internal_host: For multi-homed boxes, the IP address you want to use for binding to a specific interface., defaults to None
    :type internal_host: str, optional
    :param max_threads: The maximum number of handler threads that the listen process spawn. It queues other requests., defaults to None
    :type max_threads: int, optional
    :param min_auth: The minimum authentication required by the web server. Options are none and basic. The are multi-tenant, so the default is set to basic. The default for local Runtimes and Runtime clusters is none., defaults to None
    :type min_auth: MinAuth, optional
    :param override_url: Allows manual overriding of the exposed URL used to connect to the shared web server. This value is for informational purposes for any tenant. By default, this is false, meaning the URL is constructed based on the host name or external host name and port or SSL port settings. Set this to true to specify a custom URL attribute value., defaults to None
    :type override_url: bool, optional
    :param ssl_certificate_id: The component ID for the SSL certificate used by the server, if applicable., defaults to None
    :type ssl_certificate_id: str, optional
    :param url: The URL for connecting to the shared web server., defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        api_type: ApiType = SENTINEL,
        atom_id: str = SENTINEL,
        auth: Auth = SENTINEL,
        auth_token: str = SENTINEL,
        check_forwarded_headers: bool = SENTINEL,
        external_host: str = SENTINEL,
        external_http_port: int = SENTINEL,
        external_https_port: int = SENTINEL,
        http_port: int = SENTINEL,
        https_port: int = SENTINEL,
        internal_host: str = SENTINEL,
        max_threads: int = SENTINEL,
        min_auth: MinAuth = SENTINEL,
        override_url: bool = SENTINEL,
        ssl_certificate_id: str = SENTINEL,
        url: str = SENTINEL,
        **kwargs
    ):
        """SharedServerInformation

        :param api_type: The level of user management and API management functionality applicable to the shared web server.Options are basic, intermediate, and advanced. The default is intermediate., defaults to None
        :type api_type: ApiType, optional
        :param atom_id: The ID of the Runtime that is hosting the shared web server., defaults to None
        :type atom_id: str, optional
        :param auth: The authentication required by the web server. Options are none and basic. If minAuth is set to basic, you must also set auth to basic., defaults to None
        :type auth: Auth, optional
        :param auth_token: If you configure BASIC authentication, this is an authentication token for connecting to the shared web server. You cannot update this with the UPDATE operation., defaults to None
        :type auth_token: str, optional
        :param check_forwarded_headers: Information regarding the external host, might be forwarded in headers. The embedded Java technology is capable of examining these headers and extracting external host information for response and callback purposes. Set this to true to enable the server to check for this information. The default is false., defaults to None
        :type check_forwarded_headers: bool, optional
        :param external_host: The external host name or IP for the listener., defaults to None
        :type external_host: str, optional
        :param external_http_port: The external HTTP port routes to the shared web server listener., defaults to None
        :type external_http_port: int, optional
        :param external_https_port: The external HTTPS port routes to the shared web server listener., defaults to None
        :type external_https_port: int, optional
        :param http_port: The HTTP port on which the web server listens. The default port is 9090., defaults to None
        :type http_port: int, optional
        :param https_port: The SSL \(HTTPS\) port on which the web server listens, if applicable. The default port is 9093., defaults to None
        :type https_port: int, optional
        :param internal_host: For multi-homed boxes, the IP address you want to use for binding to a specific interface., defaults to None
        :type internal_host: str, optional
        :param max_threads: The maximum number of handler threads that the listen process spawn. It queues other requests., defaults to None
        :type max_threads: int, optional
        :param min_auth: The minimum authentication required by the web server. Options are none and basic. The are multi-tenant, so the default is set to basic. The default for local Runtimes and Runtime clusters is none., defaults to None
        :type min_auth: MinAuth, optional
        :param override_url: Allows manual overriding of the exposed URL used to connect to the shared web server. This value is for informational purposes for any tenant. By default, this is false, meaning the URL is constructed based on the host name or external host name and port or SSL port settings. Set this to true to specify a custom URL attribute value., defaults to None
        :type override_url: bool, optional
        :param ssl_certificate_id: The component ID for the SSL certificate used by the server, if applicable., defaults to None
        :type ssl_certificate_id: str, optional
        :param url: The URL for connecting to the shared web server., defaults to None
        :type url: str, optional
        """
        if api_type is not SENTINEL:
            self.api_type = self._enum_matching(api_type, ApiType.list(), "api_type")
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if auth is not SENTINEL:
            self.auth = self._enum_matching(auth, Auth.list(), "auth")
        if auth_token is not SENTINEL:
            self.auth_token = auth_token
        if check_forwarded_headers is not SENTINEL:
            self.check_forwarded_headers = check_forwarded_headers
        if external_host is not SENTINEL:
            self.external_host = external_host
        if external_http_port is not SENTINEL:
            self.external_http_port = external_http_port
        if external_https_port is not SENTINEL:
            self.external_https_port = external_https_port
        if http_port is not SENTINEL:
            self.http_port = http_port
        if https_port is not SENTINEL:
            self.https_port = https_port
        if internal_host is not SENTINEL:
            self.internal_host = internal_host
        if max_threads is not SENTINEL:
            self.max_threads = max_threads
        if min_auth is not SENTINEL:
            self.min_auth = self._enum_matching(min_auth, MinAuth.list(), "min_auth")
        if override_url is not SENTINEL:
            self.override_url = override_url
        if ssl_certificate_id is not SENTINEL:
            self.ssl_certificate_id = ssl_certificate_id
        if url is not SENTINEL:
            self.url = url
        self._kwargs = kwargs
