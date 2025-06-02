
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class TrackedField(BaseModel):
    """TrackedField

    :param name: name, defaults to None
    :type name: str, optional
    :param value: value, defaults to None
    :type value: str, optional
    """

    def __init__(self, name: str = SENTINEL, value: str = SENTINEL, **kwargs):
        """TrackedField

        :param name: name, defaults to None
        :type name: str, optional
        :param value: value, defaults to None
        :type value: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs
