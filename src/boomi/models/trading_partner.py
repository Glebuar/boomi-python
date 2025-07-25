
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .trading_partner_category import TradingPartnerCategory


@JsonMap({"id_": "id"})
class TradingPartner(BaseModel):
    """TradingPartner

    :param category: category, defaults to None
    :type category: List[TradingPartnerCategory], optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        category: List[TradingPartnerCategory] = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        **kwargs,
    ):
        """TradingPartner

        :param category: category, defaults to None
        :type category: List[TradingPartnerCategory], optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param name: name, defaults to None
        :type name: str, optional
        """
        if category is not SENTINEL:
            self.category = self._define_list(category, TradingPartnerCategory)
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
