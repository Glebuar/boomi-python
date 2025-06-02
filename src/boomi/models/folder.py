
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .permitted_roles import PermittedRoles


@JsonMap(
    {
        "permitted_roles": "PermittedRoles",
        "full_path": "fullPath",
        "id_": "id",
        "parent_id": "parentId",
        "parent_name": "parentName",
    }
)
class Folder(BaseModel):
    """Folder

    :param permitted_roles: Optional. The defined role assigned to the available folder object., defaults to None
    :type permitted_roles: PermittedRoles, optional
    :param deleted: Read only. Indicates if the component is deleted. A true value indicates a deleted status, whereas a false value indicates an active status., defaults to None
    :type deleted: bool, optional
    :param full_path: Read only. The full path of the folder location in which the component most currently resides within the Component Explorer hierarchy., defaults to None
    :type full_path: str, optional
    :param id_: Required. Read only. The -generated, unique identifier of the folder., defaults to None
    :type id_: str, optional
    :param name: Required. The user-defined name given to the folder., defaults to None
    :type name: str, optional
    :param parent_id: Required. The -generated, unique identifier of the parent folder., defaults to None
    :type parent_id: str, optional
    :param parent_name: parent_name, defaults to None
    :type parent_name: str, optional
    """

    def __init__(
        self,
        permitted_roles: PermittedRoles = SENTINEL,
        deleted: bool = SENTINEL,
        full_path: str = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        parent_id: str = SENTINEL,
        parent_name: str = SENTINEL,
        **kwargs,
    ):
        """Folder

        :param permitted_roles: Optional. The defined role assigned to the available folder object., defaults to None
        :type permitted_roles: PermittedRoles, optional
        :param deleted: Read only. Indicates if the component is deleted. A true value indicates a deleted status, whereas a false value indicates an active status., defaults to None
        :type deleted: bool, optional
        :param full_path: Read only. The full path of the folder location in which the component most currently resides within the Component Explorer hierarchy., defaults to None
        :type full_path: str, optional
        :param id_: Required. Read only. The -generated, unique identifier of the folder., defaults to None
        :type id_: str, optional
        :param name: Required. The user-defined name given to the folder., defaults to None
        :type name: str, optional
        :param parent_id: Required. The -generated, unique identifier of the parent folder., defaults to None
        :type parent_id: str, optional
        :param parent_name: parent_name, defaults to None
        :type parent_name: str, optional
        """
        if permitted_roles is not SENTINEL:
            self.permitted_roles = self._define_object(permitted_roles, PermittedRoles)
        if deleted is not SENTINEL:
            self.deleted = deleted
        if full_path is not SENTINEL:
            self.full_path = full_path
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        if parent_id is not SENTINEL:
            self.parent_id = parent_id
        if parent_name is not SENTINEL:
            self.parent_name = parent_name
        self._kwargs = kwargs
