
from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .bulk_id import BulkId


class TradingPartnerComponentBulkRequestType(Enum):
    """An enumeration representing different categories.

    :cvar GET: "GET"
    :vartype GET: str
    :cvar DELETE: "DELETE"
    :vartype DELETE: str
    :cvar UPDATE: "UPDATE"
    :vartype UPDATE: str
    :cvar CREATE: "CREATE"
    :vartype CREATE: str
    """

    GET = "GET"
    DELETE = "DELETE"
    UPDATE = "UPDATE"
    CREATE = "CREATE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                TradingPartnerComponentBulkRequestType._member_map_.values(),
            )
        )


@JsonMap({"type_": "type"})
class TradingPartnerComponentBulkRequest(BaseModel):
    """TradingPartnerComponentBulkRequest

    :param request: request, defaults to None
    :type request: List[BulkId], optional
    :param type_: type_, defaults to None
    :type type_: TradingPartnerComponentBulkRequestType, optional
    """

    def __init__(
        self,
        request: List[BulkId] = SENTINEL,
        type_: TradingPartnerComponentBulkRequestType = SENTINEL,
        **kwargs,
    ):
        """TradingPartnerComponentBulkRequest

        :param request: request, defaults to None
        :type request: List[BulkId], optional
        :param type_: type_, defaults to None
        :type type_: TradingPartnerComponentBulkRequestType, optional
        """
        if request is not SENTINEL:
            self.request = self._define_list(request, BulkId)
        if type_ is not SENTINEL:
            self.type_ = self._enum_matching(
                type_, TradingPartnerComponentBulkRequestType.list(), "type_"
            )
        self._kwargs = kwargs
