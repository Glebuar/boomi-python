
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ReferencesType(Enum):
    """An enumeration representing different categories.

    :cvar DEPENDENT: "DEPENDENT"
    :vartype DEPENDENT: str
    :cvar INDEPENDENT: "INDEPENDENT"
    :vartype INDEPENDENT: str
    """

    DEPENDENT = "DEPENDENT"
    INDEPENDENT = "INDEPENDENT"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ReferencesType._member_map_.values()))


@JsonMap(
    {
        "component_id": "componentId",
        "parent_component_id": "parentComponentId",
        "parent_version": "parentVersion",
        "type_": "type",
        "branch_id": "branchId",
    }
)
class References(BaseModel):
    """References

    :param component_id: The ID of the secondary component. The component ID is available in the Revision History dialog, which you can access from the Build page in the service., defaults to None
    :type component_id: str, optional
    :param parent_component_id: The ID of the primary component that the secondary components reference. You can use this attribute specifically in the QUERY operation. The component ID is available in the Revision History dialog, which you can access from the Build page in the service., defaults to None
    :type parent_component_id: str, optional
    :param parent_version: The revision number of the primary component. This attribute is used specifically in the QUERY operation. A component's version number is available in the Revision History dialog, which you can access from the Build page in the service., defaults to None
    :type parent_version: int, optional
    :param type_: The type of reference component.   - A value of DEPENDENT indicates that the component is included automatically in a process at packaging and deployment time.   - A value of INDEPENDENT indicates the component is standalone, and you must package and deploy it individually and manually, though you might use it in a process configuration.   For more information on component reference types, see the topic [Component References](https://help.boomi.com/docs/Atomsphere/Integration/Process%20building/int-Component_references_8d7cf9db-2716-4301-b8d8-46eb9f055999)., defaults to None
    :type type_: ReferencesType, optional
    :param branch_id: If specified, the ID of the branch on which you want to query., defaults to None
    :type branch_id: str, optional
    """

    def __init__(
        self,
        component_id: str = SENTINEL,
        parent_component_id: str = SENTINEL,
        parent_version: int = SENTINEL,
        type_: ReferencesType = SENTINEL,
        branch_id: str = SENTINEL,
        **kwargs
    ):
        """References

        :param component_id: The ID of the secondary component. The component ID is available in the Revision History dialog, which you can access from the Build page in the service., defaults to None
        :type component_id: str, optional
        :param parent_component_id: The ID of the primary component that the secondary components reference. You can use this attribute specifically in the QUERY operation. The component ID is available in the Revision History dialog, which you can access from the Build page in the service., defaults to None
        :type parent_component_id: str, optional
        :param parent_version: The revision number of the primary component. This attribute is used specifically in the QUERY operation. A component's version number is available in the Revision History dialog, which you can access from the Build page in the service., defaults to None
        :type parent_version: int, optional
        :param type_: The type of reference component.   - A value of DEPENDENT indicates that the component is included automatically in a process at packaging and deployment time.   - A value of INDEPENDENT indicates the component is standalone, and you must package and deploy it individually and manually, though you might use it in a process configuration.   For more information on component reference types, see the topic [Component References](https://help.boomi.com/docs/Atomsphere/Integration/Process%20building/int-Component_references_8d7cf9db-2716-4301-b8d8-46eb9f055999)., defaults to None
        :type type_: ReferencesType, optional
        :param branch_id: If specified, the ID of the branch on which you want to query., defaults to None
        :type branch_id: str, optional
        """
        if component_id is not SENTINEL:
            self.component_id = component_id
        if parent_component_id is not SENTINEL:
            self.parent_component_id = parent_component_id
        if parent_version is not SENTINEL:
            self.parent_version = parent_version
        if type_ is not SENTINEL:
            self.type_ = self._enum_matching(type_, ReferencesType.list(), "type_")
        if branch_id is not SENTINEL:
            self.branch_id = branch_id
        self._kwargs = kwargs
