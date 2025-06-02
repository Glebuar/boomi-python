
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class SharedWebServerLoginModuleOption(BaseModel):
    """SharedWebServerLoginModuleOption

    :param encrypt: encrypt, defaults to None
    :type encrypt: bool, optional
    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    def __init__(self, name: str, value: str, encrypt: bool = SENTINEL, **kwargs):
        """SharedWebServerLoginModuleOption

        :param encrypt: encrypt, defaults to None
        :type encrypt: bool, optional
        :param name: name
        :type name: str
        :param value: value
        :type value: str
        """
        if encrypt is not SENTINEL:
            self.encrypt = encrypt
        self.name = name
        self.value = value
        self._kwargs = kwargs
