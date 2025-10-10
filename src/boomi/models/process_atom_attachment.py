
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "atom_id": "atomId",
        "component_type": "componentType",
        "id_": "id",
        "process_id": "processId",
    }
)
class ProcessAtomAttachment(BaseModel):
    """ProcessAtomAttachment

    :param atom_id: atom_id, defaults to None
    :type atom_id: str, optional
    :param component_type: component_type, defaults to None
    :type component_type: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param process_id: process_id, defaults to None
    :type process_id: str, optional
    """

    def __init__(
        self,
        atom_id: str = SENTINEL,
        component_type: str = SENTINEL,
        id_: str = SENTINEL,
        process_id: str = SENTINEL,
        **kwargs
    ):
        """ProcessAtomAttachment

        :param atom_id: atom_id, defaults to None
        :type atom_id: str, optional
        :param component_type: component_type, defaults to None
        :type component_type: str, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param process_id: process_id, defaults to None
        :type process_id: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if component_type is not SENTINEL:
            self.component_type = component_type
        if id_ is not SENTINEL:
            self.id_ = id_
        if process_id is not SENTINEL:
            self.process_id = process_id
        self._kwargs = kwargs
