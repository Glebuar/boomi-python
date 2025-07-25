
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"atom_id": "atomId"})
class JavaRollback(BaseModel):
    """JavaRollback

    :param atom_id: The unique ID assigned by the system to the container. 1. Use the Runtime ID for Runtimes, Runtime clusters, and Runtime clouds found in the user interface by navigating to **Manage** \> **Runtime Management** and viewing the Runtime Information panel for a selected container. 2. Use the Gateway ID found in the user interface by navigating to **Configure Server** \> **Gateways** \> `\<gatewayName\>` \> Gateway Information panel. 3. Use the Broker ID found in the user interface by navigating to **Configure Server** \> **Authentication** \> `\<brokerName\>` \> Broker Information panel., defaults to None
    :type atom_id: str, optional
    """

    def __init__(self, atom_id: str = SENTINEL, **kwargs):
        """JavaRollback

        :param atom_id: The unique ID assigned by the system to the container. 1. Use the Runtime ID for Runtimes, Runtime clusters, and Runtime clouds found in the user interface by navigating to **Manage** \> **Runtime Management** and viewing the Runtime Information panel for a selected container. 2. Use the Gateway ID found in the user interface by navigating to **Configure Server** \> **Gateways** \> `\<gatewayName\>` \> Gateway Information panel. 3. Use the Broker ID found in the user interface by navigating to **Configure Server** \> **Authentication** \> `\<brokerName\>` \> Broker Information panel., defaults to None
        :type atom_id: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        self._kwargs = kwargs
