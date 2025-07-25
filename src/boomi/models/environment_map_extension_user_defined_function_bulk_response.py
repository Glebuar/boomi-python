
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .environment_map_extension_user_defined_function import (
    EnvironmentMapExtensionUserDefinedFunction,
)


@JsonMap(
    {
        "result": "Result",
        "id_": "id",
        "status_code": "statusCode",
        "error_message": "errorMessage",
    }
)
class EnvironmentMapExtensionUserDefinedFunctionBulkResponseResponse(BaseModel):
    """EnvironmentMapExtensionUserDefinedFunctionBulkResponseResponse

    :param result: result
    :type result: EnvironmentMapExtensionUserDefinedFunction
    :param index: index, defaults to None
    :type index: int, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param status_code: status_code, defaults to None
    :type status_code: int, optional
    :param error_message: error_message, defaults to None
    :type error_message: str, optional
    """

    def __init__(
        self,
        result: EnvironmentMapExtensionUserDefinedFunction,
        index: int = SENTINEL,
        id_: str = SENTINEL,
        status_code: int = SENTINEL,
        error_message: str = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtensionUserDefinedFunctionBulkResponseResponse

        :param result: result
        :type result: EnvironmentMapExtensionUserDefinedFunction
        :param index: index, defaults to None
        :type index: int, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param status_code: status_code, defaults to None
        :type status_code: int, optional
        :param error_message: error_message, defaults to None
        :type error_message: str, optional
        """
        self.result = self._define_object(
            result, EnvironmentMapExtensionUserDefinedFunction
        )
        if index is not SENTINEL:
            self.index = index
        if id_ is not SENTINEL:
            self.id_ = id_
        if status_code is not SENTINEL:
            self.status_code = status_code
        if error_message is not SENTINEL:
            self.error_message = error_message
        self._kwargs = kwargs


@JsonMap({})
class EnvironmentMapExtensionUserDefinedFunctionBulkResponse(BaseModel):
    """EnvironmentMapExtensionUserDefinedFunctionBulkResponse

    :param response: response, defaults to None
    :type response: List[EnvironmentMapExtensionUserDefinedFunctionBulkResponseResponse], optional
    """

    def __init__(
        self,
        response: List[
            EnvironmentMapExtensionUserDefinedFunctionBulkResponseResponse
        ] = SENTINEL,
        **kwargs,
    ):
        """EnvironmentMapExtensionUserDefinedFunctionBulkResponse

        :param response: response, defaults to None
        :type response: List[EnvironmentMapExtensionUserDefinedFunctionBulkResponseResponse], optional
        """
        if response is not SENTINEL:
            self.response = self._define_list(
                response, EnvironmentMapExtensionUserDefinedFunctionBulkResponseResponse
            )
        self._kwargs = kwargs
