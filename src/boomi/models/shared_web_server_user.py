
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "client_certificate": "clientCertificate",
        "component_filters": "componentFilters",
        "external_username": "externalUsername",
        "ip_filters": "ipFilters",
        "role_associations": "roleAssociations",
        "using_component_filters": "usingComponentFilters",
        "using_ip_filters": "usingIPFilters",
    }
)
class SharedWebServerUser(BaseModel):
    """SharedWebServerUser

    :param client_certificate: client_certificate, defaults to None
    :type client_certificate: str, optional
    :param component_filters: component_filters, defaults to None
    :type component_filters: List[str], optional
    :param external_username: external_username, defaults to None
    :type external_username: str, optional
    :param ip_filters: ip_filters, defaults to None
    :type ip_filters: List[str], optional
    :param role_associations: role_associations, defaults to None
    :type role_associations: List[str], optional
    :param token: token, defaults to None
    :type token: str, optional
    :param username: username
    :type username: str
    :param using_component_filters: using_component_filters, defaults to None
    :type using_component_filters: bool, optional
    :param using_ip_filters: using_ip_filters, defaults to None
    :type using_ip_filters: bool, optional
    """

    def __init__(
        self,
        username: str,
        client_certificate: str = SENTINEL,
        component_filters: List[str] = SENTINEL,
        external_username: str = SENTINEL,
        ip_filters: List[str] = SENTINEL,
        role_associations: List[str] = SENTINEL,
        token: str = SENTINEL,
        using_component_filters: bool = SENTINEL,
        using_ip_filters: bool = SENTINEL,
        **kwargs
    ):
        """SharedWebServerUser

        :param client_certificate: client_certificate, defaults to None
        :type client_certificate: str, optional
        :param component_filters: component_filters, defaults to None
        :type component_filters: List[str], optional
        :param external_username: external_username, defaults to None
        :type external_username: str, optional
        :param ip_filters: ip_filters, defaults to None
        :type ip_filters: List[str], optional
        :param role_associations: role_associations, defaults to None
        :type role_associations: List[str], optional
        :param token: token, defaults to None
        :type token: str, optional
        :param username: username
        :type username: str
        :param using_component_filters: using_component_filters, defaults to None
        :type using_component_filters: bool, optional
        :param using_ip_filters: using_ip_filters, defaults to None
        :type using_ip_filters: bool, optional
        """
        if client_certificate is not SENTINEL:
            self.client_certificate = client_certificate
        if component_filters is not SENTINEL:
            self.component_filters = component_filters
        if external_username is not SENTINEL:
            self.external_username = external_username
        if ip_filters is not SENTINEL:
            self.ip_filters = ip_filters
        if role_associations is not SENTINEL:
            self.role_associations = role_associations
        if token is not SENTINEL:
            self.token = token
        self.username = username
        if using_component_filters is not SENTINEL:
            self.using_component_filters = using_component_filters
        if using_ip_filters is not SENTINEL:
            self.using_ip_filters = using_ip_filters
        self._kwargs = kwargs
