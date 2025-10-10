
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class SegmentTerminatorValue(Enum):
    """An enumeration representing different categories.

    :cvar NEWLINE: "newline"
    :vartype NEWLINE: str
    :cvar SINGLEQUOTE: "singlequote"
    :vartype SINGLEQUOTE: str
    :cvar TILDE: "tilde"
    :vartype TILDE: str
    :cvar CARRIAGERETURN: "carriagereturn"
    :vartype CARRIAGERETURN: str
    :cvar BYTECHARACTER: "bytecharacter"
    :vartype BYTECHARACTER: str
    :cvar OTHERCHARACTER: "othercharacter"
    :vartype OTHERCHARACTER: str
    """

    NEWLINE = "newline"
    SINGLEQUOTE = "singlequote"
    TILDE = "tilde"
    CARRIAGERETURN = "carriagereturn"
    BYTECHARACTER = "bytecharacter"
    OTHERCHARACTER = "othercharacter"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SegmentTerminatorValue._member_map_.values())
        )


@JsonMap(
    {
        "segment_terminator_special": "segmentTerminatorSpecial",
        "segment_terminator_value": "segmentTerminatorValue",
    }
)
class EdiSegmentTerminator(BaseModel):
    """EdiSegmentTerminator

    :param segment_terminator_special: segment_terminator_special, defaults to None
    :type segment_terminator_special: str, optional
    :param segment_terminator_value: segment_terminator_value, defaults to None
    :type segment_terminator_value: SegmentTerminatorValue, optional
    """

    def __init__(
        self,
        segment_terminator_special: str = SENTINEL,
        segment_terminator_value: SegmentTerminatorValue = SENTINEL,
        **kwargs
    ):
        """EdiSegmentTerminator

        :param segment_terminator_special: segment_terminator_special, defaults to None
        :type segment_terminator_special: str, optional
        :param segment_terminator_value: segment_terminator_value, defaults to None
        :type segment_terminator_value: SegmentTerminatorValue, optional
        """
        if segment_terminator_special is not SENTINEL:
            self.segment_terminator_special = segment_terminator_special
        if segment_terminator_value is not SENTINEL:
            self.segment_terminator_value = self._enum_matching(
                segment_terminator_value,
                SegmentTerminatorValue.list(),
                "segment_terminator_value",
            )
        self._kwargs = kwargs
