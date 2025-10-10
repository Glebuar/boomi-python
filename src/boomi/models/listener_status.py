
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"connector_type": "connectorType", "listener_id": "listenerId"})
class ListenerStatus(BaseModel):
    """ListenerStatus

    :param connector_type: The internal and unique identifier for connector type, which resembles the connector type names presented on the **Build** tab of the user interface., defaults to None
    :type connector_type: str, optional
    :param listener_id: The Component ID for the listener process.
    :type listener_id: str
    :param status: The status of the listener as `listening`, `paused`, or `errored`.
    :type status: str
    """

    def __init__(
        self, listener_id: str, status: str, connector_type: str = SENTINEL, **kwargs
    ):
        """ListenerStatus

        :param connector_type: The internal and unique identifier for connector type, which resembles the connector type names presented on the **Build** tab of the user interface., defaults to None
        :type connector_type: str, optional
        :param listener_id: The Component ID for the listener process.
        :type listener_id: str
        :param status: The status of the listener as `listening`, `paused`, or `errored`.
        :type status: str
        """
        if connector_type is not SENTINEL:
            self.connector_type = connector_type
        self.listener_id = listener_id
        self.status = status
        self._kwargs = kwargs
