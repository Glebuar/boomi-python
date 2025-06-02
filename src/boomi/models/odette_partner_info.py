
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .odette_control_info import OdetteControlInfo
from .odette_options import OdetteOptions


@JsonMap(
    {"odette_control_info": "OdetteControlInfo", "odette_options": "OdetteOptions"}
)
class OdettePartnerInfo(BaseModel):
    """OdettePartnerInfo

    :param odette_control_info: odette_control_info
    :type odette_control_info: OdetteControlInfo
    :param odette_options: odette_options
    :type odette_options: OdetteOptions
    """

    def __init__(
        self,
        odette_control_info: OdetteControlInfo,
        odette_options: OdetteOptions,
        **kwargs,
    ):
        """OdettePartnerInfo

        :param odette_control_info: odette_control_info
        :type odette_control_info: OdetteControlInfo
        :param odette_options: odette_options
        :type odette_options: OdetteOptions
        """
        self.odette_control_info = self._define_object(
            odette_control_info, OdetteControlInfo
        )
        self.odette_options = self._define_object(odette_options, OdetteOptions)
        self._kwargs = kwargs
