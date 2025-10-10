
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"convert_from": "convertFrom", "convert_to": "convertTo"})
class MapExtensionsJapaneseCharacterConversion(BaseModel):
    """MapExtensionsJapaneseCharacterConversion

    :param convert_from: convert_from, defaults to None
    :type convert_from: str, optional
    :param convert_to: convert_to, defaults to None
    :type convert_to: str, optional
    """

    def __init__(
        self, convert_from: str = SENTINEL, convert_to: str = SENTINEL, **kwargs
    ):
        """MapExtensionsJapaneseCharacterConversion

        :param convert_from: convert_from, defaults to None
        :type convert_from: str, optional
        :param convert_to: convert_to, defaults to None
        :type convert_to: str, optional
        """
        if convert_from is not SENTINEL:
            self.convert_from = convert_from
        if convert_to is not SENTINEL:
            self.convert_to = convert_to
        self._kwargs = kwargs
