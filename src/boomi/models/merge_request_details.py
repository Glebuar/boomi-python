
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .merge_request_detail import MergeRequestDetail


@JsonMap({"merge_request_detail": "MergeRequestDetail"})
class MergeRequestDetails(BaseModel):
    """MergeRequestDetails

    :param merge_request_detail: merge_request_detail, defaults to None
    :type merge_request_detail: List[MergeRequestDetail], optional
    """

    def __init__(
        self, merge_request_detail: List[MergeRequestDetail] = SENTINEL, **kwargs
    ):
        """MergeRequestDetails

        :param merge_request_detail: merge_request_detail, defaults to None
        :type merge_request_detail: List[MergeRequestDetail], optional
        """
        if merge_request_detail is not SENTINEL:
            self.merge_request_detail = self._define_list(
                merge_request_detail, MergeRequestDetail
            )
        self._kwargs = kwargs
