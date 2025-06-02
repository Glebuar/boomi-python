
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "enable_http_request_handling": "EnableHTTPRequestHandling",
        "enable_https_request_handling": "EnableHTTPSRequestHandling",
        "allow_credentials": "allowCredentials",
        "allow_methods": "allowMethods",
        "allow_request_headers": "allowRequestHeaders",
        "allow_response_headers": "allowResponseHeaders",
        "cache_timeout": "cacheTimeout",
    }
)
class SharedWebServerCorsOrigin(BaseModel):
    """SharedWebServerCorsOrigin

    :param enable_http_request_handling: enable_http_request_handling, defaults to None
    :type enable_http_request_handling: bool, optional
    :param enable_https_request_handling: enable_https_request_handling, defaults to None
    :type enable_https_request_handling: bool, optional
    :param allow_credentials: allow_credentials, defaults to None
    :type allow_credentials: bool, optional
    :param allow_methods: allow_methods, defaults to None
    :type allow_methods: List[str], optional
    :param allow_request_headers: allow_request_headers, defaults to None
    :type allow_request_headers: List[str], optional
    :param allow_response_headers: allow_response_headers, defaults to None
    :type allow_response_headers: List[str], optional
    :param cache_timeout: cache_timeout, defaults to None
    :type cache_timeout: int, optional
    :param domain: domain
    :type domain: str
    :param ports: ports, defaults to None
    :type ports: List[int], optional
    """

    def __init__(
        self,
        domain: str,
        enable_http_request_handling: bool = SENTINEL,
        enable_https_request_handling: bool = SENTINEL,
        allow_credentials: bool = SENTINEL,
        allow_methods: List[str] = SENTINEL,
        allow_request_headers: List[str] = SENTINEL,
        allow_response_headers: List[str] = SENTINEL,
        cache_timeout: int = SENTINEL,
        ports: List[int] = SENTINEL,
        **kwargs
    ):
        """SharedWebServerCorsOrigin

        :param enable_http_request_handling: enable_http_request_handling, defaults to None
        :type enable_http_request_handling: bool, optional
        :param enable_https_request_handling: enable_https_request_handling, defaults to None
        :type enable_https_request_handling: bool, optional
        :param allow_credentials: allow_credentials, defaults to None
        :type allow_credentials: bool, optional
        :param allow_methods: allow_methods, defaults to None
        :type allow_methods: List[str], optional
        :param allow_request_headers: allow_request_headers, defaults to None
        :type allow_request_headers: List[str], optional
        :param allow_response_headers: allow_response_headers, defaults to None
        :type allow_response_headers: List[str], optional
        :param cache_timeout: cache_timeout, defaults to None
        :type cache_timeout: int, optional
        :param domain: domain
        :type domain: str
        :param ports: ports, defaults to None
        :type ports: List[int], optional
        """
        if enable_http_request_handling is not SENTINEL:
            self.enable_http_request_handling = enable_http_request_handling
        if enable_https_request_handling is not SENTINEL:
            self.enable_https_request_handling = enable_https_request_handling
        if allow_credentials is not SENTINEL:
            self.allow_credentials = allow_credentials
        if allow_methods is not SENTINEL:
            self.allow_methods = allow_methods
        if allow_request_headers is not SENTINEL:
            self.allow_request_headers = allow_request_headers
        if allow_response_headers is not SENTINEL:
            self.allow_response_headers = allow_response_headers
        if cache_timeout is not SENTINEL:
            self.cache_timeout = cache_timeout
        self.domain = domain
        if ports is not SENTINEL:
            self.ports = ports
        self._kwargs = kwargs
