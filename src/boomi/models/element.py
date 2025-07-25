
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class Element(BaseModel):
    """Element

    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = SENTINEL, **kwargs):
        """Element

        :param name: name, defaults to None
        :type name: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
