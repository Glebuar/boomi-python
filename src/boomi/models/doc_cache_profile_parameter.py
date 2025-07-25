
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"tag_list_key": "tagListKey"})
class DocCacheProfileParameter(BaseModel):
    """DocCacheProfileParameter

    :param index: index, defaults to None
    :type index: int, optional
    :param key: key, defaults to None
    :type key: int, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param tag_list_key: tag_list_key, defaults to None
    :type tag_list_key: int, optional
    """

    def __init__(
        self,
        index: int = SENTINEL,
        key: int = SENTINEL,
        name: str = SENTINEL,
        tag_list_key: int = SENTINEL,
        **kwargs
    ):
        """DocCacheProfileParameter

        :param index: index, defaults to None
        :type index: int, optional
        :param key: key, defaults to None
        :type key: int, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param tag_list_key: tag_list_key, defaults to None
        :type tag_list_key: int, optional
        """
        if index is not SENTINEL:
            self.index = index
        if key is not SENTINEL:
            self.key = key
        if name is not SENTINEL:
            self.name = name
        if tag_list_key is not SENTINEL:
            self.tag_list_key = tag_list_key
        self._kwargs = kwargs
