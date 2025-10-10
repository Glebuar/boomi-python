
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class MapExtensionsNode(BaseModel):
    """MapExtensionsNode

    :param name: name, defaults to None
    :type name: str, optional
    :param xpath: xpath, defaults to None
    :type xpath: str, optional
    """

    def __init__(self, name: str = SENTINEL, xpath: str = SENTINEL, **kwargs):
        """MapExtensionsNode

        :param name: name, defaults to None
        :type name: str, optional
        :param xpath: xpath, defaults to None
        :type xpath: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        if xpath is not SENTINEL:
            self.xpath = xpath
        self._kwargs = kwargs
