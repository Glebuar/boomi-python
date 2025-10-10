
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .tradacoms_control_info import TradacomsControlInfo
from .tradacoms_options import TradacomsOptions


@JsonMap(
    {
        "tradacoms_control_info": "TradacomsControlInfo",
        "tradacoms_options": "TradacomsOptions",
    }
)
class TradacomsPartnerInfo(BaseModel):
    """TradacomsPartnerInfo

    :param tradacoms_control_info: tradacoms_control_info, defaults to None
    :type tradacoms_control_info: TradacomsControlInfo, optional
    :param tradacoms_options: tradacoms_options, defaults to None
    :type tradacoms_options: TradacomsOptions, optional
    """

    def __init__(
        self,
        tradacoms_control_info: TradacomsControlInfo = SENTINEL,
        tradacoms_options: TradacomsOptions = SENTINEL,
        **kwargs,
    ):
        """TradacomsPartnerInfo

        :param tradacoms_control_info: tradacoms_control_info, defaults to None
        :type tradacoms_control_info: TradacomsControlInfo, optional
        :param tradacoms_options: tradacoms_options, defaults to None
        :type tradacoms_options: TradacomsOptions, optional
        """
        if tradacoms_control_info is not SENTINEL:
            self.tradacoms_control_info = self._define_object(
                tradacoms_control_info, TradacomsControlInfo
            )
        if tradacoms_options is not SENTINEL:
            self.tradacoms_options = self._define_object(
                tradacoms_options, TradacomsOptions
            )
        self._kwargs = kwargs
