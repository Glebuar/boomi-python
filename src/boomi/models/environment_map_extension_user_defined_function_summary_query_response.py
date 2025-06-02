
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .environment_map_extension_user_defined_function_summary import (
    EnvironmentMapExtensionUserDefinedFunctionSummary,
)


@JsonMap({"number_of_results": "numberOfResults", "query_token": "queryToken"})
class EnvironmentMapExtensionUserDefinedFunctionSummaryQueryResponse(BaseModel):
    """EnvironmentMapExtensionUserDefinedFunctionSummaryQueryResponse

    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param query_token: query_token, defaults to None
    :type query_token: str, optional
    :param result: result, defaults to None
    :type result: List[EnvironmentMapExtensionUserDefinedFunctionSummary], optional
    """

    def __init__(
        self,
        number_of_results: int = SENTINEL,
        query_token: str = SENTINEL,
        result: List[EnvironmentMapExtensionUserDefinedFunctionSummary] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtensionUserDefinedFunctionSummaryQueryResponse

        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param query_token: query_token, defaults to None
        :type query_token: str, optional
        :param result: result, defaults to None
        :type result: List[EnvironmentMapExtensionUserDefinedFunctionSummary], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        if query_token is not SENTINEL:
            self.query_token = query_token
        if result is not SENTINEL:
            self.result = self._define_list(
                result, EnvironmentMapExtensionUserDefinedFunctionSummary
            )
        self._kwargs = kwargs
