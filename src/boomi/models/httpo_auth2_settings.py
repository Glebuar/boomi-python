
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .http_endpoint import HttpEndpoint
from .http_request_parameters import HttpRequestParameters
from .httpo_auth_credentials import HttpoAuthCredentials


class GrantType(Enum):
    """An enumeration representing different categories.

    :cvar CODE: "code"
    :vartype CODE: str
    :cvar CLIENTCREDENTIALS: "client_credentials"
    :vartype CLIENTCREDENTIALS: str
    :cvar PASSWORD: "password"
    :vartype PASSWORD: str
    """

    CODE = "code"
    CLIENTCREDENTIALS = "client_credentials"
    PASSWORD = "password"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GrantType._member_map_.values()))


@JsonMap(
    {
        "access_token_endpoint": "accessTokenEndpoint",
        "access_token_parameters": "accessTokenParameters",
        "authorization_parameters": "authorizationParameters",
        "authorization_token_endpoint": "authorizationTokenEndpoint",
        "grant_type": "grantType",
    }
)
class HttpoAuth2Settings(BaseModel):
    """HttpoAuth2Settings

    :param access_token_endpoint: access_token_endpoint
    :type access_token_endpoint: HttpEndpoint
    :param access_token_parameters: access_token_parameters
    :type access_token_parameters: HttpRequestParameters
    :param authorization_parameters: authorization_parameters
    :type authorization_parameters: HttpRequestParameters
    :param authorization_token_endpoint: authorization_token_endpoint
    :type authorization_token_endpoint: HttpEndpoint
    :param credentials: credentials
    :type credentials: HttpoAuthCredentials
    :param grant_type: grant_type, defaults to None
    :type grant_type: GrantType, optional
    :param scope: scope
    :type scope: str
    """

    def __init__(
        self,
        access_token_endpoint: HttpEndpoint,
        access_token_parameters: HttpRequestParameters,
        authorization_parameters: HttpRequestParameters,
        authorization_token_endpoint: HttpEndpoint,
        credentials: HttpoAuthCredentials,
        scope: str,
        grant_type: GrantType = SENTINEL,
        **kwargs,
    ):
        """HttpoAuth2Settings

        :param access_token_endpoint: access_token_endpoint
        :type access_token_endpoint: HttpEndpoint
        :param access_token_parameters: access_token_parameters
        :type access_token_parameters: HttpRequestParameters
        :param authorization_parameters: authorization_parameters
        :type authorization_parameters: HttpRequestParameters
        :param authorization_token_endpoint: authorization_token_endpoint
        :type authorization_token_endpoint: HttpEndpoint
        :param credentials: credentials
        :type credentials: HttpoAuthCredentials
        :param grant_type: grant_type, defaults to None
        :type grant_type: GrantType, optional
        :param scope: scope
        :type scope: str
        """
        self.access_token_endpoint = self._define_object(
            access_token_endpoint, HttpEndpoint
        )
        self.access_token_parameters = self._define_object(
            access_token_parameters, HttpRequestParameters
        )
        self.authorization_parameters = self._define_object(
            authorization_parameters, HttpRequestParameters
        )
        self.authorization_token_endpoint = self._define_object(
            authorization_token_endpoint, HttpEndpoint
        )
        self.credentials = self._define_object(credentials, HttpoAuthCredentials)
        if grant_type is not SENTINEL:
            self.grant_type = self._enum_matching(
                grant_type, GrantType.list(), "grant_type"
            )
        self.scope = scope
        self._kwargs = kwargs
