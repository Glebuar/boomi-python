
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "component_id": "componentId",
        "component_name": "componentName",
        "component_type": "componentType",
        "current_version": "currentVersion",
        "latest_version": "latestVersion",
        "pending_version": "pendingVersion",
    }
)
class PublisherPackagedComponent(BaseModel):
    """PublisherPackagedComponent

    :param component_id: ID of the primary component in the packaged component., defaults to None
    :type component_id: str, optional
    :param component_name: Name of the primary component in the packaged component., defaults to None
    :type component_name: str, optional
    :param component_type: Component type of the primary component in the packaged component., defaults to None
    :type component_type: str, optional
    :param current_version: Packaged component version of the component that is currently released in this integration pack., defaults to None
    :type current_version: str, optional
    :param deleted: If true, the packaged component will be removed from the integration pack in the next release., defaults to None
    :type deleted: bool, optional
    :param latest_version: Latest packaged component version of the component that is available to be added to this integration pack., defaults to None
    :type latest_version: str, optional
    :param pending_version: Packaged component version of the component that will be included in the next release of this integration pack., defaults to None
    :type pending_version: str, optional
    """

    def __init__(
        self,
        component_id: str = SENTINEL,
        component_name: str = SENTINEL,
        component_type: str = SENTINEL,
        current_version: str = SENTINEL,
        deleted: bool = SENTINEL,
        latest_version: str = SENTINEL,
        pending_version: str = SENTINEL,
        **kwargs
    ):
        """PublisherPackagedComponent

        :param component_id: ID of the primary component in the packaged component., defaults to None
        :type component_id: str, optional
        :param component_name: Name of the primary component in the packaged component., defaults to None
        :type component_name: str, optional
        :param component_type: Component type of the primary component in the packaged component., defaults to None
        :type component_type: str, optional
        :param current_version: Packaged component version of the component that is currently released in this integration pack., defaults to None
        :type current_version: str, optional
        :param deleted: If true, the packaged component will be removed from the integration pack in the next release., defaults to None
        :type deleted: bool, optional
        :param latest_version: Latest packaged component version of the component that is available to be added to this integration pack., defaults to None
        :type latest_version: str, optional
        :param pending_version: Packaged component version of the component that will be included in the next release of this integration pack., defaults to None
        :type pending_version: str, optional
        """
        if component_id is not SENTINEL:
            self.component_id = component_id
        if component_name is not SENTINEL:
            self.component_name = component_name
        if component_type is not SENTINEL:
            self.component_type = component_type
        if current_version is not SENTINEL:
            self.current_version = current_version
        if deleted is not SENTINEL:
            self.deleted = deleted
        if latest_version is not SENTINEL:
            self.latest_version = latest_version
        if pending_version is not SENTINEL:
            self.pending_version = pending_version
        self._kwargs = kwargs
