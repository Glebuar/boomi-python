
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "account_group_id": "accountGroupId",
        "first_name": "firstName",
        "id_": "id",
        "last_name": "lastName",
        "notify_user": "notifyUser",
        "role_id": "roleId",
        "user_id": "userId",
    }
)
class AccountGroupUserRole(BaseModel):
    """AccountGroupUserRole

    :param account_group_id: The ID of the account group., defaults to None
    :type account_group_id: str, optional
    :param first_name: The first name of the user., defaults to None
    :type first_name: str, optional
    :param id_: The object’s conceptual ID, which is synthesized from the role, user, and account group IDs., defaults to None
    :type id_: str, optional
    :param last_name: The last name of the user., defaults to None
    :type last_name: str, optional
    :param notify_user: If true, which is the default, users receive an email notification when adding them to the account group., defaults to None
    :type notify_user: bool, optional
    :param role_id: The ID of the role., defaults to None
    :type role_id: str, optional
    :param user_id: The user ID., defaults to None
    :type user_id: str, optional
    """

    def __init__(
        self,
        account_group_id: str = SENTINEL,
        first_name: str = SENTINEL,
        id_: str = SENTINEL,
        last_name: str = SENTINEL,
        notify_user: bool = SENTINEL,
        role_id: str = SENTINEL,
        user_id: str = SENTINEL,
        **kwargs
    ):
        """AccountGroupUserRole

        :param account_group_id: The ID of the account group., defaults to None
        :type account_group_id: str, optional
        :param first_name: The first name of the user., defaults to None
        :type first_name: str, optional
        :param id_: The object’s conceptual ID, which is synthesized from the role, user, and account group IDs., defaults to None
        :type id_: str, optional
        :param last_name: The last name of the user., defaults to None
        :type last_name: str, optional
        :param notify_user: If true, which is the default, users receive an email notification when adding them to the account group., defaults to None
        :type notify_user: bool, optional
        :param role_id: The ID of the role., defaults to None
        :type role_id: str, optional
        :param user_id: The user ID., defaults to None
        :type user_id: str, optional
        """
        if account_group_id is not SENTINEL:
            self.account_group_id = account_group_id
        if first_name is not SENTINEL:
            self.first_name = first_name
        if id_ is not SENTINEL:
            self.id_ = id_
        if last_name is not SENTINEL:
            self.last_name = last_name
        if notify_user is not SENTINEL:
            self.notify_user = notify_user
        if role_id is not SENTINEL:
            self.role_id = role_id
        if user_id is not SENTINEL:
            self.user_id = user_id
        self._kwargs = kwargs
