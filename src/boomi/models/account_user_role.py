
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "account_id": "accountId",
        "first_name": "firstName",
        "id_": "id",
        "last_name": "lastName",
        "notify_user": "notifyUser",
        "role_id": "roleId",
        "user_id": "userId",
    }
)
class AccountUserRole(BaseModel):
    """AccountUserRole

    :param account_id: The account ID., defaults to None
    :type account_id: str, optional
    :param first_name: The first name of a user in the account., defaults to None
    :type first_name: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param last_name: The last name of a user in the account., defaults to None
    :type last_name: str, optional
    :param notify_user: If true, defaults to None
    :type notify_user: bool, optional
    :param role_id: The ID of the role., defaults to None
    :type role_id: str, optional
    :param user_id: The user ID., defaults to None
    :type user_id: str, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        first_name: str = SENTINEL,
        id_: str = SENTINEL,
        last_name: str = SENTINEL,
        notify_user: bool = SENTINEL,
        role_id: str = SENTINEL,
        user_id: str = SENTINEL,
        **kwargs
    ):
        """AccountUserRole

        :param account_id: The account ID., defaults to None
        :type account_id: str, optional
        :param first_name: The first name of a user in the account., defaults to None
        :type first_name: str, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param last_name: The last name of a user in the account., defaults to None
        :type last_name: str, optional
        :param notify_user: If true, defaults to None
        :type notify_user: bool, optional
        :param role_id: The ID of the role., defaults to None
        :type role_id: str, optional
        :param user_id: The user ID., defaults to None
        :type user_id: str, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
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
