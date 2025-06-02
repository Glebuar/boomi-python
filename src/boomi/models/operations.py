
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .operation import Operation


@JsonMap({})
class Operations(BaseModel):
    """Operations

    :param operation: operation, defaults to None
    :type operation: List[Operation], optional
    """

    def __init__(self, operation: List[Operation] = SENTINEL, **kwargs):
        """Operations

        :param operation: operation, defaults to None
        :type operation: List[Operation], optional
        """
        if operation is not SENTINEL:
            self.operation = self._define_list(operation, Operation)
        self._kwargs = kwargs
