
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..event import EventService
from ...models import EventQueryResponse, EventQueryConfig


class EventServiceAsync(EventService):
    """
    Async Wrapper for EventServiceAsync
    """

    def query_event(
        self, request_body: EventQueryConfig = None
    ) -> Awaitable[Union[EventQueryResponse, str]]:
        return to_async(super().query_event)(request_body)

    def query_more_event(
        self, request_body: str
    ) -> Awaitable[Union[EventQueryResponse, str]]:
        return to_async(super().query_more_event)(request_body)
