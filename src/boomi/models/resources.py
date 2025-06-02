
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .resource import Resource


@JsonMap({"resource": "Resource"})
class Resources(BaseModel):
    """Resources

    :param resource: resource, defaults to None
    :type resource: List[Resource], optional
    """

    def __init__(self, resource: List[Resource] = SENTINEL, **kwargs):
        """Resources

        :param resource: resource, defaults to None
        :type resource: List[Resource], optional
        """
        if resource is not SENTINEL:
            self.resource = self._define_list(resource, Resource)
        self._kwargs = kwargs
