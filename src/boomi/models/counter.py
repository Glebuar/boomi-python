
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class Counter(BaseModel):
    """Counter

    :param name: The name of the counter., defaults to None
    :type name: str, optional
    :param value: The assigned value to the counter., defaults to None
    :type value: int, optional
    """

    def __init__(self, name: str = SENTINEL, value: int = SENTINEL, **kwargs):
        """Counter

        :param name: The name of the counter., defaults to None
        :type name: str, optional
        :param value: The assigned value to the counter., defaults to None
        :type value: int, optional
        """
        if name is not SENTINEL:
            self.name = name
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs
