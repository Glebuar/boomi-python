
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .organization_contact_info import OrganizationContactInfo


@JsonMap(
    {
        "organization_contact_info": "OrganizationContactInfo",
        "component_id": "componentId",
        "component_name": "componentName",
        "folder_id": "folderId",
        "folder_name": "folderName",
    }
)
class OrganizationComponent(BaseModel):
    """OrganizationComponent

    :param organization_contact_info: organization_contact_info
    :type organization_contact_info: OrganizationContactInfo
    :param component_id: A unique ID assigned by the system to the component., defaults to None
    :type component_id: str, optional
    :param component_name: A user-defined name for the component., defaults to None
    :type component_name: str, optional
    :param deleted: Indicates if the component is deleted. A value of `true` indicates a deleted status, whereas `false` indicates an active status., defaults to None
    :type deleted: bool, optional
    :param description: Description of the component.  \>**Note:** Although this field is in the object, operations do not support the field. For example, the system ignores the field if it is present in a QUERY, CREATE, or UPDATE request., defaults to None
    :type description: str, optional
    :param folder_id: The ID of the folder in which the component currently resides., defaults to None
    :type folder_id: int, optional
    :param folder_name: The folder location of the component within Component Explorer., defaults to None
    :type folder_name: str, optional
    """

    def __init__(
        self,
        organization_contact_info: OrganizationContactInfo,
        component_id: str = SENTINEL,
        component_name: str = SENTINEL,
        deleted: bool = SENTINEL,
        description: str = SENTINEL,
        folder_id: int = SENTINEL,
        folder_name: str = SENTINEL,
        **kwargs,
    ):
        """OrganizationComponent

        :param organization_contact_info: organization_contact_info
        :type organization_contact_info: OrganizationContactInfo
        :param component_id: A unique ID assigned by the system to the component., defaults to None
        :type component_id: str, optional
        :param component_name: A user-defined name for the component., defaults to None
        :type component_name: str, optional
        :param deleted: Indicates if the component is deleted. A value of `true` indicates a deleted status, whereas `false` indicates an active status., defaults to None
        :type deleted: bool, optional
        :param description: Description of the component.  \>**Note:** Although this field is in the object, operations do not support the field. For example, the system ignores the field if it is present in a QUERY, CREATE, or UPDATE request., defaults to None
        :type description: str, optional
        :param folder_id: The ID of the folder in which the component currently resides., defaults to None
        :type folder_id: int, optional
        :param folder_name: The folder location of the component within Component Explorer., defaults to None
        :type folder_name: str, optional
        """
        self.organization_contact_info = self._define_object(
            organization_contact_info, OrganizationContactInfo
        )
        if component_id is not SENTINEL:
            self.component_id = component_id
        if component_name is not SENTINEL:
            self.component_name = component_name
        if deleted is not SENTINEL:
            self.deleted = deleted
        if description is not SENTINEL:
            self.description = description
        if folder_id is not SENTINEL:
            self.folder_id = folder_id
        if folder_name is not SENTINEL:
            self.folder_name = folder_name
        self._kwargs = kwargs
