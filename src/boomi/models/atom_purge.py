
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"atom_id": "atomId"})
class AtomPurge(BaseModel):
    """AtomPurge

    :param atom_id: The unique ID assigned by the system to the Runtime cloud attachment. The Runtime ID is found in the user interface by navigating to **Manage \> Runtime Management** and viewing the Runtime Information panel for a selected Runtime., defaults to None
    :type atom_id: str, optional
    """

    def __init__(self, atom_id: str = SENTINEL, **kwargs):
        """AtomPurge

        :param atom_id: The unique ID assigned by the system to the Runtime cloud attachment. The Runtime ID is found in the user interface by navigating to **Manage \> Runtime Management** and viewing the Runtime Information panel for a selected Runtime., defaults to None
        :type atom_id: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        self._kwargs = kwargs
