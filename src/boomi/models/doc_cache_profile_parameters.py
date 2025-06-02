
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .doc_cache_profile_parameter import DocCacheProfileParameter


@JsonMap({"output": "Output"})
class DocCacheProfileParameters(BaseModel):
    """DocCacheProfileParameters

    :param output: output, defaults to None
    :type output: List[DocCacheProfileParameter], optional
    """

    def __init__(self, output: List[DocCacheProfileParameter] = SENTINEL, **kwargs):
        """DocCacheProfileParameters

        :param output: output, defaults to None
        :type output: List[DocCacheProfileParameter], optional
        """
        if output is not SENTINEL:
            self.output = self._define_list(output, DocCacheProfileParameter)
        self._kwargs = kwargs
