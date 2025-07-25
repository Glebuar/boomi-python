
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .processing_group_partner_standard_route import ProcessingGroupPartnerStandardRoute


@JsonMap(
    {
        "standard_route": "StandardRoute",
        "process_id": "processId",
        "trading_partner_id": "tradingPartnerId",
    }
)
class ProcessingGroupPartnerRoute(BaseModel):
    """ProcessingGroupPartnerRoute

    :param standard_route: standard_route, defaults to None
    :type standard_route: List[ProcessingGroupPartnerStandardRoute], optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    :param trading_partner_id: trading_partner_id, defaults to None
    :type trading_partner_id: str, optional
    """

    def __init__(
        self,
        standard_route: List[ProcessingGroupPartnerStandardRoute] = SENTINEL,
        process_id: str = SENTINEL,
        trading_partner_id: str = SENTINEL,
        **kwargs,
    ):
        """ProcessingGroupPartnerRoute

        :param standard_route: standard_route, defaults to None
        :type standard_route: List[ProcessingGroupPartnerStandardRoute], optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        :param trading_partner_id: trading_partner_id, defaults to None
        :type trading_partner_id: str, optional
        """
        if standard_route is not SENTINEL:
            self.standard_route = self._define_list(
                standard_route, ProcessingGroupPartnerStandardRoute
            )
        if process_id is not SENTINEL:
            self.process_id = process_id
        if trading_partner_id is not SENTINEL:
            self.trading_partner_id = trading_partner_id
        self._kwargs = kwargs
