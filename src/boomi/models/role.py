
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .privileges import Privileges


@JsonMap(
    {
        "description": "Description",
        "privileges": "Privileges",
        "account_id": "accountId",
        "id_": "id",
        "parent_id": "parentId",
    }
)
class Role(BaseModel):
    """Role

    :param description: Description of the role, defaults to None
    :type description: str, optional
    :param privileges: One or more privileges assigned to the role., defaults to None
    :type privileges: Privileges, optional
    :param account_id: The account ID under which the role exists., defaults to None
    :type account_id: str, optional
    :param id_: The ID of the role., defaults to None
    :type id_: str, optional
    :param name: The name of the role., defaults to None
    :type name: str, optional
    :param parent_id: The ID of the role from which this role inherits privileges., defaults to None
    :type parent_id: str, optional
    """

    def __init__(
        self,
        description: str = SENTINEL,
        privileges: Privileges = SENTINEL,
        account_id: str = SENTINEL,
        id_: str = SENTINEL,
        name: str = SENTINEL,
        parent_id: str = SENTINEL,
        **kwargs,
    ):
        """Role

        :param description: Description of the role, defaults to None
        :type description: str, optional
        :param privileges: One or more privileges assigned to the role., defaults to None
        :type privileges: Privileges, optional
        :param account_id: The account ID under which the role exists., defaults to None
        :type account_id: str, optional
        :param id_: The ID of the role., defaults to None
        :type id_: str, optional
        :param name: The name of the role., defaults to None
        :type name: str, optional
        :param parent_id: The ID of the role from which this role inherits privileges., defaults to None
        :type parent_id: str, optional
        """
        if description is not SENTINEL:
            self.description = description
        if privileges is not SENTINEL:
            self.privileges = self._define_object(privileges, Privileges)
        if account_id is not SENTINEL:
            self.account_id = account_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if name is not SENTINEL:
            self.name = name
        if parent_id is not SENTINEL:
            self.parent_id = parent_id
        self._kwargs = kwargs
