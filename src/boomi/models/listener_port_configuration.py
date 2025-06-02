
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_port import SharedWebServerPort


@JsonMap({})
class ListenerPortConfiguration(BaseModel):
    """ListenerPortConfiguration

    :param port: port, defaults to None
    :type port: List[SharedWebServerPort], optional
    """

    def __init__(self, port: List[SharedWebServerPort] = SENTINEL, **kwargs):
        """ListenerPortConfiguration

        :param port: port, defaults to None
        :type port: List[SharedWebServerPort], optional
        """
        if port is not SENTINEL:
            self.port = self._define_list(port, SharedWebServerPort)
        self._kwargs = kwargs
