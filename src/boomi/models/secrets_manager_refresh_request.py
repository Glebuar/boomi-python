
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class Provider(Enum):
    """An enumeration representing different categories.

    :cvar AWS: "AWS"
    :vartype AWS: str
    :cvar AZURE: "AZURE"
    :vartype AZURE: str
    """

    AWS = "AWS"
    AZURE = "AZURE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Provider._member_map_.values()))


@JsonMap({})
class SecretsManagerRefreshRequest(BaseModel):
    """SecretsManagerRefreshRequest

    :param provider: provider, defaults to None
    :type provider: Provider, optional
    """

    def __init__(self, provider: Provider = SENTINEL, **kwargs):
        """SecretsManagerRefreshRequest

        :param provider: provider, defaults to None
        :type provider: Provider, optional
        """
        if provider is not SENTINEL:
            self.provider = self._enum_matching(provider, Provider.list(), "provider")
        self._kwargs = kwargs
