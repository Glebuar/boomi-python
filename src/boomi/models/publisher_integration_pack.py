
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .publisher_packaged_components import PublisherPackagedComponents


class PublisherIntegrationPackInstallationType(Enum):
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
                lambda x: x.value,
                PublisherIntegrationPackInstallationType._member_map_.values(),
            )
        )


class OperationType(Enum):
    """An enumeration representing different categories.

    :cvar ADD: "ADD"
    :vartype ADD: str
    :cvar DELETE: "DELETE"
    :vartype DELETE: str
    """

    ADD = "ADD"
    DELETE = "DELETE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, OperationType._member_map_.values()))


@JsonMap(
    {
        "description": "Description",
        "publisher_packaged_components": "PublisherPackagedComponents",
        "id_": "id",
        "installation_type": "installationType",
        "operation_type": "operationType",
    }
)
class PublisherIntegrationPack(BaseModel):
    """PublisherIntegrationPack

    :param description: description
    :type description: str
    :param publisher_packaged_components: publisher_packaged_components, defaults to None
    :type publisher_packaged_components: PublisherPackagedComponents, optional
    :param id_: A unique ID assigned by the system to the integration pack., defaults to None
    :type id_: str, optional
    :param installation_type: The type of integration pack. Possible values: - SINGLE — single attachment  - MULTI — multiple attachment, defaults to None
    :type installation_type: PublisherIntegrationPackInstallationType, optional
    :param name: The name of the integration pack., defaults to None
    :type name: str, optional
    :param operation_type: Specifies the type of operation (ADD or DELETE) to perform when updating the packaged component to the integration pack. This field is mandatory for the Update operation and is not available for other operations, defaults to None
    :type operation_type: OperationType, optional
    """

    def __init__(
        self,
        description: str,
        publisher_packaged_components: PublisherPackagedComponents = SENTINEL,
        id_: str = SENTINEL,
        installation_type: PublisherIntegrationPackInstallationType = SENTINEL,
        name: str = SENTINEL,
        operation_type: OperationType = SENTINEL,
        **kwargs,
    ):
        """PublisherIntegrationPack

        :param description: description
        :type description: str
        :param publisher_packaged_components: publisher_packaged_components, defaults to None
        :type publisher_packaged_components: PublisherPackagedComponents, optional
        :param id_: A unique ID assigned by the system to the integration pack., defaults to None
        :type id_: str, optional
        :param installation_type: The type of integration pack. Possible values: - SINGLE — single attachment  - MULTI — multiple attachment, defaults to None
        :type installation_type: PublisherIntegrationPackInstallationType, optional
        :param name: The name of the integration pack., defaults to None
        :type name: str, optional
        :param operation_type: Specifies the type of operation (ADD or DELETE) to perform when updating the packaged component to the integration pack. This field is mandatory for the Update operation and is not available for other operations, defaults to None
        :type operation_type: OperationType, optional
        """
        self.description = description
        if publisher_packaged_components is not SENTINEL:
            self.publisher_packaged_components = self._define_object(
                publisher_packaged_components, PublisherPackagedComponents
            )
        if id_ is not SENTINEL:
            self.id_ = id_
        if installation_type is not SENTINEL:
            self.installation_type = self._enum_matching(
                installation_type,
                PublisherIntegrationPackInstallationType.list(),
                "installation_type",
            )
        if name is not SENTINEL:
            self.name = name
        if operation_type is not SENTINEL:
            self.operation_type = self._enum_matching(
                operation_type, OperationType.list(), "operation_type"
            )
        self._kwargs = kwargs
