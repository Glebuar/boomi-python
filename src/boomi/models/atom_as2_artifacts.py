
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"atom_id": "atomId", "log_date": "logDate"})
class AtomAs2Artifacts(BaseModel):
    """AtomAs2Artifacts

    :param atom_id: The ID of the Runtime., defaults to None
    :type atom_id: str, optional
    :param log_date: The date of the logged events., defaults to None
    :type log_date: str, optional
    """

    def __init__(self, atom_id: str = SENTINEL, log_date: str = SENTINEL, **kwargs):
        """AtomAs2Artifacts

        :param atom_id: The ID of the Runtime., defaults to None
        :type atom_id: str, optional
        :param log_date: The date of the logged events., defaults to None
        :type log_date: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if log_date is not SENTINEL:
            self.log_date = log_date
        self._kwargs = kwargs
