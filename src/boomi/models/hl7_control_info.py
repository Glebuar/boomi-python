
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .msh_control_info import MshControlInfo


@JsonMap({"msh_control_info": "MSHControlInfo"})
class Hl7ControlInfo(BaseModel):
    """Hl7ControlInfo

    :param msh_control_info: msh_control_info
    :type msh_control_info: MshControlInfo
    """

    def __init__(self, msh_control_info: MshControlInfo, **kwargs):
        """Hl7ControlInfo

        :param msh_control_info: msh_control_info
        :type msh_control_info: MshControlInfo
        """
        self.msh_control_info = self._define_object(msh_control_info, MshControlInfo)
        self._kwargs = kwargs
