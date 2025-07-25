
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class SecretsManagerRefreshResponse(BaseModel):
    """SecretsManagerRefreshResponse

    :param message: message, defaults to None
    :type message: str, optional
    """

    def __init__(self, message: str = SENTINEL, **kwargs):
        """SecretsManagerRefreshResponse

        :param message: message, defaults to None
        :type message: str, optional
        """
        if message is not SENTINEL:
            self.message = message
        self._kwargs = kwargs
