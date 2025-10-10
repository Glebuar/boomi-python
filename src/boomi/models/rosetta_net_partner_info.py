
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .rosetta_net_control_info import RosettaNetControlInfo
from .rosetta_net_message_options import RosettaNetMessageOptions
from .rosetta_net_options import RosettaNetOptions


@JsonMap(
    {
        "rosetta_net_control_info": "RosettaNetControlInfo",
        "rosetta_net_message_options": "RosettaNetMessageOptions",
        "rosetta_net_options": "RosettaNetOptions",
    }
)
class RosettaNetPartnerInfo(BaseModel):
    """RosettaNetPartnerInfo

    :param rosetta_net_control_info: rosetta_net_control_info, defaults to None
    :type rosetta_net_control_info: RosettaNetControlInfo, optional
    :param rosetta_net_message_options: rosetta_net_message_options, defaults to None
    :type rosetta_net_message_options: RosettaNetMessageOptions, optional
    :param rosetta_net_options: rosetta_net_options, defaults to None
    :type rosetta_net_options: RosettaNetOptions, optional
    """

    def __init__(
        self,
        rosetta_net_control_info: RosettaNetControlInfo = SENTINEL,
        rosetta_net_message_options: RosettaNetMessageOptions = SENTINEL,
        rosetta_net_options: RosettaNetOptions = SENTINEL,
        **kwargs,
    ):
        """RosettaNetPartnerInfo

        :param rosetta_net_control_info: rosetta_net_control_info, defaults to None
        :type rosetta_net_control_info: RosettaNetControlInfo, optional
        :param rosetta_net_message_options: rosetta_net_message_options, defaults to None
        :type rosetta_net_message_options: RosettaNetMessageOptions, optional
        :param rosetta_net_options: rosetta_net_options, defaults to None
        :type rosetta_net_options: RosettaNetOptions, optional
        """
        if rosetta_net_control_info is not SENTINEL:
            self.rosetta_net_control_info = self._define_object(
                rosetta_net_control_info, RosettaNetControlInfo
            )
        if rosetta_net_message_options is not SENTINEL:
            self.rosetta_net_message_options = self._define_object(
                rosetta_net_message_options, RosettaNetMessageOptions
            )
        if rosetta_net_options is not SENTINEL:
            self.rosetta_net_options = self._define_object(
                rosetta_net_options, RosettaNetOptions
            )
        self._kwargs = kwargs
