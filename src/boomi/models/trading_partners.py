
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .trading_partner import TradingPartner


@JsonMap({"trading_partner": "tradingPartner"})
class TradingPartners(BaseModel):
    """TradingPartners

    :param trading_partner: trading_partner, defaults to None
    :type trading_partner: List[TradingPartner], optional
    """

    def __init__(self, trading_partner: List[TradingPartner] = SENTINEL, **kwargs):
        """TradingPartners

        :param trading_partner: trading_partner, defaults to None
        :type trading_partner: List[TradingPartner], optional
        """
        if trading_partner is not SENTINEL:
            self.trading_partner = self._define_list(trading_partner, TradingPartner)
        self._kwargs = kwargs
