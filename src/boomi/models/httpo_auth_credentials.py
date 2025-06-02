
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "access_token": "accessToken",
        "access_token_key": "accessTokenKey",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "use_refresh_token": "useRefreshToken",
    }
)
class HttpoAuthCredentials(BaseModel):
    """HttpoAuthCredentials

    :param access_token: access_token, defaults to None
    :type access_token: str, optional
    :param access_token_key: access_token_key, defaults to None
    :type access_token_key: str, optional
    :param client_id: client_id, defaults to None
    :type client_id: str, optional
    :param client_secret: client_secret, defaults to None
    :type client_secret: str, optional
    :param use_refresh_token: use_refresh_token, defaults to None
    :type use_refresh_token: bool, optional
    """

    def __init__(
        self,
        access_token: str = SENTINEL,
        access_token_key: str = SENTINEL,
        client_id: str = SENTINEL,
        client_secret: str = SENTINEL,
        use_refresh_token: bool = SENTINEL,
        **kwargs
    ):
        """HttpoAuthCredentials

        :param access_token: access_token, defaults to None
        :type access_token: str, optional
        :param access_token_key: access_token_key, defaults to None
        :type access_token_key: str, optional
        :param client_id: client_id, defaults to None
        :type client_id: str, optional
        :param client_secret: client_secret, defaults to None
        :type client_secret: str, optional
        :param use_refresh_token: use_refresh_token, defaults to None
        :type use_refresh_token: bool, optional
        """
        if access_token is not SENTINEL:
            self.access_token = access_token
        if access_token_key is not SENTINEL:
            self.access_token_key = access_token_key
        if client_id is not SENTINEL:
            self.client_id = client_id
        if client_secret is not SENTINEL:
            self.client_secret = client_secret
        if use_refresh_token is not SENTINEL:
            self.use_refresh_token = use_refresh_token
        self._kwargs = kwargs
