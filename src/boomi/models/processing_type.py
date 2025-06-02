
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ProcessingId(Enum):
    """An enumeration representing different categories.

    :cvar D: "D"
    :vartype D: str
    :cvar P: "P"
    :vartype P: str
    :cvar T: "T"
    :vartype T: str
    """

    D = "D"
    P = "P"
    T = "T"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ProcessingId._member_map_.values()))


class ProcessingMode(Enum):
    """An enumeration representing different categories.

    :cvar A: "A"
    :vartype A: str
    :cvar R: "R"
    :vartype R: str
    :cvar I: "I"
    :vartype I: str
    :cvar T: "T"
    :vartype T: str
    :cvar NOTPRESENT: "NOT_PRESENT"
    :vartype NOTPRESENT: str
    """

    A = "A"
    R = "R"
    I = "I"
    T = "T"
    NOTPRESENT = "NOT_PRESENT"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ProcessingMode._member_map_.values()))


@JsonMap({"processing_id": "processingId", "processing_mode": "processingMode"})
class ProcessingType(BaseModel):
    """ProcessingType

    :param processing_id: processing_id, defaults to None
    :type processing_id: ProcessingId, optional
    :param processing_mode: processing_mode, defaults to None
    :type processing_mode: ProcessingMode, optional
    """

    def __init__(
        self,
        processing_id: ProcessingId = SENTINEL,
        processing_mode: ProcessingMode = SENTINEL,
        **kwargs
    ):
        """ProcessingType

        :param processing_id: processing_id, defaults to None
        :type processing_id: ProcessingId, optional
        :param processing_mode: processing_mode, defaults to None
        :type processing_mode: ProcessingMode, optional
        """
        if processing_id is not SENTINEL:
            self.processing_id = self._enum_matching(
                processing_id, ProcessingId.list(), "processing_id"
            )
        if processing_mode is not SENTINEL:
            self.processing_mode = self._enum_matching(
                processing_mode, ProcessingMode.list(), "processing_mode"
            )
        self._kwargs = kwargs
