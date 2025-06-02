
from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .listener_status import ListenerStatus


class ResponseStatusCode(Enum):
    """An enumeration representing different categories.

    :cvar _200: 200
    :vartype _200: int
    :cvar _202: 202
    :vartype _202: int
    """

    _200 = 200
    _202 = 202

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ResponseStatusCode._member_map_.values()))


@JsonMap(
    {
        "number_of_results": "numberOfResults",
        "response_status_code": "responseStatusCode",
    }
)
class ListenerStatusAsyncResponse(BaseModel):
    """ListenerStatusAsyncResponse

    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param response_status_code: The status code returned from a request, as follows:   - 202 — Initialized the Listener status request and is in progress (QUERY response).  - 200 — Listener status request is complete (GET response).
    :type response_status_code: ResponseStatusCode
    :param result: result, defaults to None
    :type result: List[ListenerStatus], optional
    """

    def __init__(
        self,
        response_status_code: ResponseStatusCode,
        number_of_results: int = SENTINEL,
        result: List[ListenerStatus] = SENTINEL,
        **kwargs,
    ):
        """ListenerStatusAsyncResponse

        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param response_status_code: The status code returned from a request, as follows:   - 202 — Initialized the Listener status request and is in progress (QUERY response).  - 200 — Listener status request is complete (GET response).
        :type response_status_code: ResponseStatusCode
        :param result: result, defaults to None
        :type result: List[ListenerStatus], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        self.response_status_code = self._enum_matching(
            response_status_code, ResponseStatusCode.list(), "response_status_code"
        )
        if result is not SENTINEL:
            self.result = self._define_list(result, ListenerStatus)
        self._kwargs = kwargs
