
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .java_upgrade_options import JavaUpgradeOptions


@JsonMap({"java_upgrade_options": "JavaUpgradeOptions", "atom_id": "atomId"})
class JavaUpgrade(BaseModel):
    """JavaUpgrade

    :param java_upgrade_options: java_upgrade_options, defaults to None
    :type java_upgrade_options: JavaUpgradeOptions, optional
    :param atom_id: The unique ID assigned by the system to the container\<br /\> 1. Use the Runtime ID for Runtimes, Runtime clusters, and Runtime clouds found in the user interface by navigating to **Manage** \> **Runtime Management** and viewing the **Runtime Information** panel for a selected container. \<br /\> 2. Use the Gateway ID found in the user interface by navigating to **Configure Server** \> **Gateways** \> **click on a Gateway's name** \> **Gateway Information panel**. \<br /\> 3. Use the Broker ID found in the user interface by navigating to **Configure Server** \> **Authentication** \> **click on a Broker's name** \> **Broker Information panel**., defaults to None
    :type atom_id: str, optional
    """

    def __init__(
        self,
        java_upgrade_options: JavaUpgradeOptions = SENTINEL,
        atom_id: str = SENTINEL,
        **kwargs,
    ):
        """JavaUpgrade

        :param java_upgrade_options: java_upgrade_options, defaults to None
        :type java_upgrade_options: JavaUpgradeOptions, optional
        :param atom_id: The unique ID assigned by the system to the container\<br /\> 1. Use the Runtime ID for Runtimes, Runtime clusters, and Runtime clouds found in the user interface by navigating to **Manage** \> **Runtime Management** and viewing the **Runtime Information** panel for a selected container. \<br /\> 2. Use the Gateway ID found in the user interface by navigating to **Configure Server** \> **Gateways** \> **click on a Gateway's name** \> **Gateway Information panel**. \<br /\> 3. Use the Broker ID found in the user interface by navigating to **Configure Server** \> **Authentication** \> **click on a Broker's name** \> **Broker Information panel**., defaults to None
        :type atom_id: str, optional
        """
        if java_upgrade_options is not SENTINEL:
            self.java_upgrade_options = self._define_object(
                java_upgrade_options, JavaUpgradeOptions
            )
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        self._kwargs = kwargs
