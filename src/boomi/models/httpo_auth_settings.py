
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class SignatureMethod(Enum):
    """An enumeration representing different categories.

    :cvar SHA1: "SHA1"
    :vartype SHA1: str
    :cvar SHA256: "SHA256"
    :vartype SHA256: str
    """

    SHA1 = "SHA1"
    SHA256 = "SHA256"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SignatureMethod._member_map_.values()))


@JsonMap(
    {
        "access_token": "accessToken",
        "access_token_url": "accessTokenURL",
        "authorization_url": "authorizationURL",
        "consumer_key": "consumerKey",
        "consumer_secret": "consumerSecret",
        "request_token_url": "requestTokenURL",
        "signature_method": "signatureMethod",
        "suppress_blank_access_token": "suppressBlankAccessToken",
        "token_secret": "tokenSecret",
    }
)
class HttpoAuthSettings(BaseModel):
    """HttpoAuthSettings

    :param access_token: access_token, defaults to None
    :type access_token: str, optional
    :param access_token_url: access_token_url, defaults to None
    :type access_token_url: str, optional
    :param authorization_url: authorization_url, defaults to None
    :type authorization_url: str, optional
    :param consumer_key: consumer_key, defaults to None
    :type consumer_key: str, optional
    :param consumer_secret: consumer_secret, defaults to None
    :type consumer_secret: str, optional
    :param realm: realm, defaults to None
    :type realm: str, optional
    :param request_token_url: request_token_url, defaults to None
    :type request_token_url: str, optional
    :param signature_method: signature_method, defaults to None
    :type signature_method: SignatureMethod, optional
    :param suppress_blank_access_token: suppress_blank_access_token, defaults to None
    :type suppress_blank_access_token: bool, optional
    :param token_secret: token_secret, defaults to None
    :type token_secret: str, optional
    """

    def __init__(
        self,
        access_token: str = SENTINEL,
        access_token_url: str = SENTINEL,
        authorization_url: str = SENTINEL,
        consumer_key: str = SENTINEL,
        consumer_secret: str = SENTINEL,
        realm: str = SENTINEL,
        request_token_url: str = SENTINEL,
        signature_method: SignatureMethod = SENTINEL,
        suppress_blank_access_token: bool = SENTINEL,
        token_secret: str = SENTINEL,
        **kwargs
    ):
        """HttpoAuthSettings

        :param access_token: access_token, defaults to None
        :type access_token: str, optional
        :param access_token_url: access_token_url, defaults to None
        :type access_token_url: str, optional
        :param authorization_url: authorization_url, defaults to None
        :type authorization_url: str, optional
        :param consumer_key: consumer_key, defaults to None
        :type consumer_key: str, optional
        :param consumer_secret: consumer_secret, defaults to None
        :type consumer_secret: str, optional
        :param realm: realm, defaults to None
        :type realm: str, optional
        :param request_token_url: request_token_url, defaults to None
        :type request_token_url: str, optional
        :param signature_method: signature_method, defaults to None
        :type signature_method: SignatureMethod, optional
        :param suppress_blank_access_token: suppress_blank_access_token, defaults to None
        :type suppress_blank_access_token: bool, optional
        :param token_secret: token_secret, defaults to None
        :type token_secret: str, optional
        """
        if access_token is not SENTINEL:
            self.access_token = access_token
        if access_token_url is not SENTINEL:
            self.access_token_url = access_token_url
        if authorization_url is not SENTINEL:
            self.authorization_url = authorization_url
        if consumer_key is not SENTINEL:
            self.consumer_key = consumer_key
        if consumer_secret is not SENTINEL:
            self.consumer_secret = consumer_secret
        if realm is not SENTINEL:
            self.realm = realm
        if request_token_url is not SENTINEL:
            self.request_token_url = request_token_url
        if signature_method is not SENTINEL:
            self.signature_method = self._enum_matching(
                signature_method, SignatureMethod.list(), "signature_method"
            )
        if suppress_blank_access_token is not SENTINEL:
            self.suppress_blank_access_token = suppress_blank_access_token
        if token_secret is not SENTINEL:
            self.token_secret = token_secret
        self._kwargs = kwargs
