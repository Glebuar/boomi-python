
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class DeployedPackageListenerStatus(Enum):
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
            map(lambda x: x.value, DeployedPackageListenerStatus._member_map_.values())
        )


@JsonMap(
    {
        "branch_name": "branchName",
        "component_id": "componentId",
        "component_type": "componentType",
        "component_version": "componentVersion",
        "deployed_by": "deployedBy",
        "deployed_date": "deployedDate",
        "deployment_id": "deploymentId",
        "environment_id": "environmentId",
        "listener_status": "listenerStatus",
        "package_id": "packageId",
        "package_version": "packageVersion",
    }
)
class DeployedPackage(BaseModel):
    """DeployedPackage

    :param active: Identifies if the packaged component is actively deployed., defaults to None
    :type active: bool, optional
    :param branch_name: branch_name, defaults to None
    :type branch_name: str, optional
    :param component_id: The ID of the component. You can use the `componentId` to create and deploy a new packaged component. The **component ID** is available in the **Revision History** dialog, which you can access from the **Build** page in the user interface., defaults to None
    :type component_id: str, optional
    :param component_type: The type of component: \<br /\>-   certificate\<br /\>-   customlibrary\<br /\>-   flowservice\<br /\>-   process\<br /\>-   processroute\<br /\>-   tpgroup\<br /\>-   webservice, defaults to None
    :type component_type: str, optional
    :param component_version: The Revision History number assigned to each saved configuration change made to a component on the **Build** tab. The component version is available in the **Revision History** dialog, which you can access from the **Build** page in the service., defaults to None
    :type component_version: int, optional
    :param deployed_by: The user ID of the user who deployed the packaged component., defaults to None
    :type deployed_by: str, optional
    :param deployed_date: The date and time you deployed the packaged component., defaults to None
    :type deployed_date: str, optional
    :param deployment_id: The ID of the deployment., defaults to None
    :type deployment_id: str, optional
    :param environment_id: The ID of the environment., defaults to None
    :type environment_id: str, optional
    :param listener_status: \(Optional, for packaged listener processes only\) The status of a listener process as RUNNING or PAUSED. If you do not specify `listenerStatus` \(or you specify an invalid value\), the current status remains unchanged. By default, the deployment of listener processes are in a running state.\<br /\>**Important:** This field is only available for the CREATE operation. To retrieve the status of deployed listeners, use the [Listener Status object](/api/platformapi#tag/ListenerStatus)., defaults to None
    :type listener_status: DeployedPackageListenerStatus, optional
    :param message: This tag is returned with the following message only when a successful additional deployment is performed after utilizing all the available connections in the account for CREATE operation:   ``` \<bns:message\>Your packaged components were successfully deployed. You have exceeded the usage count in your current connection licenses by 15. Contact a Boomi representative to purchase a higher connection licenses count.\</bns:message\> ```, defaults to None
    :type message: str, optional
    :param notes: Notes that describe the deployment., defaults to None
    :type notes: str, optional
    :param package_id: The ID of the packaged component. You can use `packageId` to deploy an existing packaged component. The packaged component ID is available from the:\<br /\>-   Packaged Component object\<br /\>-   The **Packaged Component Details** page on the **Deploy** \\> **Packaged Components** page in the user interface., defaults to None
    :type package_id: str, optional
    :param package_version: The user-defined version of the packaged component., defaults to None
    :type package_version: str, optional
    :param version: The version number generated automatically for a deployment., defaults to None
    :type version: int, optional
    """

    def __init__(
        self,
        active: bool = SENTINEL,
        branch_name: str = SENTINEL,
        component_id: str = SENTINEL,
        component_type: str = SENTINEL,
        component_version: int = SENTINEL,
        deployed_by: str = SENTINEL,
        deployed_date: str = SENTINEL,
        deployment_id: str = SENTINEL,
        environment_id: str = SENTINEL,
        listener_status: DeployedPackageListenerStatus = SENTINEL,
        message: str = SENTINEL,
        notes: str = SENTINEL,
        package_id: str = SENTINEL,
        package_version: str = SENTINEL,
        version: int = SENTINEL,
        **kwargs
    ):
        """DeployedPackage

        :param active: Identifies if the packaged component is actively deployed., defaults to None
        :type active: bool, optional
        :param branch_name: branch_name, defaults to None
        :type branch_name: str, optional
        :param component_id: The ID of the component. You can use the `componentId` to create and deploy a new packaged component. The **component ID** is available in the **Revision History** dialog, which you can access from the **Build** page in the user interface., defaults to None
        :type component_id: str, optional
        :param component_type: The type of component: \<br /\>-   certificate\<br /\>-   customlibrary\<br /\>-   flowservice\<br /\>-   process\<br /\>-   processroute\<br /\>-   tpgroup\<br /\>-   webservice, defaults to None
        :type component_type: str, optional
        :param component_version: The Revision History number assigned to each saved configuration change made to a component on the **Build** tab. The component version is available in the **Revision History** dialog, which you can access from the **Build** page in the service., defaults to None
        :type component_version: int, optional
        :param deployed_by: The user ID of the user who deployed the packaged component., defaults to None
        :type deployed_by: str, optional
        :param deployed_date: The date and time you deployed the packaged component., defaults to None
        :type deployed_date: str, optional
        :param deployment_id: The ID of the deployment., defaults to None
        :type deployment_id: str, optional
        :param environment_id: The ID of the environment., defaults to None
        :type environment_id: str, optional
        :param listener_status: \(Optional, for packaged listener processes only\) The status of a listener process as RUNNING or PAUSED. If you do not specify `listenerStatus` \(or you specify an invalid value\), the current status remains unchanged. By default, the deployment of listener processes are in a running state.\<br /\>**Important:** This field is only available for the CREATE operation. To retrieve the status of deployed listeners, use the [Listener Status object](/api/platformapi#tag/ListenerStatus)., defaults to None
        :type listener_status: DeployedPackageListenerStatus, optional
        :param message: This tag is returned with the following message only when a successful additional deployment is performed after utilizing all the available connections in the account for CREATE operation:   ``` \<bns:message\>Your packaged components were successfully deployed. You have exceeded the usage count in your current connection licenses by 15. Contact a Boomi representative to purchase a higher connection licenses count.\</bns:message\> ```, defaults to None
        :type message: str, optional
        :param notes: Notes that describe the deployment., defaults to None
        :type notes: str, optional
        :param package_id: The ID of the packaged component. You can use `packageId` to deploy an existing packaged component. The packaged component ID is available from the:\<br /\>-   Packaged Component object\<br /\>-   The **Packaged Component Details** page on the **Deploy** \\> **Packaged Components** page in the user interface., defaults to None
        :type package_id: str, optional
        :param package_version: The user-defined version of the packaged component., defaults to None
        :type package_version: str, optional
        :param version: The version number generated automatically for a deployment., defaults to None
        :type version: int, optional
        """
        if active is not SENTINEL:
            self.active = active
        if branch_name is not SENTINEL:
            self.branch_name = branch_name
        if component_id is not SENTINEL:
            self.component_id = component_id
        if component_type is not SENTINEL:
            self.component_type = component_type
        if component_version is not SENTINEL:
            self.component_version = component_version
        if deployed_by is not SENTINEL:
            self.deployed_by = deployed_by
        if deployed_date is not SENTINEL:
            self.deployed_date = deployed_date
        if deployment_id is not SENTINEL:
            self.deployment_id = deployment_id
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if listener_status is not SENTINEL:
            self.listener_status = self._enum_matching(
                listener_status, DeployedPackageListenerStatus.list(), "listener_status"
            )
        if message is not SENTINEL:
            self.message = message
        if notes is not SENTINEL:
            self.notes = notes
        if package_id is not SENTINEL:
            self.package_id = package_id
        if package_version is not SENTINEL:
            self.package_version = package_version
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
