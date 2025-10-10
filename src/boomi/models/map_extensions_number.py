
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"implied_decimal": "impliedDecimal"})
class MapExtensionsNumber(BaseModel):
    """MapExtensionsNumber

    :param format: format, defaults to None
    :type format: str, optional
    :param implied_decimal: implied_decimal, defaults to None
    :type implied_decimal: int, optional
    :param signed: signed, defaults to None
    :type signed: bool, optional
    """

    def __init__(
        self,
        format: str = SENTINEL,
        implied_decimal: int = SENTINEL,
        signed: bool = SENTINEL,
        **kwargs
    ):
        """MapExtensionsNumber

        :param format: format, defaults to None
        :type format: str, optional
        :param implied_decimal: implied_decimal, defaults to None
        :type implied_decimal: int, optional
        :param signed: signed, defaults to None
        :type signed: bool, optional
        """
        if format is not SENTINEL:
            self.format = format
        if implied_decimal is not SENTINEL:
            self.implied_decimal = implied_decimal
        if signed is not SENTINEL:
            self.signed = signed
        self._kwargs = kwargs
