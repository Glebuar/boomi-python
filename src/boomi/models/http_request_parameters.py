
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .parameter import Parameter


@JsonMap({})
class HttpRequestParameters(BaseModel):
    """HttpRequestParameters

    :param parameter: parameter, defaults to None
    :type parameter: List[Parameter], optional
    """

    def __init__(self, parameter: List[Parameter] = SENTINEL, **kwargs):
        """HttpRequestParameters

        :param parameter: parameter, defaults to None
        :type parameter: List[Parameter], optional
        """
        if parameter is not SENTINEL:
            self.parameter = self._define_list(parameter, Parameter)
        self._kwargs = kwargs
