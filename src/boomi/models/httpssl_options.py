
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"trust_server_cert": "trustServerCert"})
class HttpsslOptions(BaseModel):
    """HttpsslOptions

    :param clientauth: clientauth, defaults to None
    :type clientauth: bool, optional
    :param clientsslalias: clientsslalias, defaults to None
    :type clientsslalias: str, optional
    :param trust_server_cert: trust_server_cert, defaults to None
    :type trust_server_cert: bool, optional
    :param trustedcertalias: trustedcertalias, defaults to None
    :type trustedcertalias: str, optional
    """

    def __init__(
        self,
        clientauth: bool = SENTINEL,
        clientsslalias: str = SENTINEL,
        trust_server_cert: bool = SENTINEL,
        trustedcertalias: str = SENTINEL,
        **kwargs
    ):
        """HttpsslOptions

        :param clientauth: clientauth, defaults to None
        :type clientauth: bool, optional
        :param clientsslalias: clientsslalias, defaults to None
        :type clientsslalias: str, optional
        :param trust_server_cert: trust_server_cert, defaults to None
        :type trust_server_cert: bool, optional
        :param trustedcertalias: trustedcertalias, defaults to None
        :type trustedcertalias: str, optional
        """
        if clientauth is not SENTINEL:
            self.clientauth = clientauth
        if clientsslalias is not SENTINEL:
            self.clientsslalias = clientsslalias
        if trust_server_cert is not SENTINEL:
            self.trust_server_cert = trust_server_cert
        if trustedcertalias is not SENTINEL:
            self.trustedcertalias = trustedcertalias
        self._kwargs = kwargs
