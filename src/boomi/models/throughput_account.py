
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"account_id": "accountId", "atom_id": "atomId", "date_": "date"})
class ThroughputAccount(BaseModel):
    """ThroughputAccount

    :param account_id: The account ID from which you process the data., defaults to None
    :type account_id: str, optional
    :param atom_id: The Runtime ID from which you process the data., defaults to None
    :type atom_id: str, optional
    :param date_: The processing date of the data. The time zone is UTC±00:00., defaults to None
    :type date_: str, optional
    :param value: The calculated throughput size, in bytes., defaults to None
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
        """ThroughputAccount

        :param account_id: The account ID from which you process the data., defaults to None
        :type account_id: str, optional
        :param atom_id: The Runtime ID from which you process the data., defaults to None
        :type atom_id: str, optional
        :param date_: The processing date of the data. The time zone is UTC±00:00., defaults to None
        :type date_: str, optional
        :param value: The calculated throughput size, in bytes., defaults to None
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
