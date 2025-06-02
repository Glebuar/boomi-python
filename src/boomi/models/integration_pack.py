
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class IntegrationPackInstallationType(Enum):
    """An enumeration representing different categories.

    :cvar SINGLE: "SINGLE"
    :vartype SINGLE: str
    :cvar MULTI: "MULTI"
    :vartype MULTI: str
    """

    SINGLE = "SINGLE"
    MULTI = "MULTI"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, IntegrationPackInstallationType._member_map_.values()
            )
        )


@JsonMap(
    {"description": "Description", "id_": "id", "installation_type": "installationType"}
)
class IntegrationPack(BaseModel):
    """IntegrationPack

    :param description: A description of the integration pack.
    :type description: str
    :param id_: A unique ID assigned by the system to the integration pack., defaults to None
    :type id_: str, optional
    :param installation_type: The type of integration pack. Possible values:\<br /\>-   SINGLE — single-attach\<br /\>-   MULTI — multi-attach, defaults to None
    :type installation_type: IntegrationPackInstallationType, optional
    :param name: The name of the integration pack., defaults to None
    :type name: str, optional
    """

    def __init__(
        self,
        description: str,
        id_: str = SENTINEL,
        installation_type: IntegrationPackInstallationType = SENTINEL,
        name: str = SENTINEL,
        **kwargs
    ):
        """IntegrationPack

        :param description: A description of the integration pack.
        :type description: str
        :param id_: A unique ID assigned by the system to the integration pack., defaults to None
        :type id_: str, optional
        :param installation_type: The type of integration pack. Possible values:\<br /\>-   SINGLE — single-attach\<br /\>-   MULTI — multi-attach, defaults to None
        :type installation_type: IntegrationPackInstallationType, optional
        :param name: The name of the integration pack., defaults to None
        :type name: str, optional
        """
        self.description = description
        if id_ is not SENTINEL:
            self.id_ = id_
        if installation_type is not SENTINEL:
            self.installation_type = self._enum_matching(
                installation_type,
                IntegrationPackInstallationType.list(),
                "installation_type",
            )
        if name is not SENTINEL:
            self.name = name
        self._kwargs = kwargs
