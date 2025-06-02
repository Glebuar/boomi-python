
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class Molecule(BaseModel):
    """Indicates the number of Runtime clusters available on an account and the number of Runtime clusters currently in use.

    :param purchased: purchased, defaults to None
    :type purchased: int, optional
    :param used: used, defaults to None
    :type used: int, optional
    """

    def __init__(self, purchased: int = SENTINEL, used: int = SENTINEL, **kwargs):
        """Indicates the number of Runtime clusters available on an account and the number of Runtime clusters currently in use.

        :param purchased: purchased, defaults to None
        :type purchased: int, optional
        :param used: used, defaults to None
        :type used: int, optional
        """
        if purchased is not SENTINEL:
            self.purchased = purchased
        if used is not SENTINEL:
            self.used = used
        self._kwargs = kwargs
