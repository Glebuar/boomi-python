
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class MapExtensionsInput(BaseModel):
    """MapExtensionsInput

    :param default: default, defaults to None
    :type default: str, optional
    :param key: key, defaults to None
    :type key: int, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        default: str = SENTINEL,
        key: int = SENTINEL,
        name: str = SENTINEL,
        **kwargs
    ):
        """MapExtensionsInput

        :param default: default, defaults to None
        :type default: str, optional
        :param key: key, defaults to None
        :type key: int, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if default is not SENTINEL:
            self.default = default
        if key is not SENTINEL:
            self.key = key
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
