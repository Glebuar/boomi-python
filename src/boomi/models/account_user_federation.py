
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "account_id": "accountId",
        "federation_id": "federationId",
        "id_": "id",
        "user_id": "userId",
    }
)
class AccountUserFederation(BaseModel):
    """AccountUserFederation

    :param account_id: The account ID., defaults to None
    :type account_id: str, optional
    :param federation_id: The federation ID uniquely identifies the user., defaults to None
    :type federation_id: str, optional
    :param id_: The object’s conceptual ID, which is synthesized from the federation, user, and account IDs., defaults to None
    :type id_: str, optional
    :param user_id: The user ID., defaults to None
    :type user_id: str, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        federation_id: str = SENTINEL,
        id_: str = SENTINEL,
        user_id: str = SENTINEL,
        **kwargs
    ):
        """AccountUserFederation

        :param account_id: The account ID., defaults to None
        :type account_id: str, optional
        :param federation_id: The federation ID uniquely identifies the user., defaults to None
        :type federation_id: str, optional
        :param id_: The object’s conceptual ID, which is synthesized from the federation, user, and account IDs., defaults to None
        :type id_: str, optional
        :param user_id: The user ID., defaults to None
        :type user_id: str, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if federation_id is not SENTINEL:
            self.federation_id = federation_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if user_id is not SENTINEL:
            self.user_id = user_id
        self._kwargs = kwargs
