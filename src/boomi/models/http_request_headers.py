
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .header import Header


@JsonMap({})
class HttpRequestHeaders(BaseModel):
    """HttpRequestHeaders

    :param header: header, defaults to None
    :type header: List[Header], optional
    """

    def __init__(self, header: List[Header] = SENTINEL, **kwargs):
        """HttpRequestHeaders

        :param header: header, defaults to None
        :type header: List[Header], optional
        """
        if header is not SENTINEL:
            self.header = self._define_list(header, Header)
        self._kwargs = kwargs
