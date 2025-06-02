
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ChangeType(Enum):
    """An enumeration representing different categories.

    :cvar ADDED: "ADDED"
    :vartype ADDED: str
    :cvar MODIFIED: "MODIFIED"
    :vartype MODIFIED: str
    :cvar DELETED: "DELETED"
    :vartype DELETED: str
    """

    ADDED = "ADDED"
    MODIFIED = "MODIFIED"
    DELETED = "DELETED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ChangeType._member_map_.values()))


class Resolution(Enum):
    """An enumeration representing different categories.

    :cvar OVERRIDE: "OVERRIDE"
    :vartype OVERRIDE: str
    :cvar KEEPDESTINATION: "KEEP_DESTINATION"
    :vartype KEEPDESTINATION: str
    """

    OVERRIDE = "OVERRIDE"
    KEEPDESTINATION = "KEEP_DESTINATION"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Resolution._member_map_.values()))


class MergeRequestDetailStage(Enum):
    """An enumeration representing different categories.

    :cvar DRAFTED: "DRAFTED"
    :vartype DRAFTED: str
    :cvar REVIEWED: "REVIEWED"
    :vartype REVIEWED: str
    :cvar CONFLICTRESOLVED: "CONFLICT_RESOLVED"
    :vartype CONFLICTRESOLVED: str
    :cvar MERGED: "MERGED"
    :vartype MERGED: str
    :cvar REVERTED: "REVERTED"
    :vartype REVERTED: str
    """

    DRAFTED = "DRAFTED"
    REVIEWED = "REVIEWED"
    CONFLICTRESOLVED = "CONFLICT_RESOLVED"
    MERGED = "MERGED"
    REVERTED = "REVERTED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, MergeRequestDetailStage._member_map_.values())
        )


@JsonMap(
    {
        "change_type": "changeType",
        "component_guid": "componentGuid",
        "created_by": "createdBy",
        "created_date": "createdDate",
        "destination_revision": "destinationRevision",
        "locked_on_destination_branch": "lockedOnDestinationBranch",
        "merge_revision": "mergeRevision",
        "modified_by": "modifiedBy",
        "modified_date": "modifiedDate",
        "source_revision": "sourceRevision",
    }
)
class MergeRequestDetail(BaseModel):
    """MergeRequestDetail

    :param change_type: change_type, defaults to None
    :type change_type: ChangeType, optional
    :param component_guid: component_guid, defaults to None
    :type component_guid: str, optional
    :param conflict: conflict, defaults to None
    :type conflict: bool, optional
    :param created_by: created_by, defaults to None
    :type created_by: str, optional
    :param created_date: created_date, defaults to None
    :type created_date: str, optional
    :param destination_revision: destination_revision, defaults to None
    :type destination_revision: int, optional
    :param excluded: When true, signifies that a component will not be included in the Merge., defaults to None
    :type excluded: bool, optional
    :param locked_on_destination_branch: locked_on_destination_branch, defaults to None
    :type locked_on_destination_branch: bool, optional
    :param merge_revision: merge_revision, defaults to None
    :type merge_revision: int, optional
    :param modified_by: modified_by, defaults to None
    :type modified_by: str, optional
    :param modified_date: modified_date, defaults to None
    :type modified_date: str, optional
    :param resolution: resolution, defaults to None
    :type resolution: Resolution, optional
    :param source_revision: source_revision, defaults to None
    :type source_revision: int, optional
    :param stage: stage, defaults to None
    :type stage: MergeRequestDetailStage, optional
    """

    def __init__(
        self,
        change_type: ChangeType = SENTINEL,
        component_guid: str = SENTINEL,
        conflict: bool = SENTINEL,
        created_by: str = SENTINEL,
        created_date: str = SENTINEL,
        destination_revision: int = SENTINEL,
        excluded: bool = SENTINEL,
        locked_on_destination_branch: bool = SENTINEL,
        merge_revision: int = SENTINEL,
        modified_by: str = SENTINEL,
        modified_date: str = SENTINEL,
        resolution: Resolution = SENTINEL,
        source_revision: int = SENTINEL,
        stage: MergeRequestDetailStage = SENTINEL,
        **kwargs
    ):
        """MergeRequestDetail

        :param change_type: change_type, defaults to None
        :type change_type: ChangeType, optional
        :param component_guid: component_guid, defaults to None
        :type component_guid: str, optional
        :param conflict: conflict, defaults to None
        :type conflict: bool, optional
        :param created_by: created_by, defaults to None
        :type created_by: str, optional
        :param created_date: created_date, defaults to None
        :type created_date: str, optional
        :param destination_revision: destination_revision, defaults to None
        :type destination_revision: int, optional
        :param excluded: When true, signifies that a component will not be included in the Merge., defaults to None
        :type excluded: bool, optional
        :param locked_on_destination_branch: locked_on_destination_branch, defaults to None
        :type locked_on_destination_branch: bool, optional
        :param merge_revision: merge_revision, defaults to None
        :type merge_revision: int, optional
        :param modified_by: modified_by, defaults to None
        :type modified_by: str, optional
        :param modified_date: modified_date, defaults to None
        :type modified_date: str, optional
        :param resolution: resolution, defaults to None
        :type resolution: Resolution, optional
        :param source_revision: source_revision, defaults to None
        :type source_revision: int, optional
        :param stage: stage, defaults to None
        :type stage: MergeRequestDetailStage, optional
        """
        if change_type is not SENTINEL:
            self.change_type = self._enum_matching(
                change_type, ChangeType.list(), "change_type"
            )
        if component_guid is not SENTINEL:
            self.component_guid = component_guid
        if conflict is not SENTINEL:
            self.conflict = conflict
        if created_by is not SENTINEL:
            self.created_by = created_by
        if created_date is not SENTINEL:
            self.created_date = created_date
        if destination_revision is not SENTINEL:
            self.destination_revision = destination_revision
        if excluded is not SENTINEL:
            self.excluded = excluded
        if locked_on_destination_branch is not SENTINEL:
            self.locked_on_destination_branch = locked_on_destination_branch
        if merge_revision is not SENTINEL:
            self.merge_revision = merge_revision
        if modified_by is not SENTINEL:
            self.modified_by = modified_by
        if modified_date is not SENTINEL:
            self.modified_date = modified_date
        if resolution is not SENTINEL:
            self.resolution = self._enum_matching(
                resolution, Resolution.list(), "resolution"
            )
        if source_revision is not SENTINEL:
            self.source_revision = source_revision
        if stage is not SENTINEL:
            self.stage = self._enum_matching(
                stage, MergeRequestDetailStage.list(), "stage"
            )
        self._kwargs = kwargs
