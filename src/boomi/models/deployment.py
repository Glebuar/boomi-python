
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class DeploymentListenerStatus(Enum):
    """An enumeration representing different categories.

    :cvar RUNNING: "RUNNING"
    :vartype RUNNING: str
    :cvar PAUSED: "PAUSED"
    :vartype PAUSED: str
    """

    RUNNING = "RUNNING"
    PAUSED = "PAUSED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, DeploymentListenerStatus._member_map_.values())
        )


@JsonMap(
    {
        "component_id": "componentId",
        "component_type": "componentType",
        "deployed_by": "deployedBy",
        "deployed_on": "deployedOn",
        "environment_id": "environmentId",
        "id_": "id",
        "listener_status": "listenerStatus",
        "process_id": "processId",
    }
)
class Deployment(BaseModel):
    """Deployment

    :param component_id: component_id
    :type component_id: str
    :param component_type: component_type
    :type component_type: str
    :param current: current, defaults to None
    :type current: bool, optional
    :param deployed_by: deployed_by
    :type deployed_by: str
    :param deployed_on: deployed_on
    :type deployed_on: str
    :param digest: digest
    :type digest: str
    :param environment_id: environment_id
    :type environment_id: str
    :param id_: id_
    :type id_: str
    :param listener_status: listener_status, defaults to None
    :type listener_status: DeploymentListenerStatus, optional
    :param message: message, defaults to None
    :type message: str, optional
    :param notes: notes
    :type notes: str
    :param process_id: process_id
    :type process_id: str
    :param version: version, defaults to None
    :type version: int, optional
    """

    def __init__(
        self,
        component_id: str,
        component_type: str,
        deployed_by: str,
        deployed_on: str,
        digest: str,
        environment_id: str,
        id_: str,
        notes: str,
        process_id: str,
        current: bool = SENTINEL,
        listener_status: DeploymentListenerStatus = SENTINEL,
        message: str = SENTINEL,
        version: int = SENTINEL,
        **kwargs
    ):
        """Deployment

        :param component_id: component_id
        :type component_id: str
        :param component_type: component_type
        :type component_type: str
        :param current: current, defaults to None
        :type current: bool, optional
        :param deployed_by: deployed_by
        :type deployed_by: str
        :param deployed_on: deployed_on
        :type deployed_on: str
        :param digest: digest
        :type digest: str
        :param environment_id: environment_id
        :type environment_id: str
        :param id_: id_
        :type id_: str
        :param listener_status: listener_status, defaults to None
        :type listener_status: DeploymentListenerStatus, optional
        :param message: message, defaults to None
        :type message: str, optional
        :param notes: notes
        :type notes: str
        :param process_id: process_id
        :type process_id: str
        :param version: version, defaults to None
        :type version: int, optional
        """
        self.component_id = component_id
        self.component_type = component_type
        if current is not SENTINEL:
            self.current = current
        self.deployed_by = deployed_by
        self.deployed_on = deployed_on
        self.digest = digest
        self.environment_id = environment_id
        self.id_ = id_
        if listener_status is not SENTINEL:
            self.listener_status = self._enum_matching(
                listener_status, DeploymentListenerStatus.list(), "listener_status"
            )
        if message is not SENTINEL:
            self.message = message
        self.notes = notes
        self.process_id = process_id
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
