
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "environment_id": "environmentId",
        "id_": "id",
        "integration_pack_instance_id": "integrationPackInstanceId",
    }
)
class IntegrationPackEnvironmentAttachment(BaseModel):
    """IntegrationPackEnvironmentAttachment

    :param environment_id: A unique ID assigned by the system to the environment., defaults to None
    :type environment_id: str, optional
    :param id_: The object’s conceptual ID, which is synthesized from the environment and integration pack instance IDs., defaults to None
    :type id_: str, optional
    :param integration_pack_instance_id: A unique ID assigned by the system to the integration pack instance., defaults to None
    :type integration_pack_instance_id: str, optional
    """

    def __init__(
        self,
        environment_id: str = SENTINEL,
        id_: str = SENTINEL,
        integration_pack_instance_id: str = SENTINEL,
        **kwargs
    ):
        """IntegrationPackEnvironmentAttachment

        :param environment_id: A unique ID assigned by the system to the environment., defaults to None
        :type environment_id: str, optional
        :param id_: The object’s conceptual ID, which is synthesized from the environment and integration pack instance IDs., defaults to None
        :type id_: str, optional
        :param integration_pack_instance_id: A unique ID assigned by the system to the integration pack instance., defaults to None
        :type integration_pack_instance_id: str, optional
        """
        if environment_id is not SENTINEL:
            self.environment_id = environment_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if integration_pack_instance_id is not SENTINEL:
            self.integration_pack_instance_id = integration_pack_instance_id
        self._kwargs = kwargs
