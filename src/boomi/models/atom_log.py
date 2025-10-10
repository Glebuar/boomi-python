
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"atom_id": "atomId", "include_bin": "includeBin", "log_date": "logDate"})
class AtomLog(BaseModel):
    """AtomLog

    :param atom_id: The ID of the Runtime., defaults to None
    :type atom_id: str, optional
    :param include_bin: If true, binary files are included in the download. The default is false., defaults to None
    :type include_bin: bool, optional
    :param log_date: The date of the logged events., defaults to None
    :type log_date: str, optional
    """

    def __init__(
        self,
        atom_id: str = SENTINEL,
        include_bin: bool = SENTINEL,
        log_date: str = SENTINEL,
        **kwargs
    ):
        """AtomLog

        :param atom_id: The ID of the Runtime., defaults to None
        :type atom_id: str, optional
        :param include_bin: If true, binary files are included in the download. The default is false., defaults to None
        :type include_bin: bool, optional
        :param log_date: The date of the logged events., defaults to None
        :type log_date: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if include_bin is not SENTINEL:
            self.include_bin = include_bin
        if log_date is not SENTINEL:
            self.log_date = log_date
        self._kwargs = kwargs
