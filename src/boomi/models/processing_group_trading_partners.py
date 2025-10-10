
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .processing_group_trading_partner import ProcessingGroupTradingPartner


@JsonMap({"trading_partner": "TradingPartner"})
class ProcessingGroupTradingPartners(BaseModel):
    """ProcessingGroupTradingPartners

    :param trading_partner: trading_partner, defaults to None
    :type trading_partner: List[ProcessingGroupTradingPartner], optional
    """

    def __init__(
        self, trading_partner: List[ProcessingGroupTradingPartner] = SENTINEL, **kwargs
    ):
        """ProcessingGroupTradingPartners

        :param trading_partner: trading_partner, defaults to None
        :type trading_partner: List[ProcessingGroupTradingPartner], optional
        """
        if trading_partner is not SENTINEL:
            self.trading_partner = self._define_list(
                trading_partner, ProcessingGroupTradingPartner
            )
        self._kwargs = kwargs
