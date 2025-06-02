
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .x12_control_info import X12ControlInfo
from .x12_options import X12Options


@JsonMap({"x12_control_info": "X12ControlInfo", "x12_options": "X12Options"})
class X12PartnerInfo(BaseModel):
    """X12PartnerInfo

    :param x12_control_info: x12_control_info, defaults to None
    :type x12_control_info: X12ControlInfo, optional
    :param x12_options: x12_options, defaults to None
    :type x12_options: X12Options, optional
    """

    def __init__(
        self,
        x12_control_info: X12ControlInfo = SENTINEL,
        x12_options: X12Options = SENTINEL,
        **kwargs,
    ):
        """X12PartnerInfo

        :param x12_control_info: x12_control_info, defaults to None
        :type x12_control_info: X12ControlInfo, optional
        :param x12_options: x12_options, defaults to None
        :type x12_options: X12Options, optional
        """
        if x12_control_info is not SENTINEL:
            self.x12_control_info = self._define_object(
                x12_control_info, X12ControlInfo
            )
        if x12_options is not SENTINEL:
            self.x12_options = self._define_object(x12_options, X12Options)
        self._kwargs = kwargs
