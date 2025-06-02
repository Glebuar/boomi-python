
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .execution_count_account import ExecutionCountAccount


@JsonMap({"number_of_results": "numberOfResults", "query_token": "queryToken"})
class ExecutionCountAccountQueryResponse(BaseModel):
    """ExecutionCountAccountQueryResponse

    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param query_token: query_token, defaults to None
    :type query_token: str, optional
    :param result: result, defaults to None
    :type result: List[ExecutionCountAccount], optional
    """

    def __init__(
        self,
        number_of_results: int = SENTINEL,
        query_token: str = SENTINEL,
        result: List[ExecutionCountAccount] = SENTINEL,
        **kwargs,
    ):
        """ExecutionCountAccountQueryResponse

        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param query_token: query_token, defaults to None
        :type query_token: str, optional
        :param result: result, defaults to None
        :type result: List[ExecutionCountAccount], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        if query_token is not SENTINEL:
            self.query_token = query_token
        if result is not SENTINEL:
            self.result = self._define_list(result, ExecutionCountAccount)
        self._kwargs = kwargs
