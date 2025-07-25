
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "branch_name": "branchName",
        "component_id": "componentId",
        "component_type": "componentType",
        "component_version": "componentVersion",
        "created_by": "createdBy",
        "created_date": "createdDate",
        "fully_publicly_consumable": "fullyPubliclyConsumable",
        "package_id": "packageId",
        "package_version": "packageVersion",
    }
)
class PackagedComponent(BaseModel):
    """PackagedComponent

    :param branch_name: The name of the branch on which you want to create a packaged component.
    :type branch_name: str
    :param component_id: The ID of the component.The **component ID** is available on the **Revision History** dialog, which you can access from the **Build** page in the user interface.
    :type component_id: str
    :param component_type: The type of component: \<br /\>-   certificate\<br /\>-   customlibrary\<br /\>-   flowservice\<br /\>-   process\<br /\>-   processroute\<br /\>-   tpgroup\<br /\>-   webservice
    :type component_type: str
    :param component_version: When you save the component configuration change on the **Build** tab, this is the assigned Revision History number. You can find the component version in the **Revision History** dialog, which you can access from the **Build** page in the service., defaults to None
    :type component_version: int, optional
    :param created_by: The user ID of the person who created the packaged component.
    :type created_by: str
    :param created_date: The creation date and time of the packaged component.
    :type created_date: str
    :param deleted: deleted, defaults to None
    :type deleted: bool, optional
    :param fully_publicly_consumable: fully_publicly_consumable, defaults to None
    :type fully_publicly_consumable: bool, optional
    :param notes: Notes that describe the packaged component.
    :type notes: str
    :param package_id: The ID of the packaged component.
    :type package_id: str
    :param package_version: The user-defined version of the packaged component. Generates a value automatically based on the component's revision number if you do not specify a packaged component version.
    :type package_version: str
    :param shareable: \(For processes and API Service components only\) Identifies whether you can share the packaged component in the **Process Library** or as part of an integration pack.   \>**Note:** You cannot share processes that contain **Process Route** components in the **Process Library** or as part of an integration pack., defaults to None
    :type shareable: bool, optional
    """

    def __init__(
        self,
        branch_name: str,
        component_id: str,
        component_type: str,
        created_by: str,
        created_date: str,
        notes: str,
        package_id: str,
        package_version: str,
        component_version: int = SENTINEL,
        deleted: bool = SENTINEL,
        fully_publicly_consumable: bool = SENTINEL,
        shareable: bool = SENTINEL,
        **kwargs
    ):
        """PackagedComponent

        :param branch_name: The name of the branch on which you want to create a packaged component.
        :type branch_name: str
        :param component_id: The ID of the component.The **component ID** is available on the **Revision History** dialog, which you can access from the **Build** page in the user interface.
        :type component_id: str
        :param component_type: The type of component: \<br /\>-   certificate\<br /\>-   customlibrary\<br /\>-   flowservice\<br /\>-   process\<br /\>-   processroute\<br /\>-   tpgroup\<br /\>-   webservice
        :type component_type: str
        :param component_version: When you save the component configuration change on the **Build** tab, this is the assigned Revision History number. You can find the component version in the **Revision History** dialog, which you can access from the **Build** page in the service., defaults to None
        :type component_version: int, optional
        :param created_by: The user ID of the person who created the packaged component.
        :type created_by: str
        :param created_date: The creation date and time of the packaged component.
        :type created_date: str
        :param deleted: deleted, defaults to None
        :type deleted: bool, optional
        :param fully_publicly_consumable: fully_publicly_consumable, defaults to None
        :type fully_publicly_consumable: bool, optional
        :param notes: Notes that describe the packaged component.
        :type notes: str
        :param package_id: The ID of the packaged component.
        :type package_id: str
        :param package_version: The user-defined version of the packaged component. Generates a value automatically based on the component's revision number if you do not specify a packaged component version.
        :type package_version: str
        :param shareable: \(For processes and API Service components only\) Identifies whether you can share the packaged component in the **Process Library** or as part of an integration pack.   \>**Note:** You cannot share processes that contain **Process Route** components in the **Process Library** or as part of an integration pack., defaults to None
        :type shareable: bool, optional
        """
        self.branch_name = branch_name
        self.component_id = component_id
        self.component_type = component_type
        if component_version is not SENTINEL:
            self.component_version = component_version
        self.created_by = created_by
        self.created_date = created_date
        if deleted is not SENTINEL:
            self.deleted = deleted
        if fully_publicly_consumable is not SENTINEL:
            self.fully_publicly_consumable = fully_publicly_consumable
        self.notes = notes
        self.package_id = package_id
        self.package_version = package_version
        if shareable is not SENTINEL:
            self.shareable = shareable
        self._kwargs = kwargs
