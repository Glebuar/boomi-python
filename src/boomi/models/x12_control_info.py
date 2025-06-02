
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .gs_control_info import GsControlInfo
from .isa_control_info import IsaControlInfo


@JsonMap({"gs_control_info": "GSControlInfo", "isa_control_info": "isaControlInfo"})
class X12ControlInfo(BaseModel):
    """X12ControlInfo

    :param gs_control_info: gs_control_info, defaults to None
    :type gs_control_info: GsControlInfo, optional
    :param isa_control_info: isa_control_info, defaults to None
    :type isa_control_info: IsaControlInfo, optional
    """

    def __init__(
        self,
        gs_control_info: GsControlInfo = SENTINEL,
        isa_control_info: IsaControlInfo = SENTINEL,
        **kwargs,
    ):
        """X12ControlInfo

        :param gs_control_info: gs_control_info, defaults to None
        :type gs_control_info: GsControlInfo, optional
        :param isa_control_info: isa_control_info, defaults to None
        :type isa_control_info: IsaControlInfo, optional
        """
        if gs_control_info is not SENTINEL:
            self.gs_control_info = self._define_object(gs_control_info, GsControlInfo)
        if isa_control_info is not SENTINEL:
            self.isa_control_info = self._define_object(
                isa_control_info, IsaControlInfo
            )
        self._kwargs = kwargs
