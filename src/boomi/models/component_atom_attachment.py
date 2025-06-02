
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "atom_id": "atomId",
        "component_id": "componentId",
        "component_type": "componentType",
        "id_": "id",
    }
)
class ComponentAtomAttachment(BaseModel):
    """ComponentAtomAttachment

    :param atom_id: atom_id, defaults to None
    :type atom_id: str, optional
    :param component_id: component_id, defaults to None
    :type component_id: str, optional
    :param component_type: component_type, defaults to None
    :type component_type: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    """

    def __init__(
        self,
        atom_id: str = SENTINEL,
        component_id: str = SENTINEL,
        component_type: str = SENTINEL,
        id_: str = SENTINEL,
        **kwargs
    ):
        """ComponentAtomAttachment

        :param atom_id: atom_id, defaults to None
        :type atom_id: str, optional
        :param component_id: component_id, defaults to None
        :type component_id: str, optional
        :param component_type: component_type, defaults to None
        :type component_type: str, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if component_id is not SENTINEL:
            self.component_id = component_id
        if component_type is not SENTINEL:
            self.component_type = component_type
        if id_ is not SENTINEL:
            self.id_ = id_
        self._kwargs = kwargs
