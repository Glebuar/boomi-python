
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .process import Process


@JsonMap(
    {
        "result": "Result",
        "id_": "id",
        "status_code": "statusCode",
        "error_message": "errorMessage",
    }
)
class ProcessBulkResponseResponse(BaseModel):
    """ProcessBulkResponseResponse

    :param result: result
    :type result: Process
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
        result: Process,
        index: int = SENTINEL,
        id_: str = SENTINEL,
        status_code: int = SENTINEL,
        error_message: str = SENTINEL,
        **kwargs,
    ):
        """ProcessBulkResponseResponse

        :param result: result
        :type result: Process
        :param index: index, defaults to None
        :type index: int, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param status_code: status_code, defaults to None
        :type status_code: int, optional
        :param error_message: error_message, defaults to None
        :type error_message: str, optional
        """
        self.result = self._define_object(result, Process)
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
class ProcessBulkResponse(BaseModel):
    """ProcessBulkResponse

    :param response: response, defaults to None
    :type response: List[ProcessBulkResponseResponse], optional
    """

    def __init__(
        self, response: List[ProcessBulkResponseResponse] = SENTINEL, **kwargs
    ):
        """ProcessBulkResponse

        :param response: response, defaults to None
        :type response: List[ProcessBulkResponseResponse], optional
        """
        if response is not SENTINEL:
            self.response = self._define_list(response, ProcessBulkResponseResponse)
        self._kwargs = kwargs
