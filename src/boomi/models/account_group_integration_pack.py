
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class AccountGroupIntegrationPackInstallationType(Enum):
    """An enumeration representing different categories.

    :cvar SINGLE: "SINGLE"
    :vartype SINGLE: str
    :cvar MULTI: "MULTI"
    :vartype MULTI: str
    """

    SINGLE = "SINGLE"
    MULTI = "MULTI"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                AccountGroupIntegrationPackInstallationType._member_map_.values(),
            )
        )


@JsonMap(
    {
        "account_group_id": "accountGroupId",
        "id_": "id",
        "installation_type": "installationType",
        "integration_pack_id": "integrationPackId",
        "integration_pack_name": "integrationPackName",
    }
)
class AccountGroupIntegrationPack(BaseModel):
    """AccountGroupIntegrationPack

    :param account_group_id: The ID of the account group., defaults to None
    :type account_group_id: str, optional
    :param id_: A unique ID assigned by the system to the integration pack. This field populates only if you add the integration pack to an account group., defaults to None
    :type id_: str, optional
    :param installation_type: The type of integration pack. Possible values:    - SINGLE — single attachment  - MULTI — multiple attachment, defaults to None
    :type installation_type: AccountGroupIntegrationPackInstallationType, optional
    :param integration_pack_id: A unique ID assigned by the system to the integration pack., defaults to None
    :type integration_pack_id: str, optional
    :param integration_pack_name: The name of the integration pack., defaults to None
    :type integration_pack_name: str, optional
    """

    def __init__(
        self,
        account_group_id: str = SENTINEL,
        id_: str = SENTINEL,
        installation_type: AccountGroupIntegrationPackInstallationType = SENTINEL,
        integration_pack_id: str = SENTINEL,
        integration_pack_name: str = SENTINEL,
        **kwargs
    ):
        """AccountGroupIntegrationPack

        :param account_group_id: The ID of the account group., defaults to None
        :type account_group_id: str, optional
        :param id_: A unique ID assigned by the system to the integration pack. This field populates only if you add the integration pack to an account group., defaults to None
        :type id_: str, optional
        :param installation_type: The type of integration pack. Possible values:    - SINGLE — single attachment  - MULTI — multiple attachment, defaults to None
        :type installation_type: AccountGroupIntegrationPackInstallationType, optional
        :param integration_pack_id: A unique ID assigned by the system to the integration pack., defaults to None
        :type integration_pack_id: str, optional
        :param integration_pack_name: The name of the integration pack., defaults to None
        :type integration_pack_name: str, optional
        """
        if account_group_id is not SENTINEL:
            self.account_group_id = account_group_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if installation_type is not SENTINEL:
            self.installation_type = self._enum_matching(
                installation_type,
                AccountGroupIntegrationPackInstallationType.list(),
                "installation_type",
            )
        if integration_pack_id is not SENTINEL:
            self.integration_pack_id = integration_pack_id
        if integration_pack_name is not SENTINEL:
            self.integration_pack_name = integration_pack_name
        self._kwargs = kwargs
