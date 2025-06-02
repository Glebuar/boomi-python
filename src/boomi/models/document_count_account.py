
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"account_id": "accountId", "atom_id": "atomId", "date_": "date"})
class DocumentCountAccount(BaseModel):
    """DocumentCountAccount

    :param account_id: The ID of the account that processed the documents., defaults to None
    :type account_id: str, optional
    :param atom_id: The ID of the Runtime that processed the documents., defaults to None
    :type atom_id: str, optional
    :param date_: The processing date of the documents. The time zone is UTC±00:00., defaults to None
    :type date_: str, optional
    :param value: The count of processed documents., defaults to None
    :type value: int, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        atom_id: str = SENTINEL,
        date_: str = SENTINEL,
        value: int = SENTINEL,
        **kwargs
    ):
        """DocumentCountAccount

        :param account_id: The ID of the account that processed the documents., defaults to None
        :type account_id: str, optional
        :param atom_id: The ID of the Runtime that processed the documents., defaults to None
        :type atom_id: str, optional
        :param date_: The processing date of the documents. The time zone is UTC±00:00., defaults to None
        :type date_: str, optional
        :param value: The count of processed documents., defaults to None
        :type value: int, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if date_ is not SENTINEL:
            self.date_ = date_
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs
