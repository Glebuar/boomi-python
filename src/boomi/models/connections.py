
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .connection import Connection


@JsonMap({})
class Connections(BaseModel):
    """Connections

    :param connection: connection, defaults to None
    :type connection: List[Connection], optional
    """

    def __init__(self, connection: List[Connection] = SENTINEL, **kwargs):
        """Connections

        :param connection: connection, defaults to None
        :type connection: List[Connection], optional
        """
        if connection is not SENTINEL:
            self.connection = self._define_list(connection, Connection)
        self._kwargs = kwargs
