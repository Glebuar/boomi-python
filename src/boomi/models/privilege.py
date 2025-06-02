
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class Privilege(BaseModel):
    """Privilege

    :param name: name
    :type name: str
    """

    def __init__(self, name: str, **kwargs):
        """Privilege

        :param name: name
        :type name: str
        """
        self.name = name
        self._kwargs = kwargs
