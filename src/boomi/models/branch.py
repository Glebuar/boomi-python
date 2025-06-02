
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "created_by": "createdBy",
        "created_date": "createdDate",
        "deployment_id": "deploymentId",
        "id_": "id",
        "modified_by": "modifiedBy",
        "modified_date": "modifiedDate",
        "package_id": "packageId",
        "parent_id": "parentId",
    }
)
class Branch(BaseModel):
    """Branch

    :param created_by: The user who created the branch., defaults to None
    :type created_by: str, optional
    :param created_date: The date and time when the branch was created., defaults to None
    :type created_date: str, optional
    :param deleted: Whether the branch is deleted., defaults to None
    :type deleted: bool, optional
    :param deployment_id: deployment_id, defaults to None
    :type deployment_id: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param id_: The ID of the branch., defaults to None
    :type id_: str, optional
    :param modified_by: The user who last modified the branch., defaults to None
    :type modified_by: str, optional
    :param modified_date: The date and time when the branch was updated., defaults to None
    :type modified_date: str, optional
    :param name: The name of the branch., defaults to None
    :type name: str, optional
    :param package_id: The ID of the packaged component from which the branch is created., defaults to None
    :type package_id: str, optional
    :param parent_id: The ID of the parent branch., defaults to None
    :type parent_id: str, optional
    :param ready: Whether the branch is ready to use., defaults to None
    :type ready: bool, optional
    :param stage: The branch status: CREATING, NORMAL (ready for use), or DELETING., defaults to None
    :type stage: str, optional
    """

    def __init__(
        self,
        created_by: str = SENTINEL,
        created_date: str = SENTINEL,
        deleted: bool = SENTINEL,
        deployment_id: str = SENTINEL,
        description: str = SENTINEL,
        id_: str = SENTINEL,
        modified_by: str = SENTINEL,
        modified_date: str = SENTINEL,
        name: str = SENTINEL,
        package_id: str = SENTINEL,
        parent_id: str = SENTINEL,
        ready: bool = SENTINEL,
        stage: str = SENTINEL,
        **kwargs
    ):
        """Branch

        :param created_by: The user who created the branch., defaults to None
        :type created_by: str, optional
        :param created_date: The date and time when the branch was created., defaults to None
        :type created_date: str, optional
        :param deleted: Whether the branch is deleted., defaults to None
        :type deleted: bool, optional
        :param deployment_id: deployment_id, defaults to None
        :type deployment_id: str, optional
        :param description: description, defaults to None
        :type description: str, optional
        :param id_: The ID of the branch., defaults to None
        :type id_: str, optional
        :param modified_by: The user who last modified the branch., defaults to None
        :type modified_by: str, optional
        :param modified_date: The date and time when the branch was updated., defaults to None
        :type modified_date: str, optional
        :param name: The name of the branch., defaults to None
        :type name: str, optional
        :param package_id: The ID of the packaged component from which the branch is created., defaults to None
        :type package_id: str, optional
        :param parent_id: The ID of the parent branch., defaults to None
        :type parent_id: str, optional
        :param ready: Whether the branch is ready to use., defaults to None
        :type ready: bool, optional
        :param stage: The branch status: CREATING, NORMAL (ready for use), or DELETING., defaults to None
        :type stage: str, optional
        """
        if created_by is not SENTINEL:
            self.created_by = created_by
        if created_date is not SENTINEL:
            self.created_date = created_date
        if deleted is not SENTINEL:
            self.deleted = deleted
        if deployment_id is not SENTINEL:
            self.deployment_id = deployment_id
        if description is not SENTINEL:
            self.description = description
        if id_ is not SENTINEL:
            self.id_ = id_
        if modified_by is not SENTINEL:
            self.modified_by = modified_by
        if modified_date is not SENTINEL:
            self.modified_date = modified_date
        if name is not SENTINEL:
            self.name = name
        if package_id is not SENTINEL:
            self.package_id = package_id
        if parent_id is not SENTINEL:
            self.parent_id = parent_id
        if ready is not SENTINEL:
            self.ready = ready
        if stage is not SENTINEL:
            self.stage = stage
        self._kwargs = kwargs
