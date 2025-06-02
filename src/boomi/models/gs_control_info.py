
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class Respagencycode(Enum):
    """An enumeration representing different categories.

    :cvar T: "T"
    :vartype T: str
    :cvar X: "X"
    :vartype X: str
    """

    T = "T"
    X = "X"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Respagencycode._member_map_.values()))


@JsonMap({"gs_version": "gsVersion"})
class GsControlInfo(BaseModel):
    """GsControlInfo

    :param applicationcode: applicationcode, defaults to None
    :type applicationcode: str, optional
    :param gs_version: gs_version, defaults to None
    :type gs_version: str, optional
    :param respagencycode: respagencycode, defaults to None
    :type respagencycode: Respagencycode, optional
    """

    def __init__(
        self,
        applicationcode: str = SENTINEL,
        gs_version: str = SENTINEL,
        respagencycode: Respagencycode = SENTINEL,
        **kwargs
    ):
        """GsControlInfo

        :param applicationcode: applicationcode, defaults to None
        :type applicationcode: str, optional
        :param gs_version: gs_version, defaults to None
        :type gs_version: str, optional
        :param respagencycode: respagencycode, defaults to None
        :type respagencycode: Respagencycode, optional
        """
        if applicationcode is not SENTINEL:
            self.applicationcode = applicationcode
        if gs_version is not SENTINEL:
            self.gs_version = gs_version
        if respagencycode is not SENTINEL:
            self.respagencycode = self._enum_matching(
                respagencycode, Respagencycode.list(), "respagencycode"
            )
        self._kwargs = kwargs
