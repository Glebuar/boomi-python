
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..trading_partner_component import TradingPartnerComponentService
from ...models import (
    TradingPartnerComponent,
    TradingPartnerComponentBulkResponse,
    TradingPartnerComponentBulkRequest,
    TradingPartnerComponentQueryResponse,
    TradingPartnerComponentQueryConfig,
)


class TradingPartnerComponentServiceAsync(TradingPartnerComponentService):
    """
    Async Wrapper for TradingPartnerComponentServiceAsync
    """

    def create_trading_partner_component(
        self, request_body: TradingPartnerComponent = None
    ) -> Awaitable[Union[TradingPartnerComponent, str]]:
        return to_async(super().create_trading_partner_component)(request_body)

    def get_trading_partner_component(
        self, id_: str
    ) -> Awaitable[Union[TradingPartnerComponent, str]]:
        return to_async(super().get_trading_partner_component)(id_)

    def update_trading_partner_component(
        self, id_: str, request_body: TradingPartnerComponent = None
    ) -> Awaitable[Union[TradingPartnerComponent, str]]:
        return to_async(super().update_trading_partner_component)(id_, request_body)

    def delete_trading_partner_component(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_trading_partner_component)(id_)

    def bulk_trading_partner_component(
        self, request_body: TradingPartnerComponentBulkRequest = None
    ) -> Awaitable[Union[TradingPartnerComponentBulkResponse, str]]:
        return to_async(super().bulk_trading_partner_component)(request_body)

    def query_trading_partner_component(
        self, request_body: TradingPartnerComponentQueryConfig = None
    ) -> Awaitable[Union[TradingPartnerComponentQueryResponse, str]]:
        return to_async(super().query_trading_partner_component)(request_body)

    def query_more_trading_partner_component(
        self, request_body: str
    ) -> Awaitable[Union[TradingPartnerComponentQueryResponse, str]]:
        return to_async(super().query_more_trading_partner_component)(request_body)
