
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..trading_partner_processing_group import TradingPartnerProcessingGroupService
from ...models import (
    TradingPartnerProcessingGroup,
    TradingPartnerProcessingGroupBulkResponse,
    TradingPartnerProcessingGroupBulkRequest,
    TradingPartnerProcessingGroupQueryResponse,
    TradingPartnerProcessingGroupQueryConfig,
)


class TradingPartnerProcessingGroupServiceAsync(TradingPartnerProcessingGroupService):
    """
    Async Wrapper for TradingPartnerProcessingGroupServiceAsync
    """

    def create_trading_partner_processing_group(
        self, request_body: TradingPartnerProcessingGroup = None
    ) -> Awaitable[Union[TradingPartnerProcessingGroup, str]]:
        return to_async(super().create_trading_partner_processing_group)(request_body)

    def get_trading_partner_processing_group(
        self, id_: str
    ) -> Awaitable[Union[TradingPartnerProcessingGroup, str]]:
        return to_async(super().get_trading_partner_processing_group)(id_)

    def update_trading_partner_processing_group(
        self, id_: str, request_body: TradingPartnerProcessingGroup = None
    ) -> Awaitable[Union[TradingPartnerProcessingGroup, str]]:
        return to_async(super().update_trading_partner_processing_group)(
            id_, request_body
        )

    def delete_trading_partner_processing_group(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_trading_partner_processing_group)(id_)

    def bulk_trading_partner_processing_group(
        self, request_body: TradingPartnerProcessingGroupBulkRequest = None
    ) -> Awaitable[Union[TradingPartnerProcessingGroupBulkResponse, str]]:
        return to_async(super().bulk_trading_partner_processing_group)(request_body)

    def query_trading_partner_processing_group(
        self, request_body: TradingPartnerProcessingGroupQueryConfig = None
    ) -> Awaitable[Union[TradingPartnerProcessingGroupQueryResponse, str]]:
        return to_async(super().query_trading_partner_processing_group)(request_body)

    def query_more_trading_partner_processing_group(
        self, request_body: str
    ) -> Awaitable[Union[TradingPartnerProcessingGroupQueryResponse, str]]:
        return to_async(super().query_more_trading_partner_processing_group)(
            request_body
        )
