
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class MapExtensionsOutput(BaseModel):
    """MapExtensionsOutput

    :param key: key, defaults to None
    :type key: int, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, key: int = SENTINEL, name: str = SENTINEL, **kwargs):
        """MapExtensionsOutput

        :param key: key, defaults to None
        :type key: int, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if key is not SENTINEL:
            self.key = key
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
