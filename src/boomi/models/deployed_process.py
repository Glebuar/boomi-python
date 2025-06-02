
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .process_properties import ProcessProperties


@JsonMap({"process_properties": "ProcessProperties", "process_id": "processId"})
class DeployedProcess(BaseModel):
    """DeployedProcess

    :param process_properties: The complete list of Persisted Process properties within the specified Runtime, Runtime cluster, or cloud, where the definition of each property is by its name and value.
    :type process_properties: ProcessProperties
    :param process_id: A unique ID assigned by the system to the process.
    :type process_id: str
    """

    def __init__(
        self, process_properties: ProcessProperties, process_id: str, **kwargs
    ):
        """DeployedProcess

        :param process_properties: The complete list of Persisted Process properties within the specified Runtime, Runtime cluster, or cloud, where the definition of each property is by its name and value.
        :type process_properties: ProcessProperties
        :param process_id: A unique ID assigned by the system to the process.
        :type process_id: str
        """
        self.process_properties = self._define_object(
            process_properties, ProcessProperties
        )
        self.process_id = process_id
        self._kwargs = kwargs
