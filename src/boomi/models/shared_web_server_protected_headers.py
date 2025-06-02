
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class SharedWebServerProtectedHeaders(BaseModel):
    """SharedWebServerProtectedHeaders

    :param header: header, defaults to None
    :type header: List[str], optional
    """

    def __init__(self, header: List[str] = SENTINEL, **kwargs):
        """SharedWebServerProtectedHeaders

        :param header: header, defaults to None
        :type header: List[str], optional
        """
        if header is not SENTINEL:
            self.header = header
        self._kwargs = kwargs
