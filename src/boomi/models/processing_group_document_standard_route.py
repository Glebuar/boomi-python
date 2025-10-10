
from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .processing_group_document_type_route import ProcessingGroupDocumentTypeRoute


class ProcessingGroupDocumentStandardRouteStandard(Enum):
    """An enumeration representing different categories.

    :cvar X12: "x12"
    :vartype X12: str
    :cvar EDIFACT: "edifact"
    :vartype EDIFACT: str
    :cvar HL7: "hl7"
    :vartype HL7: str
    :cvar CUSTOM: "custom"
    :vartype CUSTOM: str
    :cvar ROSETTANET: "rosettanet"
    :vartype ROSETTANET: str
    :cvar TRADACOMS: "tradacoms"
    :vartype TRADACOMS: str
    :cvar ODETTE: "odette"
    :vartype ODETTE: str
    """

    X12 = "x12"
    EDIFACT = "edifact"
    HL7 = "hl7"
    CUSTOM = "custom"
    ROSETTANET = "rosettanet"
    TRADACOMS = "tradacoms"
    ODETTE = "odette"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                ProcessingGroupDocumentStandardRouteStandard._member_map_.values(),
            )
        )


@JsonMap({"document_type_route": "DocumentTypeRoute", "process_id": "processId"})
class ProcessingGroupDocumentStandardRoute(BaseModel):
    """ProcessingGroupDocumentStandardRoute

    :param document_type_route: document_type_route, defaults to None
    :type document_type_route: List[ProcessingGroupDocumentTypeRoute], optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    :param standard: standard, defaults to None
    :type standard: ProcessingGroupDocumentStandardRouteStandard, optional
    """

    def __init__(
        self,
        document_type_route: List[ProcessingGroupDocumentTypeRoute] = SENTINEL,
        process_id: str = SENTINEL,
        standard: ProcessingGroupDocumentStandardRouteStandard = SENTINEL,
        **kwargs,
    ):
        """ProcessingGroupDocumentStandardRoute

        :param document_type_route: document_type_route, defaults to None
        :type document_type_route: List[ProcessingGroupDocumentTypeRoute], optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        :param standard: standard, defaults to None
        :type standard: ProcessingGroupDocumentStandardRouteStandard, optional
        """
        if document_type_route is not SENTINEL:
            self.document_type_route = self._define_list(
                document_type_route, ProcessingGroupDocumentTypeRoute
            )
        if process_id is not SENTINEL:
            self.process_id = process_id
        if standard is not SENTINEL:
            self.standard = self._enum_matching(
                standard,
                ProcessingGroupDocumentStandardRouteStandard.list(),
                "standard",
            )
        self._kwargs = kwargs
