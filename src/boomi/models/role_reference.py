
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "id_": "id",
        "name": "name",
    }
)
class RoleReference(BaseModel):
    """RoleReference

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, id_: str = SENTINEL, name: str = SENTINEL, **kwargs):
        """RoleReference

        :param id_: id_, defaults to None
        :type id_: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
