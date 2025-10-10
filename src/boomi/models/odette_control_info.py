
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .odette_unb_control_info import OdetteUnbControlInfo
from .odette_unh_control_info import OdetteUnhControlInfo


@JsonMap(
    {
        "odette_unb_control_info": "OdetteUNBControlInfo",
        "odette_unh_control_info": "OdetteUNHControlInfo",
    }
)
class OdetteControlInfo(BaseModel):
    """OdetteControlInfo

    :param odette_unb_control_info: odette_unb_control_info
    :type odette_unb_control_info: OdetteUnbControlInfo
    :param odette_unh_control_info: odette_unh_control_info
    :type odette_unh_control_info: OdetteUnhControlInfo
    """

    def __init__(
        self,
        odette_unb_control_info: OdetteUnbControlInfo,
        odette_unh_control_info: OdetteUnhControlInfo,
        **kwargs,
    ):
        """OdetteControlInfo

        :param odette_unb_control_info: odette_unb_control_info
        :type odette_unb_control_info: OdetteUnbControlInfo
        :param odette_unh_control_info: odette_unh_control_info
        :type odette_unh_control_info: OdetteUnhControlInfo
        """
        self.odette_unb_control_info = self._define_object(
            odette_unb_control_info, OdetteUnbControlInfo
        )
        self.odette_unh_control_info = self._define_object(
            odette_unh_control_info, OdetteUnhControlInfo
        )
        self._kwargs = kwargs
