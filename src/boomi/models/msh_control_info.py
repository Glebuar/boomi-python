
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .hd_type import HdType
from .processing_type import ProcessingType


@JsonMap(
    {
        "application": "Application",
        "facility": "Facility",
        "network_address": "NetworkAddress",
        "processing_id": "ProcessingId",
    }
)
class MshControlInfo(BaseModel):
    """MshControlInfo

    :param application: application
    :type application: HdType
    :param facility: facility
    :type facility: HdType
    :param network_address: network_address
    :type network_address: HdType
    :param processing_id: processing_id
    :type processing_id: ProcessingType
    """

    def __init__(
        self,
        application: HdType,
        facility: HdType,
        network_address: HdType,
        processing_id: ProcessingType,
        **kwargs,
    ):
        """MshControlInfo

        :param application: application
        :type application: HdType
        :param facility: facility
        :type facility: HdType
        :param network_address: network_address
        :type network_address: HdType
        :param processing_id: processing_id
        :type processing_id: ProcessingType
        """
        self.application = self._define_object(application, HdType)
        self.facility = self._define_object(facility, HdType)
        self.network_address = self._define_object(network_address, HdType)
        self.processing_id = self._define_object(processing_id, ProcessingType)
        self._kwargs = kwargs
