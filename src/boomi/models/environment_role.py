
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"environment_id": "environmentId", "id_": "id", "role_id": "roleId"})
class EnvironmentRole(BaseModel):
    """EnvironmentRole

    :param environment_id: The environment ID., defaults to None
    :type environment_id: str, optional
    :param id_: The object’s conceptual ID, which is synthesized from the role and environment IDs., defaults to None
    :type id_: str, optional
    :param role_id: The ID of the role., defaults to None
    :type role_id: str, optional
    """

    def __init__(
        self,
        environment_id: str = SENTINEL,
        id_: str = SENTINEL,
        role_id: str = SENTINEL,
        **kwargs
    ):
        """EnvironmentRole

        :param environment_id: The environment ID., defaults to None
        :type environment_id: str, optional
        :param id_: The object’s conceptual ID, which is synthesized from the role and environment IDs., defaults to None
        :type id_: str, optional
        :param role_id: The ID of the role., defaults to None
        :type role_id: str, optional
        """
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if role_id is not SENTINEL:
            self.role_id = role_id
        self._kwargs = kwargs
