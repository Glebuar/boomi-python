
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "account_id": "accountId",
        "cloud_id": "cloudId",
        "id_": "id",
        "max_atom_attachment": "maxAtomAttachment",
    }
)
class AccountCloudAttachmentQuota(BaseModel):
    """AccountCloudAttachmentQuota

    :param account_id: The ID of the account authorizing the call., defaults to None
    :type account_id: str, optional
    :param cloud_id: The ID of the Runtime cloud that you want to get, add, edit, or delete a Cloud quota., defaults to None
    :type cloud_id: str, optional
    :param id_: A unique ID generated for a newly created or recently updated Cloud quota \(using the Account Cloud Attachment quota object\). You can use this ID to get a Cloud quota for an account's specific Cloud ID., defaults to None
    :type id_: str, optional
    :param max_atom_attachment: The number of Runtime attachments that you want to set on the Cloud quota., defaults to None
    :type max_atom_attachment: int, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        cloud_id: str = SENTINEL,
        id_: str = SENTINEL,
        max_atom_attachment: int = SENTINEL,
        **kwargs
    ):
        """AccountCloudAttachmentQuota

        :param account_id: The ID of the account authorizing the call., defaults to None
        :type account_id: str, optional
        :param cloud_id: The ID of the Runtime cloud that you want to get, add, edit, or delete a Cloud quota., defaults to None
        :type cloud_id: str, optional
        :param id_: A unique ID generated for a newly created or recently updated Cloud quota \(using the Account Cloud Attachment quota object\). You can use this ID to get a Cloud quota for an account's specific Cloud ID., defaults to None
        :type id_: str, optional
        :param max_atom_attachment: The number of Runtime attachments that you want to set on the Cloud quota., defaults to None
        :type max_atom_attachment: int, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if cloud_id is not SENTINEL:
            self.cloud_id = cloud_id
        if id_ is not SENTINEL:
            self.id_ = id_
        if max_atom_attachment is not SENTINEL:
            self.max_atom_attachment = max_atom_attachment
        self._kwargs = kwargs
