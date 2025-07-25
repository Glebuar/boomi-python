
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"split_length": "splitLength"})
class MapExtensionsStringSplit(BaseModel):
    """MapExtensionsStringSplit

    :param delimiter: delimiter, defaults to None
    :type delimiter: str, optional
    :param split_length: split_length, defaults to None
    :type split_length: int, optional
    """

    def __init__(
        self, delimiter: str = SENTINEL, split_length: int = SENTINEL, **kwargs
    ):
        """MapExtensionsStringSplit

        :param delimiter: delimiter, defaults to None
        :type delimiter: str, optional
        :param split_length: split_length, defaults to None
        :type split_length: int, optional
        """
        if delimiter is not SENTINEL:
            self.delimiter = delimiter
        if split_length is not SENTINEL:
            self.split_length = split_length
        self._kwargs = kwargs
