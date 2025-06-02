
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "component_id": "componentId",
        "component_name": "componentName",
        "component_type": "componentType",
        "component_version": "componentVersion",
        "environment_map_extension_id": "environmentMapExtensionId",
    }
)
class EnvironmentMapExtensionExternalComponent(BaseModel):
    """EnvironmentMapExtensionExternalComponent

    :param component_id: The ID of the component. The component ID is available by querying the Component Metadata object., defaults to None
    :type component_id: str, optional
    :param component_name: The user-defined name given to the component., defaults to None
    :type component_name: str, optional
    :param component_type: The type of component. \>**Note:** Currently, this object retrieves Cross Reference Table type-components ('crossref') only., defaults to None
    :type component_type: str, optional
    :param component_version: component_version, defaults to None
    :type component_version: int, optional
    :param environment_map_extension_id: The ID of the environment map extension. To find the environmentMapExtensionId, you can first query the [Environment Map Extension object](/api/platformapi#tag/EnvironmentMapExtension) to retrieve a list of all available environment extensions for an account and copy the resultant environment map extension ID., defaults to None
    :type environment_map_extension_id: str, optional
    """

    def __init__(
        self,
        component_id: str = SENTINEL,
        component_name: str = SENTINEL,
        component_type: str = SENTINEL,
        component_version: int = SENTINEL,
        environment_map_extension_id: str = SENTINEL,
        **kwargs
    ):
        """EnvironmentMapExtensionExternalComponent

        :param component_id: The ID of the component. The component ID is available by querying the Component Metadata object., defaults to None
        :type component_id: str, optional
        :param component_name: The user-defined name given to the component., defaults to None
        :type component_name: str, optional
        :param component_type: The type of component. \>**Note:** Currently, this object retrieves Cross Reference Table type-components ('crossref') only., defaults to None
        :type component_type: str, optional
        :param component_version: component_version, defaults to None
        :type component_version: int, optional
        :param environment_map_extension_id: The ID of the environment map extension. To find the environmentMapExtensionId, you can first query the [Environment Map Extension object](/api/platformapi#tag/EnvironmentMapExtension) to retrieve a list of all available environment extensions for an account and copy the resultant environment map extension ID., defaults to None
        :type environment_map_extension_id: str, optional
        """
        if component_id is not SENTINEL:
            self.component_id = component_id
        if component_name is not SENTINEL:
            self.component_name = component_name
        if component_type is not SENTINEL:
            self.component_type = component_type
        if component_version is not SENTINEL:
            self.component_version = component_version
        if environment_map_extension_id is not SENTINEL:
            self.environment_map_extension_id = environment_map_extension_id
        self._kwargs = kwargs
