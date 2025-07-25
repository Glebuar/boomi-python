
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .edifact_partner_info import EdifactPartnerInfo
from .hl7_partner_info import Hl7PartnerInfo
from .odette_partner_info import OdettePartnerInfo
from .rosetta_net_partner_info import RosettaNetPartnerInfo
from .tradacoms_partner_info import TradacomsPartnerInfo
from .x12_partner_info import X12PartnerInfo


@JsonMap(
    {
        "custom_partner_info": "CustomPartnerInfo",
        "edifact_partner_info": "EdifactPartnerInfo",
        "hl7_partner_info": "HL7PartnerInfo",
        "odette_partner_info": "OdettePartnerInfo",
        "rosetta_net_partner_info": "RosettaNetPartnerInfo",
        "tradacoms_partner_info": "TradacomsPartnerInfo",
        "x12_partner_info": "X12PartnerInfo",
    }
)
class PartnerInfo(BaseModel):
    """PartnerInfo

    :param custom_partner_info: custom_partner_info, defaults to None
    :type custom_partner_info: dict, optional
    :param edifact_partner_info: edifact_partner_info, defaults to None
    :type edifact_partner_info: EdifactPartnerInfo, optional
    :param hl7_partner_info: hl7_partner_info, defaults to None
    :type hl7_partner_info: Hl7PartnerInfo, optional
    :param odette_partner_info: odette_partner_info, defaults to None
    :type odette_partner_info: OdettePartnerInfo, optional
    :param rosetta_net_partner_info: rosetta_net_partner_info, defaults to None
    :type rosetta_net_partner_info: RosettaNetPartnerInfo, optional
    :param tradacoms_partner_info: tradacoms_partner_info, defaults to None
    :type tradacoms_partner_info: TradacomsPartnerInfo, optional
    :param x12_partner_info: x12_partner_info, defaults to None
    :type x12_partner_info: X12PartnerInfo, optional
    """

    def __init__(
        self,
        custom_partner_info: dict = SENTINEL,
        edifact_partner_info: EdifactPartnerInfo = SENTINEL,
        hl7_partner_info: Hl7PartnerInfo = SENTINEL,
        odette_partner_info: OdettePartnerInfo = SENTINEL,
        rosetta_net_partner_info: RosettaNetPartnerInfo = SENTINEL,
        tradacoms_partner_info: TradacomsPartnerInfo = SENTINEL,
        x12_partner_info: X12PartnerInfo = SENTINEL,
        **kwargs,
    ):
        """PartnerInfo

        :param custom_partner_info: custom_partner_info, defaults to None
        :type custom_partner_info: dict, optional
        :param edifact_partner_info: edifact_partner_info, defaults to None
        :type edifact_partner_info: EdifactPartnerInfo, optional
        :param hl7_partner_info: hl7_partner_info, defaults to None
        :type hl7_partner_info: Hl7PartnerInfo, optional
        :param odette_partner_info: odette_partner_info, defaults to None
        :type odette_partner_info: OdettePartnerInfo, optional
        :param rosetta_net_partner_info: rosetta_net_partner_info, defaults to None
        :type rosetta_net_partner_info: RosettaNetPartnerInfo, optional
        :param tradacoms_partner_info: tradacoms_partner_info, defaults to None
        :type tradacoms_partner_info: TradacomsPartnerInfo, optional
        :param x12_partner_info: x12_partner_info, defaults to None
        :type x12_partner_info: X12PartnerInfo, optional
        """
        if custom_partner_info is not SENTINEL:
            self.custom_partner_info = custom_partner_info
        if edifact_partner_info is not SENTINEL:
            self.edifact_partner_info = self._define_object(
                edifact_partner_info, EdifactPartnerInfo
            )
        if hl7_partner_info is not SENTINEL:
            self.hl7_partner_info = self._define_object(
                hl7_partner_info, Hl7PartnerInfo
            )
        if odette_partner_info is not SENTINEL:
            self.odette_partner_info = self._define_object(
                odette_partner_info, OdettePartnerInfo
            )
        if rosetta_net_partner_info is not SENTINEL:
            self.rosetta_net_partner_info = self._define_object(
                rosetta_net_partner_info, RosettaNetPartnerInfo
            )
        if tradacoms_partner_info is not SENTINEL:
            self.tradacoms_partner_info = self._define_object(
                tradacoms_partner_info, TradacomsPartnerInfo
            )
        if x12_partner_info is not SENTINEL:
            self.x12_partner_info = self._define_object(
                x12_partner_info, X12PartnerInfo
            )
        self._kwargs = kwargs
