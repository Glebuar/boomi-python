
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "batch_size": "batchSize",
        "key_fix_to_length": "keyFixToLength",
        "key_name": "keyName",
    }
)
class MapExtensionsSequentialValue(BaseModel):
    """MapExtensionsSequentialValue

    :param batch_size: batch_size, defaults to None
    :type batch_size: int, optional
    :param key_fix_to_length: key_fix_to_length, defaults to None
    :type key_fix_to_length: int, optional
    :param key_name: key_name, defaults to None
    :type key_name: str, optional
    """

    def __init__(
        self,
        batch_size: int = SENTINEL,
        key_fix_to_length: int = SENTINEL,
        key_name: str = SENTINEL,
        **kwargs
    ):
        """MapExtensionsSequentialValue

        :param batch_size: batch_size, defaults to None
        :type batch_size: int, optional
        :param key_fix_to_length: key_fix_to_length, defaults to None
        :type key_fix_to_length: int, optional
        :param key_name: key_name, defaults to None
        :type key_name: str, optional
        """
        if batch_size is not SENTINEL:
            self.batch_size = batch_size
        if key_fix_to_length is not SENTINEL:
            self.key_fix_to_length = key_fix_to_length
        if key_name is not SENTINEL:
            self.key_name = key_name
        self._kwargs = kwargs
