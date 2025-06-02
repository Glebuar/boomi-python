
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .hl7_control_info import Hl7ControlInfo
from .hl7_options import Hl7Options


@JsonMap({"hl7_control_info": "HL7ControlInfo", "hl7_options": "HL7Options"})
class Hl7PartnerInfo(BaseModel):
    """Hl7PartnerInfo

    :param hl7_control_info: hl7_control_info, defaults to None
    :type hl7_control_info: Hl7ControlInfo, optional
    :param hl7_options: hl7_options, defaults to None
    :type hl7_options: Hl7Options, optional
    """

    def __init__(
        self,
        hl7_control_info: Hl7ControlInfo = SENTINEL,
        hl7_options: Hl7Options = SENTINEL,
        **kwargs,
    ):
        """Hl7PartnerInfo

        :param hl7_control_info: hl7_control_info, defaults to None
        :type hl7_control_info: Hl7ControlInfo, optional
        :param hl7_options: hl7_options, defaults to None
        :type hl7_options: Hl7Options, optional
        """
        if hl7_control_info is not SENTINEL:
            self.hl7_control_info = self._define_object(
                hl7_control_info, Hl7ControlInfo
            )
        if hl7_options is not SENTINEL:
            self.hl7_options = self._define_object(hl7_options, Hl7Options)
        self._kwargs = kwargs
