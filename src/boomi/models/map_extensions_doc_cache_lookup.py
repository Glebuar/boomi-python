
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .doc_cache_key_inputs import DocCacheKeyInputs
from .doc_cache_profile_parameters import DocCacheProfileParameters


@JsonMap(
    {
        "inputs": "Inputs",
        "outputs": "Outputs",
        "cache_index": "cacheIndex",
        "doc_cache": "docCache",
    }
)
class MapExtensionsDocCacheLookup(BaseModel):
    """MapExtensionsDocCacheLookup

    :param inputs: inputs
    :type inputs: DocCacheKeyInputs
    :param outputs: outputs
    :type outputs: DocCacheProfileParameters
    :param cache_index: cache_index, defaults to None
    :type cache_index: int, optional
    :param doc_cache: doc_cache, defaults to None
    :type doc_cache: str, optional
    """

    def __init__(
        self,
        inputs: DocCacheKeyInputs,
        outputs: DocCacheProfileParameters,
        cache_index: int = SENTINEL,
        doc_cache: str = SENTINEL,
        **kwargs,
    ):
        """MapExtensionsDocCacheLookup

        :param inputs: inputs
        :type inputs: DocCacheKeyInputs
        :param outputs: outputs
        :type outputs: DocCacheProfileParameters
        :param cache_index: cache_index, defaults to None
        :type cache_index: int, optional
        :param doc_cache: doc_cache, defaults to None
        :type doc_cache: str, optional
        """
        self.inputs = self._define_object(inputs, DocCacheKeyInputs)
        self.outputs = self._define_object(outputs, DocCacheProfileParameters)
        if cache_index is not SENTINEL:
            self.cache_index = cache_index
        if doc_cache is not SENTINEL:
            self.doc_cache = doc_cache
        self._kwargs = kwargs
