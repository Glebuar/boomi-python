
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class Action(Enum):
    """An enumeration representing different categories.

    :cvar RESTART: "restart"
    :vartype RESTART: str
    :cvar RESTARTALL: "restart_all"
    :vartype RESTARTALL: str
    :cvar PAUSE: "pause"
    :vartype PAUSE: str
    :cvar PAUSEALL: "pause_all"
    :vartype PAUSEALL: str
    :cvar RESUME: "resume"
    :vartype RESUME: str
    :cvar RESUMEALL: "resume_all"
    :vartype RESUMEALL: str
    """

    RESTART = "restart"
    RESTARTALL = "restart_all"
    PAUSE = "pause"
    PAUSEALL = "pause_all"
    RESUME = "resume"
    RESUMEALL = "resume_all"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Action._member_map_.values()))


@JsonMap({"container_id": "containerId", "listener_id": "listenerId"})
class ChangeListenerStatusRequest(BaseModel):
    """ChangeListenerStatusRequest

    :param action: The action to be performed., defaults to None
    :type action: Action, optional
    :param container_id: The ID of the Runtime, Runtime cluster, or Runtime cloud to which you deploy the listener or listeners., defaults to None
    :type container_id: str, optional
    :param listener_id: The ID of a single listener process whose status you want to change. To change the status of all listeners, omit this parameter.   \>**Note:** You can obtain the ID for a listener process by using a QUERY operation on the Process object., defaults to None
    :type listener_id: str, optional
    """

    def __init__(
        self,
        action: Action = SENTINEL,
        container_id: str = SENTINEL,
        listener_id: str = SENTINEL,
        **kwargs
    ):
        """ChangeListenerStatusRequest

        :param action: The action to be performed., defaults to None
        :type action: Action, optional
        :param container_id: The ID of the Runtime, Runtime cluster, or Runtime cloud to which you deploy the listener or listeners., defaults to None
        :type container_id: str, optional
        :param listener_id: The ID of a single listener process whose status you want to change. To change the status of all listeners, omit this parameter.   \>**Note:** You can obtain the ID for a listener process by using a QUERY operation on the Process object., defaults to None
        :type listener_id: str, optional
        """
        if action is not SENTINEL:
            self.action = self._enum_matching(action, Action.list(), "action")
        if container_id is not SENTINEL:
            self.container_id = container_id
        if listener_id is not SENTINEL:
            self.listener_id = listener_id
        self._kwargs = kwargs
