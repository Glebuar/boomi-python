
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_cors_origin import SharedWebServerCorsOrigin


@JsonMap({})
class SharedWebServerCors(BaseModel):
    """SharedWebServerCors

    :param origins: origins, defaults to None
    :type origins: List[SharedWebServerCorsOrigin], optional
    """

    def __init__(self, origins: List[SharedWebServerCorsOrigin] = SENTINEL, **kwargs):
        """SharedWebServerCors

        :param origins: origins, defaults to None
        :type origins: List[SharedWebServerCorsOrigin], optional
        """
        if origins is not SENTINEL:
            self.origins = self._define_list(origins, SharedWebServerCorsOrigin)
        self._kwargs = kwargs
