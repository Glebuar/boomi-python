
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class ConnectorVersion(BaseModel):
    """Each pair of `name` and `version` fields represents a connector listed on the **Runtime Management page > Runtime & Connector Versions** tab.

    :param name: The connector name used by the Runtime, Runtime cluster, or Runtime cloud., defaults to None
    :type name: str, optional
    :param version: The connector version used by the Runtime, Runtime cluster, or Runtime cloud., defaults to None
    :type version: str, optional
    """

    def __init__(self, name: str = SENTINEL, version: str = SENTINEL, **kwargs):
        """Each pair of `name` and `version` fields represents a connector listed on the **Runtime Management page > Runtime & Connector Versions** tab.

        :param name: The connector name used by the Runtime, Runtime cluster, or Runtime cloud., defaults to None
        :type name: str, optional
        :param version: The connector version used by the Runtime, Runtime cluster, or Runtime cloud., defaults to None
        :type version: str, optional
        """
        if name is not SENTINEL:
            self.name = name
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
