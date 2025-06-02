
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class PropertyPair(BaseModel):
    """PropertyPair

    :param encrypted: encrypted, defaults to None
    :type encrypted: bool, optional
    :param key: key, defaults to None
    :type key: str, optional
    :param value: value, defaults to None
    :type value: str, optional
    """

    def __init__(
        self,
        encrypted: bool = SENTINEL,
        key: str = SENTINEL,
        value: str = SENTINEL,
        **kwargs
    ):
        """PropertyPair

        :param encrypted: encrypted, defaults to None
        :type encrypted: bool, optional
        :param key: key, defaults to None
        :type key: str, optional
        :param value: value, defaults to None
        :type value: str, optional
        """
        if encrypted is not SENTINEL:
            self.encrypted = encrypted
        if key is not SENTINEL:
            self.key = key
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs
