
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .doc_cache_key_input import DocCacheKeyInput


@JsonMap({"input": "Input"})
class DocCacheKeyInputs(BaseModel):
    """DocCacheKeyInputs

    :param input: input, defaults to None
    :type input: List[DocCacheKeyInput], optional
    """

    def __init__(self, input: List[DocCacheKeyInput] = SENTINEL, **kwargs):
        """DocCacheKeyInputs

        :param input: input, defaults to None
        :type input: List[DocCacheKeyInput], optional
        """
        if input is not SENTINEL:
            self.input = self._define_list(input, DocCacheKeyInput)
        self._kwargs = kwargs
