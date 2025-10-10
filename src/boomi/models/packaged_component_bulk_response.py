
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .packaged_component import PackagedComponent


@JsonMap(
    {
        "result": "Result",
        "id_": "id",
        "status_code": "statusCode",
        "error_message": "errorMessage",
    }
)
class PackagedComponentBulkResponseResponse(BaseModel):
    """PackagedComponentBulkResponseResponse

    :param result: result
    :type result: PackagedComponent
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
        result: PackagedComponent,
        index: int = SENTINEL,
        id_: str = SENTINEL,
        status_code: int = SENTINEL,
        error_message: str = SENTINEL,
        **kwargs,
    ):
        """PackagedComponentBulkResponseResponse

        :param result: result
        :type result: PackagedComponent
        :param index: index, defaults to None
        :type index: int, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param status_code: status_code, defaults to None
        :type status_code: int, optional
        :param error_message: error_message, defaults to None
        :type error_message: str, optional
        """
        self.result = self._define_object(result, PackagedComponent)
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
class PackagedComponentBulkResponse(BaseModel):
    """PackagedComponentBulkResponse

    :param response: response, defaults to None
    :type response: List[PackagedComponentBulkResponseResponse], optional
    """

    def __init__(
        self, response: List[PackagedComponentBulkResponseResponse] = SENTINEL, **kwargs
    ):
        """PackagedComponentBulkResponse

        :param response: response, defaults to None
        :type response: List[PackagedComponentBulkResponseResponse], optional
        """
        if response is not SENTINEL:
            self.response = self._define_list(
                response, PackagedComponentBulkResponseResponse
            )
        self._kwargs = kwargs
