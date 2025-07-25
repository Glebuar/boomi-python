
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"atom_id": "atomId", "environment_id": "environmentId", "id_": "id"})
class EnvironmentAtomAttachment(BaseModel):
    """EnvironmentAtomAttachment

    :param atom_id: The ID of the Runtime., defaults to None
    :type atom_id: str, optional
    :param environment_id: The ID of the environment., defaults to None
    :type environment_id: str, optional
    :param id_: The object’s conceptual ID, which is synthesized from the Runtime and environment IDs., defaults to None
    :type id_: str, optional
    """

    def __init__(
        self,
        atom_id: str = SENTINEL,
        environment_id: str = SENTINEL,
        id_: str = SENTINEL,
        **kwargs
    ):
        """EnvironmentAtomAttachment

        :param atom_id: The ID of the Runtime., defaults to None
        :type atom_id: str, optional
        :param environment_id: The ID of the environment., defaults to None
        :type environment_id: str, optional
        :param id_: The object’s conceptual ID, which is synthesized from the Runtime and environment IDs., defaults to None
        :type id_: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if id_ is not SENTINEL:
            self.id_ = id_
        self._kwargs = kwargs
