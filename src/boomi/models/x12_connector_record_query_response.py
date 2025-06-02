
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .x12_connector_record import X12ConnectorRecord


@JsonMap({"number_of_results": "numberOfResults", "query_token": "queryToken"})
class X12ConnectorRecordQueryResponse(BaseModel):
    """X12ConnectorRecordQueryResponse

    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param query_token: query_token, defaults to None
    :type query_token: str, optional
    :param result: result, defaults to None
    :type result: List[X12ConnectorRecord], optional
    """

    def __init__(
        self,
        number_of_results: int = SENTINEL,
        query_token: str = SENTINEL,
        result: List[X12ConnectorRecord] = SENTINEL,
        **kwargs,
    ):
        """X12ConnectorRecordQueryResponse

        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param query_token: query_token, defaults to None
        :type query_token: str, optional
        :param result: result, defaults to None
        :type result: List[X12ConnectorRecord], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        if query_token is not SENTINEL:
            self.query_token = query_token
        if result is not SENTINEL:
            self.result = self._define_list(result, X12ConnectorRecord)
        self._kwargs = kwargs
