
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .listener_port_configuration import ListenerPortConfiguration


@JsonMap(
    {
        "api_type": "apiType",
        "auth_type": "authType",
        "base_url": "baseUrl",
        "listener_ports": "listenerPorts",
    }
)
class SharedWebServerCloudTennantGeneral(BaseModel):
    """SharedWebServerCloudTennantGeneral

    :param api_type: api_type
    :type api_type: str
    :param auth_type: auth_type
    :type auth_type: str
    :param base_url: base_url
    :type base_url: str
    :param listener_ports: listener_ports
    :type listener_ports: ListenerPortConfiguration
    """

    def __init__(
        self,
        api_type: str,
        auth_type: str,
        base_url: str,
        listener_ports: ListenerPortConfiguration,
        **kwargs,
    ):
        """SharedWebServerCloudTennantGeneral

        :param api_type: api_type
        :type api_type: str
        :param auth_type: auth_type
        :type auth_type: str
        :param base_url: base_url
        :type base_url: str
        :param listener_ports: listener_ports
        :type listener_ports: ListenerPortConfiguration
        """
        self.api_type = api_type
        self.auth_type = auth_type
        self.base_url = base_url
        self.listener_ports = self._define_object(
            listener_ports, ListenerPortConfiguration
        )
        self._kwargs = kwargs
