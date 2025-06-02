
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class As2BasicAuthInfo(BaseModel):
    """As2BasicAuthInfo

    :param password: password, defaults to None
    :type password: str, optional
    :param user: user, defaults to None
    :type user: str, optional
    """

    def __init__(self, password: str = SENTINEL, user: str = SENTINEL, **kwargs):
        """As2BasicAuthInfo

        :param password: password, defaults to None
        :type password: str, optional
        :param user: user, defaults to None
        :type user: str, optional
        """
        if password is not SENTINEL:
            self.password = password
        if user is not SENTINEL:
            self.user = user
        self._kwargs = kwargs
