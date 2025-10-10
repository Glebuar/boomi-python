
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .field_summary import FieldSummary


@JsonMap(
    {
        "atom_id": "atomId",
        "connection_id": "connectionId",
        "extension_group_id": "extensionGroupId",
        "id_": "id",
        "process_id": "processId",
    }
)
class AtomConnectionFieldExtensionSummary(BaseModel):
    """AtomConnectionFieldExtensionSummary

    :param atom_id: The ID of the Runtime., defaults to None
    :type atom_id: str, optional
    :param connection_id: The ID of the connection., defaults to None
    :type connection_id: str, optional
    :param extension_group_id: If the process is in a multi-install integration pack, this is the ID of the multi-install integration pack, which is the same as the ID of the process., defaults to None
    :type extension_group_id: str, optional
    :param field: field
    :type field: FieldSummary
    :param id_: The ID of the object. This is a conceptual ID synthesized from the IDs of the\<br /\> -   process\<br /\>-   connection\<br /\> -   multi-install integration pack \(extensionGroupId\), if applicable\<br /\>-   Atom, defaults to None
    :type id_: str, optional
    :param process_id: The ID of the process., defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        field: FieldSummary,
        atom_id: str = SENTINEL,
        connection_id: str = SENTINEL,
        extension_group_id: str = SENTINEL,
        id_: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs,
    ):
        """AtomConnectionFieldExtensionSummary

        :param atom_id: The ID of the Runtime., defaults to None
        :type atom_id: str, optional
        :param connection_id: The ID of the connection., defaults to None
        :type connection_id: str, optional
        :param extension_group_id: If the process is in a multi-install integration pack, this is the ID of the multi-install integration pack, which is the same as the ID of the process., defaults to None
        :type extension_group_id: str, optional
        :param field: field
        :type field: FieldSummary
        :param id_: The ID of the object. This is a conceptual ID synthesized from the IDs of the\<br /\> -   process\<br /\>-   connection\<br /\> -   multi-install integration pack \(extensionGroupId\), if applicable\<br /\>-   Atom, defaults to None
        :type id_: str, optional
        :param process_id: The ID of the process., defaults to None
        :type process_id: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if connection_id is not SENTINEL:
            self.connection_id = connection_id
        if extension_group_id is not SENTINEL:
            self.extension_group_id = extension_group_id
        self.field = self._define_object(field, FieldSummary)
        if id_ is not SENTINEL:
            self.id_ = id_
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
