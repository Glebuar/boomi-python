
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "auth_type": "authType",
        "base_url_for_request": "baseUrlForRequest",
        "default_port": "defaultPort",
        "enable_port": "enablePort",
        "external_port": "externalPort",
        "external_ssl": "externalSSL",
    }
)
class SharedWebServerPort(BaseModel):
    """SharedWebServerPort

    :param auth_type: auth_type
    :type auth_type: str
    :param base_url_for_request: base_url_for_request
    :type base_url_for_request: str
    :param default_port: default_port, defaults to None
    :type default_port: bool, optional
    :param enable_port: enable_port, defaults to None
    :type enable_port: bool, optional
    :param external_port: external_port, defaults to None
    :type external_port: int, optional
    :param external_ssl: external_ssl, defaults to None
    :type external_ssl: bool, optional
    :param port: port, defaults to None
    :type port: int, optional
    :param ssl: ssl, defaults to None
    :type ssl: bool, optional
    """

    def __init__(
        self,
        auth_type: str,
        base_url_for_request: str,
        default_port: bool = SENTINEL,
        enable_port: bool = SENTINEL,
        external_port: int = SENTINEL,
        external_ssl: bool = SENTINEL,
        port: int = SENTINEL,
        ssl: bool = SENTINEL,
        **kwargs
    ):
        """SharedWebServerPort

        :param auth_type: auth_type
        :type auth_type: str
        :param base_url_for_request: base_url_for_request
        :type base_url_for_request: str
        :param default_port: default_port, defaults to None
        :type default_port: bool, optional
        :param enable_port: enable_port, defaults to None
        :type enable_port: bool, optional
        :param external_port: external_port, defaults to None
        :type external_port: int, optional
        :param external_ssl: external_ssl, defaults to None
        :type external_ssl: bool, optional
        :param port: port, defaults to None
        :type port: int, optional
        :param ssl: ssl, defaults to None
        :type ssl: bool, optional
        """
        self.auth_type = auth_type
        self.base_url_for_request = base_url_for_request
        if default_port is not SENTINEL:
            self.default_port = default_port
        if enable_port is not SENTINEL:
            self.enable_port = enable_port
        if external_port is not SENTINEL:
            self.external_port = external_port
        if external_ssl is not SENTINEL:
            self.external_ssl = external_ssl
        if port is not SENTINEL:
            self.port = port
        if ssl is not SENTINEL:
            self.ssl = ssl
        self._kwargs = kwargs
