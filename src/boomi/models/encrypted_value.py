
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"is_set": "isSet"})
class EncryptedValue(BaseModel):
    """EncryptedValue

    :param is_set: is_set, defaults to None
    :type is_set: bool, optional
    :param path: path, defaults to None
    :type path: str, optional
    """

    def __init__(self, is_set: bool = SENTINEL, path: str = SENTINEL, **kwargs):
        """EncryptedValue

        :param is_set: is_set, defaults to None
        :type is_set: bool, optional
        :param path: path, defaults to None
        :type path: str, optional
        """
        if is_set is not SENTINEL:
            self.is_set = is_set
        if path is not SENTINEL:
            self.path = path
        self._kwargs = kwargs
