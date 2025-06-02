
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "component_id": "componentId",
        "created_by": "createdBy",
        "created_date": "createdDate",
        "environment_map_extension_id": "environmentMapExtensionId",
        "modified_by": "modifiedBy",
        "modified_date": "modifiedDate",
    }
)
class EnvironmentMapExtensionUserDefinedFunctionSummary(BaseModel):
    """EnvironmentMapExtensionUserDefinedFunctionSummary

    :param component_id: The ID of the component., defaults to None
    :type component_id: str, optional
    :param created_by: The email address of the user who created the component., defaults to None
    :type created_by: str, optional
    :param created_date: The creation date of the component., defaults to None
    :type created_date: str, optional
    :param deleted: Indicates the deletion of a component. A true value indicates a deleted status, whereas a false value indicates an active status., defaults to None
    :type deleted: bool, optional
    :param environment_map_extension_id: The system-generated ID of a environment map extension within a specific environment., defaults to None
    :type environment_map_extension_id: str, optional
    :param modified_by: The email address of the user who modified the component., defaults to None
    :type modified_by: str, optional
    :param modified_date: The modification date of the component., defaults to None
    :type modified_date: str, optional
    :param name: The user-defined name given to the component., defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        component_id: str = SENTINEL,
        created_by: str = SENTINEL,
        created_date: str = SENTINEL,
        deleted: bool = SENTINEL,
        environment_map_extension_id: str = SENTINEL,
        modified_by: str = SENTINEL,
        modified_date: str = SENTINEL,
        name: str = SENTINEL,
        **kwargs
    ):
        """EnvironmentMapExtensionUserDefinedFunctionSummary

        :param component_id: The ID of the component., defaults to None
        :type component_id: str, optional
        :param created_by: The email address of the user who created the component., defaults to None
        :type created_by: str, optional
        :param created_date: The creation date of the component., defaults to None
        :type created_date: str, optional
        :param deleted: Indicates the deletion of a component. A true value indicates a deleted status, whereas a false value indicates an active status., defaults to None
        :type deleted: bool, optional
        :param environment_map_extension_id: The system-generated ID of a environment map extension within a specific environment., defaults to None
        :type environment_map_extension_id: str, optional
        :param modified_by: The email address of the user who modified the component., defaults to None
        :type modified_by: str, optional
        :param modified_date: The modification date of the component., defaults to None
        :type modified_date: str, optional
        :param name: The user-defined name given to the component., defaults to None
        :type name: str, optional
        """
        if component_id is not SENTINEL:
            self.component_id = component_id
        if created_by is not SENTINEL:
            self.created_by = created_by
        if created_date is not SENTINEL:
            self.created_date = created_date
        if deleted is not SENTINEL:
            self.deleted = deleted
        if environment_map_extension_id is not SENTINEL:
            self.environment_map_extension_id = environment_map_extension_id
        if modified_by is not SENTINEL:
            self.modified_by = modified_by
        if modified_date is not SENTINEL:
            self.modified_date = modified_date
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
