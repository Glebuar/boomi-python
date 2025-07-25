
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .field_summary import FieldSummary


@JsonMap(
    {
        "connection_id": "connectionId",
        "environment_id": "environmentId",
        "extension_group_id": "extensionGroupId",
        "id_": "id",
        "process_id": "processId",
    }
)
class EnvironmentConnectionFieldExtensionSummary(BaseModel):
    """EnvironmentConnectionFieldExtensionSummary

    :param connection_id: connection_id, defaults to None
    :type connection_id: str, optional
    :param environment_id: environment_id, defaults to None
    :type environment_id: str, optional
    :param extension_group_id: extension_group_id, defaults to None
    :type extension_group_id: str, optional
    :param field: field
    :type field: FieldSummary
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        field: FieldSummary,
        connection_id: str = SENTINEL,
        environment_id: str = SENTINEL,
        extension_group_id: str = SENTINEL,
        id_: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs,
    ):
        """EnvironmentConnectionFieldExtensionSummary

        :param connection_id: connection_id, defaults to None
        :type connection_id: str, optional
        :param environment_id: environment_id, defaults to None
        :type environment_id: str, optional
        :param extension_group_id: extension_group_id, defaults to None
        :type extension_group_id: str, optional
        :param field: field
        :type field: FieldSummary
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        """
        if connection_id is not SENTINEL:
            self.connection_id = connection_id
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if extension_group_id is not SENTINEL:
            self.extension_group_id = extension_group_id
        self.field = self._define_object(field, FieldSummary)
        if id_ is not SENTINEL:
            self.id_ = id_
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
