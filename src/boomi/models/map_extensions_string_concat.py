
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"fixed_length": "fixedLength"})
class MapExtensionsStringConcat(BaseModel):
    """MapExtensionsStringConcat

    :param delimiter: delimiter, defaults to None
    :type delimiter: str, optional
    :param fixed_length: fixed_length, defaults to None
    :type fixed_length: int, optional
    """

    def __init__(
        self, delimiter: str = SENTINEL, fixed_length: int = SENTINEL, **kwargs
    ):
        """MapExtensionsStringConcat

        :param delimiter: delimiter, defaults to None
        :type delimiter: str, optional
        :param fixed_length: fixed_length, defaults to None
        :type fixed_length: int, optional
        """
        if delimiter is not SENTINEL:
            self.delimiter = delimiter
        if fixed_length is not SENTINEL:
            self.fixed_length = fixed_length
        self._kwargs = kwargs
