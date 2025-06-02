
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .processing_group_document_standard_route import (
    ProcessingGroupDocumentStandardRoute,
)


@JsonMap({"standard_route": "StandardRoute", "process_id": "processId"})
class ProcessingGroupDocumentBasedRouting(BaseModel):
    """ProcessingGroupDocumentBasedRouting

    :param standard_route: standard_route, defaults to None
    :type standard_route: List[ProcessingGroupDocumentStandardRoute], optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        standard_route: List[ProcessingGroupDocumentStandardRoute] = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs,
    ):
        """ProcessingGroupDocumentBasedRouting

        :param standard_route: standard_route, defaults to None
        :type standard_route: List[ProcessingGroupDocumentStandardRoute], optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        """
        if standard_route is not SENTINEL:
            self.standard_route = self._define_list(
                standard_route, ProcessingGroupDocumentStandardRoute
            )
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
