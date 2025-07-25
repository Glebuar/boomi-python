
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_user import SharedWebServerUser


@JsonMap({"enable_apim_internal_roles": "enableAPIMInternalRoles"})
class SharedWebServerUserManagement(BaseModel):
    """SharedWebServerUserManagement

    :param enable_apim_internal_roles: enable_apim_internal_roles, defaults to None
    :type enable_apim_internal_roles: bool, optional
    :param users: users, defaults to None
    :type users: List[SharedWebServerUser], optional
    """

    def __init__(
        self,
        enable_apim_internal_roles: bool = SENTINEL,
        users: List[SharedWebServerUser] = SENTINEL,
        **kwargs,
    ):
        """SharedWebServerUserManagement

        :param enable_apim_internal_roles: enable_apim_internal_roles, defaults to None
        :type enable_apim_internal_roles: bool, optional
        :param users: users, defaults to None
        :type users: List[SharedWebServerUser], optional
        """
        if enable_apim_internal_roles is not SENTINEL:
            self.enable_apim_internal_roles = enable_apim_internal_roles
        if users is not SENTINEL:
            self.users = self._define_list(users, SharedWebServerUser)
        self._kwargs = kwargs
