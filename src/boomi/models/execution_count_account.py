
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"account_id": "accountId", "atom_id": "atomId", "date_": "date"})
class ExecutionCountAccount(BaseModel):
    """ExecutionCountAccount

    :param account_id: The ID of the account under which the runs occurred., defaults to None
    :type account_id: str, optional
    :param atom_id: The ID of the Runtime on which the runs occurred., defaults to None
    :type atom_id: str, optional
    :param date_: The date on which the runs occurred. The time zone is UTC±00:00., defaults to None
    :type date_: str, optional
    :param failures: The count of failed runs., defaults to None
    :type failures: int, optional
    :param successes: The count of successful runs., defaults to None
    :type successes: int, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        atom_id: str = SENTINEL,
        date_: str = SENTINEL,
        failures: int = SENTINEL,
        successes: int = SENTINEL,
        **kwargs
    ):
        """ExecutionCountAccount

        :param account_id: The ID of the account under which the runs occurred., defaults to None
        :type account_id: str, optional
        :param atom_id: The ID of the Runtime on which the runs occurred., defaults to None
        :type atom_id: str, optional
        :param date_: The date on which the runs occurred. The time zone is UTC±00:00., defaults to None
        :type date_: str, optional
        :param failures: The count of failed runs., defaults to None
        :type failures: int, optional
        :param successes: The count of successful runs., defaults to None
        :type successes: int, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if date_ is not SENTINEL:
            self.date_ = date_
        if failures is not SENTINEL:
            self.failures = failures
        if successes is not SENTINEL:
            self.successes = successes
        self._kwargs = kwargs
