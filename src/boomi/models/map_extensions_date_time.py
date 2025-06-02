
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class MapExtensionsDateTime(BaseModel):
    """MapExtensionsDateTime

    :param format: format, defaults to None
    :type format: str, optional
    """

    def __init__(self, format: str = SENTINEL, **kwargs):
        """MapExtensionsDateTime

        :param format: format, defaults to None
        :type format: str, optional
        """
        if format is not SENTINEL:
            self.format = format
        self._kwargs = kwargs
