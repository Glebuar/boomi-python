
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .document_count_account import DocumentCountAccount


@JsonMap({"number_of_results": "numberOfResults", "query_token": "queryToken"})
class DocumentCountAccountGroupQueryResponse(BaseModel):
    """DocumentCountAccountGroupQueryResponse

    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param query_token: query_token, defaults to None
    :type query_token: str, optional
    :param result: result, defaults to None
    :type result: List[DocumentCountAccount], optional
    """

    def __init__(
        self,
        number_of_results: int = SENTINEL,
        query_token: str = SENTINEL,
        result: List[DocumentCountAccount] = SENTINEL,
        **kwargs,
    ):
        """DocumentCountAccountGroupQueryResponse

        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param query_token: query_token, defaults to None
        :type query_token: str, optional
        :param result: result, defaults to None
        :type result: List[DocumentCountAccount], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        if query_token is not SENTINEL:
            self.query_token = query_token
        if result is not SENTINEL:
            self.result = self._define_list(result, DocumentCountAccount)
        self._kwargs = kwargs
