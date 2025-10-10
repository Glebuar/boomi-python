
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class DelimiterValue(Enum):
    """An enumeration representing different categories.

    :cvar STARDELIMITED: "stardelimited"
    :vartype STARDELIMITED: str
    :cvar COMMADELIMITED: "commadelimited"
    :vartype COMMADELIMITED: str
    :cvar TABDELIMITED: "tabdelimited"
    :vartype TABDELIMITED: str
    :cvar TICKDELIMITED: "tickdelimited"
    :vartype TICKDELIMITED: str
    :cvar BARDELIMITED: "bardelimited"
    :vartype BARDELIMITED: str
    :cvar PLUSDELIMITED: "plusdelimited"
    :vartype PLUSDELIMITED: str
    :cvar COLONDELIMITED: "colondelimited"
    :vartype COLONDELIMITED: str
    :cvar CARATDELIMITED: "caratdelimited"
    :vartype CARATDELIMITED: str
    :cvar AMPERSANDDELIMITED: "ampersanddelimited"
    :vartype AMPERSANDDELIMITED: str
    :cvar BYTECHARACTER: "bytecharacter"
    :vartype BYTECHARACTER: str
    :cvar OTHERCHARACTER: "othercharacter"
    :vartype OTHERCHARACTER: str
    """

    STARDELIMITED = "stardelimited"
    COMMADELIMITED = "commadelimited"
    TABDELIMITED = "tabdelimited"
    TICKDELIMITED = "tickdelimited"
    BARDELIMITED = "bardelimited"
    PLUSDELIMITED = "plusdelimited"
    COLONDELIMITED = "colondelimited"
    CARATDELIMITED = "caratdelimited"
    AMPERSANDDELIMITED = "ampersanddelimited"
    BYTECHARACTER = "bytecharacter"
    OTHERCHARACTER = "othercharacter"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DelimiterValue._member_map_.values()))


@JsonMap({"delimiter_special": "delimiterSpecial", "delimiter_value": "delimiterValue"})
class EdiDelimiter(BaseModel):
    """EdiDelimiter

    :param delimiter_special: delimiter_special, defaults to None
    :type delimiter_special: str, optional
    :param delimiter_value: delimiter_value, defaults to None
    :type delimiter_value: DelimiterValue, optional
    """

    def __init__(
        self,
        delimiter_special: str = SENTINEL,
        delimiter_value: DelimiterValue = SENTINEL,
        **kwargs
    ):
        """EdiDelimiter

        :param delimiter_special: delimiter_special, defaults to None
        :type delimiter_special: str, optional
        :param delimiter_value: delimiter_value, defaults to None
        :type delimiter_value: DelimiterValue, optional
        """
        if delimiter_special is not SENTINEL:
            self.delimiter_special = delimiter_special
        if delimiter_value is not SENTINEL:
            self.delimiter_value = self._enum_matching(
                delimiter_value, DelimiterValue.list(), "delimiter_value"
            )
        self._kwargs = kwargs
