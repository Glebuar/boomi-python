
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .execution_request_dynamic_process_properties import (
    ExecutionRequestDynamicProcessProperties,
)
from .execution_request_process_properties import ExecutionRequestProcessProperties


@JsonMap(
    {
        "dynamic_process_properties": "DynamicProcessProperties",
        "process_properties": "ProcessProperties",
        "atom_id": "atomId",
        "process_id": "processId",
        "process_name": "processName",
        "record_url": "recordUrl",
        "request_id": "requestId",
    }
)
class ExecutionRequest(BaseModel):
    """ExecutionRequest

    :param dynamic_process_properties: The full list of Dynamic Process properties within the specified Runtime, Runtime cluster, or cloud, where each property is defined by their name and value.
    :type dynamic_process_properties: ExecutionRequestDynamicProcessProperties
    :param process_properties: The full list of Process properties within the specified Runtime, Runtime cluster, or cloud, where each property is defined by their name and value.
    :type process_properties: ExecutionRequestProcessProperties
    :param atom_id: The ID of the Runtime on which to run the process. Locate the Runtime ID by navigating to **Manage** \\> **Runtime Management** on the user interface, and viewing the Runtime Information panel for a selected Runtime.
    :type atom_id: str
    :param process_id: The ID of the process to run. You can find ID of a process by locating the process' **Component ID** in the **Revision History** dialog on the user interface., defaults to None
    :type process_id: str, optional
    :param process_name: process_name, defaults to None
    :type process_name: str, optional
    :param record_url: \(Response-only field\) The ID of the process run. This field is returned in the initial POST response and is used in the subsequent call to find the corresponding run record., defaults to None
    :type record_url: str, optional
    :param request_id: request_id, defaults to None
    :type request_id: str, optional
    """

    def __init__(
        self,
        dynamic_process_properties: ExecutionRequestDynamicProcessProperties,
        process_properties: ExecutionRequestProcessProperties,
        atom_id: str,
        process_id: str = SENTINEL,
        process_name: str = SENTINEL,
        record_url: str = SENTINEL,
        request_id: str = SENTINEL,
        **kwargs,
    ):
        """ExecutionRequest

        :param dynamic_process_properties: The full list of Dynamic Process properties within the specified Runtime, Runtime cluster, or cloud, where each property is defined by their name and value.
        :type dynamic_process_properties: ExecutionRequestDynamicProcessProperties
        :param process_properties: The full list of Process properties within the specified Runtime, Runtime cluster, or cloud, where each property is defined by their name and value.
        :type process_properties: ExecutionRequestProcessProperties
        :param atom_id: The ID of the Runtime on which to run the process. Locate the Runtime ID by navigating to **Manage** \\> **Runtime Management** on the user interface, and viewing the Runtime Information panel for a selected Runtime.
        :type atom_id: str
        :param process_id: The ID of the process to run. You can find ID of a process by locating the process' **Component ID** in the **Revision History** dialog on the user interface., defaults to None
        :type process_id: str, optional
        :param process_name: process_name, defaults to None
        :type process_name: str, optional
        :param record_url: \(Response-only field\) The ID of the process run. This field is returned in the initial POST response and is used in the subsequent call to find the corresponding run record., defaults to None
        :type record_url: str, optional
        :param request_id: request_id, defaults to None
        :type request_id: str, optional
        """
        self.dynamic_process_properties = self._define_object(
            dynamic_process_properties, ExecutionRequestDynamicProcessProperties
        )
        self.process_properties = self._define_object(
            process_properties, ExecutionRequestProcessProperties
        )
        self.atom_id = atom_id
        if process_id is not SENTINEL:
            self.process_id = process_id
        if process_name is not SENTINEL:
            self.process_name = process_name
        if record_url is not SENTINEL:
            self.record_url = record_url
        if request_id is not SENTINEL:
            self.request_id = request_id
        self._kwargs = kwargs
