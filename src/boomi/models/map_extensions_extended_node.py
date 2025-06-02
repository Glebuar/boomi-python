
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .map_extensions_date_time import MapExtensionsDateTime
from .map_extensions_number import MapExtensionsNumber


@JsonMap(
    {
        "character": "Character",
        "date_time": "DateTime",
        "number": "Number",
        "enforce_unique": "enforceUnique",
        "field_length_validation": "fieldLengthValidation",
        "max_length": "maxLength",
        "min_length": "minLength",
    }
)
class MapExtensionsExtendedNode(BaseModel):
    """MapExtensionsExtendedNode

    :param character: character, defaults to None
    :type character: dict, optional
    :param date_time: date_time, defaults to None
    :type date_time: MapExtensionsDateTime, optional
    :param number: number, defaults to None
    :type number: MapExtensionsNumber, optional
    :param enforce_unique: enforce_unique, defaults to None
    :type enforce_unique: bool, optional
    :param field_length_validation: field_length_validation, defaults to None
    :type field_length_validation: bool, optional
    :param mandatory: mandatory, defaults to None
    :type mandatory: bool, optional
    :param max_length: max_length, defaults to None
    :type max_length: int, optional
    :param min_length: min_length, defaults to None
    :type min_length: int, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        character: dict = SENTINEL,
        date_time: MapExtensionsDateTime = SENTINEL,
        number: MapExtensionsNumber = SENTINEL,
        enforce_unique: bool = SENTINEL,
        field_length_validation: bool = SENTINEL,
        mandatory: bool = SENTINEL,
        max_length: int = SENTINEL,
        min_length: int = SENTINEL,
        name: str = SENTINEL,
        **kwargs,
    ):
        """MapExtensionsExtendedNode

        :param character: character, defaults to None
        :type character: dict, optional
        :param date_time: date_time, defaults to None
        :type date_time: MapExtensionsDateTime, optional
        :param number: number, defaults to None
        :type number: MapExtensionsNumber, optional
        :param enforce_unique: enforce_unique, defaults to None
        :type enforce_unique: bool, optional
        :param field_length_validation: field_length_validation, defaults to None
        :type field_length_validation: bool, optional
        :param mandatory: mandatory, defaults to None
        :type mandatory: bool, optional
        :param max_length: max_length, defaults to None
        :type max_length: int, optional
        :param min_length: min_length, defaults to None
        :type min_length: int, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if character is not SENTINEL:
            self.character = character
        if date_time is not SENTINEL:
            self.date_time = self._define_object(date_time, MapExtensionsDateTime)
        if number is not SENTINEL:
            self.number = self._define_object(number, MapExtensionsNumber)
        if enforce_unique is not SENTINEL:
            self.enforce_unique = enforce_unique
        if field_length_validation is not SENTINEL:
            self.field_length_validation = field_length_validation
        if mandatory is not SENTINEL:
            self.mandatory = mandatory
        if max_length is not SENTINEL:
            self.max_length = max_length
        if min_length is not SENTINEL:
            self.min_length = min_length
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
