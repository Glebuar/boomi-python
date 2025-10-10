
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "client_ssl_alias": "clientSSLAlias",
        "ssl_alias": "sslAlias",
        "use_client_ssl": "useClientSSL",
        "use_ssl": "useSSL",
    }
)
class MllpsslOptions(BaseModel):
    """MllpsslOptions

    :param client_ssl_alias: client_ssl_alias, defaults to None
    :type client_ssl_alias: str, optional
    :param ssl_alias: ssl_alias, defaults to None
    :type ssl_alias: str, optional
    :param use_client_ssl: use_client_ssl, defaults to None
    :type use_client_ssl: bool, optional
    :param use_ssl: use_ssl, defaults to None
    :type use_ssl: bool, optional
    """

    def __init__(
        self,
        client_ssl_alias: str = SENTINEL,
        ssl_alias: str = SENTINEL,
        use_client_ssl: bool = SENTINEL,
        use_ssl: bool = SENTINEL,
        **kwargs
    ):
        """MllpsslOptions

        :param client_ssl_alias: client_ssl_alias, defaults to None
        :type client_ssl_alias: str, optional
        :param ssl_alias: ssl_alias, defaults to None
        :type ssl_alias: str, optional
        :param use_client_ssl: use_client_ssl, defaults to None
        :type use_client_ssl: bool, optional
        :param use_ssl: use_ssl, defaults to None
        :type use_ssl: bool, optional
        """
        if client_ssl_alias is not SENTINEL:
            self.client_ssl_alias = client_ssl_alias
        if ssl_alias is not SENTINEL:
            self.ssl_alias = ssl_alias
        if use_client_ssl is not SENTINEL:
            self.use_client_ssl = use_client_ssl
        if use_ssl is not SENTINEL:
            self.use_ssl = use_ssl
        self._kwargs = kwargs
