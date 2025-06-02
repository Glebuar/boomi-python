
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"atom_id": "atomId"})
class CloudAtom(BaseModel):
    """CloudAtom

    :param atom_id: atom_id, defaults to None
    :type atom_id: str, optional
    :param deleted: deleted, defaults to None
    :type deleted: bool, optional
    """

    def __init__(self, atom_id: str = SENTINEL, deleted: bool = SENTINEL, **kwargs):
        """CloudAtom

        :param atom_id: atom_id, defaults to None
        :type atom_id: str, optional
        :param deleted: deleted, defaults to None
        :type deleted: bool, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if deleted is not SENTINEL:
            self.deleted = deleted
        self._kwargs = kwargs
