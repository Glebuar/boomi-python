
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class AsyncToken(BaseModel):
    """AsyncToken

    :param token: token
    :type token: str
    """

    def __init__(self, token: str, **kwargs):
        """AsyncToken

        :param token: token
        :type token: str
        """
        self.token = token
        self._kwargs = kwargs
