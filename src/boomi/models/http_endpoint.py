
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .httpssl_options import HttpsslOptions


@JsonMap({"ssl_options": "sslOptions"})
class HttpEndpoint(BaseModel):
    """HttpEndpoint

    :param ssl_options: ssl_options
    :type ssl_options: HttpsslOptions
    :param url: url, defaults to None
    :type url: str, optional
    """

    def __init__(self, ssl_options: HttpsslOptions, url: str = SENTINEL, **kwargs):
        """HttpEndpoint

        :param ssl_options: ssl_options
        :type ssl_options: HttpsslOptions
        :param url: url, defaults to None
        :type url: str, optional
        """
        self.ssl_options = self._define_object(ssl_options, HttpsslOptions)
        if url is not SENTINEL:
            self.url = url
        self._kwargs = kwargs
