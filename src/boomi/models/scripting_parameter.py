
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class DataType(Enum):
    """An enumeration representing different categories.

    :cvar CHARACTER: "CHARACTER"
    :vartype CHARACTER: str
    :cvar DATETIME: "DATETIME"
    :vartype DATETIME: str
    :cvar FLOAT: "FLOAT"
    :vartype FLOAT: str
    :cvar INTEGER: "INTEGER"
    :vartype INTEGER: str
    """

    CHARACTER = "CHARACTER"
    DATETIME = "DATETIME"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DataType._member_map_.values()))


@JsonMap({"data_type": "dataType"})
class ScriptingParameter(BaseModel):
    """ScriptingParameter

    :param data_type: data_type, defaults to None
    :type data_type: DataType, optional
    :param index: index, defaults to None
    :type index: int, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        data_type: DataType = SENTINEL,
        index: int = SENTINEL,
        name: str = SENTINEL,
        **kwargs
    ):
        """ScriptingParameter

        :param data_type: data_type, defaults to None
        :type data_type: DataType, optional
        :param index: index, defaults to None
        :type index: int, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if data_type is not SENTINEL:
            self.data_type = self._enum_matching(
                data_type, DataType.list(), "data_type"
            )
        if index is not SENTINEL:
            self.index = index
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
