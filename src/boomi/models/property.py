
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class Property(BaseModel):
    """Property

    :param name: Name of property. Refer the Startup Properties Reference table., defaults to None
    :type name: str, optional
    :param value: Value of property., defaults to None
    :type value: str, optional
    """

    def __init__(self, name: str = SENTINEL, value: str = SENTINEL, **kwargs):
        """Property

        :param name: Name of property. Refer the Startup Properties Reference table., defaults to None
        :type name: str, optional
        :param value: Value of property., defaults to None
        :type value: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs
