
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .processing_group_partner_route import ProcessingGroupPartnerRoute


@JsonMap({"partner_route": "PartnerRoute", "process_id": "processId"})
class ProcessingGroupPartnerBasedRouting(BaseModel):
    """ProcessingGroupPartnerBasedRouting

    :param partner_route: partner_route, defaults to None
    :type partner_route: List[ProcessingGroupPartnerRoute], optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        partner_route: List[ProcessingGroupPartnerRoute] = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs,
    ):
        """ProcessingGroupPartnerBasedRouting

        :param partner_route: partner_route, defaults to None
        :type partner_route: List[ProcessingGroupPartnerRoute], optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        """
        if partner_route is not SENTINEL:
            self.partner_route = self._define_list(
                partner_route, ProcessingGroupPartnerRoute
            )
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
