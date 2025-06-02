
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "atom_id": "atomId",
        "id_": "id",
        "integration_pack_instance_id": "integrationPackInstanceId",
    }
)
class IntegrationPackAtomAttachment(BaseModel):
    """IntegrationPackAtomAttachment

    :param atom_id: A unique ID assigned by the system to the Runtime., defaults to None
    :type atom_id: str, optional
    :param id_: The object’s conceptual ID, which is synthesized from the Runtime and integration pack instance IDs., defaults to None
    :type id_: str, optional
    :param integration_pack_instance_id: A unique ID assigned by the system to the integration pack instance., defaults to None
    :type integration_pack_instance_id: str, optional
    """

    def __init__(
        self,
        atom_id: str = SENTINEL,
        id_: str = SENTINEL,
        integration_pack_instance_id: str = SENTINEL,
        **kwargs
    ):
        """IntegrationPackAtomAttachment

        :param atom_id: A unique ID assigned by the system to the Runtime., defaults to None
        :type atom_id: str, optional
        :param id_: The object’s conceptual ID, which is synthesized from the Runtime and integration pack instance IDs., defaults to None
        :type id_: str, optional
        :param integration_pack_instance_id: A unique ID assigned by the system to the integration pack instance., defaults to None
        :type integration_pack_instance_id: str, optional
        """
        if atom_id is not SENTINEL:
            self.atom_id = atom_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if integration_pack_instance_id is not SENTINEL:
            self.integration_pack_instance_id = integration_pack_instance_id
        self._kwargs = kwargs
