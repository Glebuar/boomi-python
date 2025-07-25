
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .unb_control_info import UnbControlInfo
from .ung_control_info import UngControlInfo
from .unh_control_info import UnhControlInfo


@JsonMap(
    {
        "unb_control_info": "UNBControlInfo",
        "ung_control_info": "UNGControlInfo",
        "unh_control_info": "UNHControlInfo",
    }
)
class EdifactControlInfo(BaseModel):
    """EdifactControlInfo

    :param unb_control_info: unb_control_info
    :type unb_control_info: UnbControlInfo
    :param ung_control_info: ung_control_info, defaults to None
    :type ung_control_info: UngControlInfo, optional
    :param unh_control_info: unh_control_info
    :type unh_control_info: UnhControlInfo
    """

    def __init__(
        self,
        unb_control_info: UnbControlInfo,
        unh_control_info: UnhControlInfo,
        ung_control_info: UngControlInfo = SENTINEL,
        **kwargs,
    ):
        """EdifactControlInfo

        :param unb_control_info: unb_control_info
        :type unb_control_info: UnbControlInfo
        :param ung_control_info: ung_control_info, defaults to None
        :type ung_control_info: UngControlInfo, optional
        :param unh_control_info: unh_control_info
        :type unh_control_info: UnhControlInfo
        """
        self.unb_control_info = self._define_object(unb_control_info, UnbControlInfo)
        if ung_control_info is not SENTINEL:
            self.ung_control_info = self._define_object(
                ung_control_info, UngControlInfo
            )
        self.unh_control_info = self._define_object(unh_control_info, UnhControlInfo)
        self._kwargs = kwargs
