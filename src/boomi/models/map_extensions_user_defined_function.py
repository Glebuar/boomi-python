
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"id_": "id"})
class MapExtensionsUserDefinedFunction(BaseModel):
    """MapExtensionsUserDefinedFunction

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param version: version, defaults to None
    :type version: int, optional
    """

    def __init__(self, id_: str = SENTINEL, version: int = SENTINEL, **kwargs):
        """MapExtensionsUserDefinedFunction

        :param id_: id_, defaults to None
        :type id_: str, optional
        :param version: version, defaults to None
        :type version: int, optional
        """
        if id_ is not SENTINEL:
            self.id_ = id_
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
