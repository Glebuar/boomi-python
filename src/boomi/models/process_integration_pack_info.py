
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "integration_pack_id": "integrationPackId",
        "integration_pack_instance_id": "integrationPackInstanceId",
    }
)
class ProcessIntegrationPackInfo(BaseModel):
    """ProcessIntegrationPackInfo

    :param integration_pack_id: If the process is in an installed integration pack, this is the unique ID assigned by the system to the integration pack., defaults to None
    :type integration_pack_id: str, optional
    :param integration_pack_instance_id: If the process is in an installed integration pack, this is the unique ID assigned by the system to the installed instance of the integration pack., defaults to None
    :type integration_pack_instance_id: str, optional
    """

    def __init__(
        self,
        integration_pack_id: str = SENTINEL,
        integration_pack_instance_id: str = SENTINEL,
        **kwargs
    ):
        """ProcessIntegrationPackInfo

        :param integration_pack_id: If the process is in an installed integration pack, this is the unique ID assigned by the system to the integration pack., defaults to None
        :type integration_pack_id: str, optional
        :param integration_pack_instance_id: If the process is in an installed integration pack, this is the unique ID assigned by the system to the installed instance of the integration pack., defaults to None
        :type integration_pack_instance_id: str, optional
        """
        if integration_pack_id is not SENTINEL:
            self.integration_pack_id = integration_pack_id
        if integration_pack_instance_id is not SENTINEL:
            self.integration_pack_instance_id = integration_pack_instance_id
        self._kwargs = kwargs
