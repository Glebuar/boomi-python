
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .atom_security_policies import AtomSecurityPolicies


@JsonMap(
    {
        "number_of_results": "numberOfResults",
        "response_status_code": "responseStatusCode",
    }
)
class AtomSecurityPoliciesAsyncResponse(BaseModel):
    """AtomSecurityPoliciesAsyncResponse

    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param response_status_code: response_status_code
    :type response_status_code: int
    :param result: result, defaults to None
    :type result: List[AtomSecurityPolicies], optional
    """

    def __init__(
        self,
        response_status_code: int,
        number_of_results: int = SENTINEL,
        result: List[AtomSecurityPolicies] = SENTINEL,
        **kwargs,
    ):
        """AtomSecurityPoliciesAsyncResponse

        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param response_status_code: response_status_code
        :type response_status_code: int
        :param result: result, defaults to None
        :type result: List[AtomSecurityPolicies], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        self.response_status_code = response_status_code
        if result is not SENTINEL:
            self.result = self._define_list(result, AtomSecurityPolicies)
        self._kwargs = kwargs
