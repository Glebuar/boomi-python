
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .stx_control_info import StxControlInfo


@JsonMap({"stx_control_info": "STXControlInfo"})
class TradacomsControlInfo(BaseModel):
    """TradacomsControlInfo

    :param stx_control_info: stx_control_info, defaults to None
    :type stx_control_info: StxControlInfo, optional
    """

    def __init__(self, stx_control_info: StxControlInfo = SENTINEL, **kwargs):
        """TradacomsControlInfo

        :param stx_control_info: stx_control_info, defaults to None
        :type stx_control_info: StxControlInfo, optional
        """
        if stx_control_info is not SENTINEL:
            self.stx_control_info = self._define_object(
                stx_control_info, StxControlInfo
            )
        self._kwargs = kwargs
