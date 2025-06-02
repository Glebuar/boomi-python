
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .hl7_connector_record import Hl7ConnectorRecord


@JsonMap({"number_of_results": "numberOfResults", "query_token": "queryToken"})
class Hl7ConnectorRecordQueryResponse(BaseModel):
    """Hl7ConnectorRecordQueryResponse

    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param query_token: query_token, defaults to None
    :type query_token: str, optional
    :param result: result, defaults to None
    :type result: List[Hl7ConnectorRecord], optional
    """

    def __init__(
        self,
        number_of_results: int = SENTINEL,
        query_token: str = SENTINEL,
        result: List[Hl7ConnectorRecord] = SENTINEL,
        **kwargs,
    ):
        """Hl7ConnectorRecordQueryResponse

        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param query_token: query_token, defaults to None
        :type query_token: str, optional
        :param result: result, defaults to None
        :type result: List[Hl7ConnectorRecord], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        if query_token is not SENTINEL:
            self.query_token = query_token
        if result is not SENTINEL:
            self.result = self._define_list(result, Hl7ConnectorRecord)
        self._kwargs = kwargs
