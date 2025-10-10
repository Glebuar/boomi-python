
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"account_group_id": "accountGroupId", "account_id": "accountId", "id_": "id"})
class AccountGroupAccount(BaseModel):
    """AccountGroupAccount

    :param account_group_id: The ID of the account group., defaults to None
    :type account_group_id: str, optional
    :param account_id: The ID of the account., defaults to None
    :type account_id: str, optional
    :param id_: The object’s conceptual ID from which the account and account group IDs synthesizes., defaults to None
    :type id_: str, optional
    """

    def __init__(
        self,
        account_group_id: str = SENTINEL,
        account_id: str = SENTINEL,
        id_: str = SENTINEL,
        **kwargs
    ):
        """AccountGroupAccount

        :param account_group_id: The ID of the account group., defaults to None
        :type account_group_id: str, optional
        :param account_id: The ID of the account., defaults to None
        :type account_id: str, optional
        :param id_: The object’s conceptual ID from which the account and account group IDs synthesizes., defaults to None
        :type id_: str, optional
        """
        if account_group_id is not SENTINEL:
            self.account_group_id = account_group_id
        if account_id is not SENTINEL:
            self.account_id = account_id
        if id_ is not SENTINEL:
            self.id_ = id_
        self._kwargs = kwargs
