
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class CustomTrackedFieldType(Enum):
    """An enumeration representing different categories.

    :cvar CHARACTER: "character"
    :vartype CHARACTER: str
    :cvar DATETIME: "datetime"
    :vartype DATETIME: str
    :cvar NUMBER: "number"
    :vartype NUMBER: str
    """

    CHARACTER = "character"
    DATETIME = "datetime"
    NUMBER = "number"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, CustomTrackedFieldType._member_map_.values())
        )


@JsonMap({"type_": "type"})
class CustomTrackedField(BaseModel):
    """CustomTrackedField

    :param label: The display name of the custom tracked field., defaults to None
    :type label: str, optional
    :param position: The display position of the custom tracked field., defaults to None
    :type position: int, optional
    :param type_: The type of custom tracked field. Allowed values include character, datetime, and number., defaults to None
    :type type_: CustomTrackedFieldType, optional
    """

    def __init__(
        self,
        label: str = SENTINEL,
        position: int = SENTINEL,
        type_: CustomTrackedFieldType = SENTINEL,
        **kwargs
    ):
        """CustomTrackedField

        :param label: The display name of the custom tracked field., defaults to None
        :type label: str, optional
        :param position: The display position of the custom tracked field., defaults to None
        :type position: int, optional
        :param type_: The type of custom tracked field. Allowed values include character, datetime, and number., defaults to None
        :type type_: CustomTrackedFieldType, optional
        """
        if label is not SENTINEL:
            self.label = label
        if position is not SENTINEL:
            self.position = position
        if type_ is not SENTINEL:
            self.type_ = self._enum_matching(
                type_, CustomTrackedFieldType.list(), "type_"
            )
        self._kwargs = kwargs
