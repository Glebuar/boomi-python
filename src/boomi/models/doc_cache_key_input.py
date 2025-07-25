
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"key_id": "keyId"})
class DocCacheKeyInput(BaseModel):
    """DocCacheKeyInput

    :param index: index, defaults to None
    :type index: int, optional
    :param key_id: key_id, defaults to None
    :type key_id: int, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        index: int = SENTINEL,
        key_id: int = SENTINEL,
        name: str = SENTINEL,
        **kwargs
    ):
        """DocCacheKeyInput

        :param index: index, defaults to None
        :type index: int, optional
        :param key_id: key_id, defaults to None
        :type key_id: int, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if index is not SENTINEL:
            self.index = index
        if key_id is not SENTINEL:
            self.key_id = key_id
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
