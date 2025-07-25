
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .merge_request_details import MergeRequestDetails


class MergeRequestAction(Enum):
    """An enumeration representing different categories.

    :cvar UPDATE: "UPDATE"
    :vartype UPDATE: str
    :cvar MERGE: "MERGE"
    :vartype MERGE: str
    :cvar RETRYDRAFTING: "RETRY_DRAFTING"
    :vartype RETRYDRAFTING: str
    :cvar REVERT: "REVERT"
    :vartype REVERT: str
    """

    UPDATE = "UPDATE"
    MERGE = "MERGE"
    RETRYDRAFTING = "RETRY_DRAFTING"
    REVERT = "REVERT"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MergeRequestAction._member_map_.values()))


class PreviousStage(Enum):
    """An enumeration representing different categories.

    :cvar NOTEXIST: "NOT_EXIST"
    :vartype NOTEXIST: str
    :cvar DRAFTING: "DRAFTING"
    :vartype DRAFTING: str
    :cvar FAILEDTODRAFT: "FAILED_TO_DRAFT"
    :vartype FAILEDTODRAFT: str
    :cvar FAILEDTOREDRAFT: "FAILED_TO_REDRAFT"
    :vartype FAILEDTOREDRAFT: str
    :cvar DRAFTED: "DRAFTED"
    :vartype DRAFTED: str
    :cvar REVIEWING: "REVIEWING"
    :vartype REVIEWING: str
    :cvar MERGING: "MERGING"
    :vartype MERGING: str
    :cvar MERGED: "MERGED"
    :vartype MERGED: str
    :cvar FAILEDTOMERGE: "FAILED_TO_MERGE"
    :vartype FAILEDTOMERGE: str
    :cvar DELETED: "DELETED"
    :vartype DELETED: str
    :cvar REDRAFTING: "REDRAFTING"
    :vartype REDRAFTING: str
    :cvar REVERTED: "REVERTED"
    :vartype REVERTED: str
    """

    NOTEXIST = "NOT_EXIST"
    DRAFTING = "DRAFTING"
    FAILEDTODRAFT = "FAILED_TO_DRAFT"
    FAILEDTOREDRAFT = "FAILED_TO_REDRAFT"
    DRAFTED = "DRAFTED"
    REVIEWING = "REVIEWING"
    MERGING = "MERGING"
    MERGED = "MERGED"
    FAILEDTOMERGE = "FAILED_TO_MERGE"
    DELETED = "DELETED"
    REDRAFTING = "REDRAFTING"
    REVERTED = "REVERTED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PreviousStage._member_map_.values()))


class PriorityBranch(Enum):
    """An enumeration representing different categories.

    :cvar SOURCE: "SOURCE"
    :vartype SOURCE: str
    :cvar DESTINATION: "DESTINATION"
    :vartype DESTINATION: str
    """

    SOURCE = "SOURCE"
    DESTINATION = "DESTINATION"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PriorityBranch._member_map_.values()))


class MergeRequestStage(Enum):
    """An enumeration representing different categories.

    :cvar NOTEXIST: "NOT_EXIST"
    :vartype NOTEXIST: str
    :cvar DRAFTING: "DRAFTING"
    :vartype DRAFTING: str
    :cvar FAILEDTODRAFT: "FAILED_TO_DRAFT"
    :vartype FAILEDTODRAFT: str
    :cvar FAILEDTOREDRAFT: "FAILED_TO_REDRAFT"
    :vartype FAILEDTOREDRAFT: str
    :cvar DRAFTED: "DRAFTED"
    :vartype DRAFTED: str
    :cvar REVIEWING: "REVIEWING"
    :vartype REVIEWING: str
    :cvar MERGING: "MERGING"
    :vartype MERGING: str
    :cvar MERGED: "MERGED"
    :vartype MERGED: str
    :cvar FAILEDTOMERGE: "FAILED_TO_MERGE"
    :vartype FAILEDTOMERGE: str
    :cvar DELETED: "DELETED"
    :vartype DELETED: str
    :cvar REDRAFTING: "REDRAFTING"
    :vartype REDRAFTING: str
    :cvar REVERTED: "REVERTED"
    :vartype REVERTED: str
    """

    NOTEXIST = "NOT_EXIST"
    DRAFTING = "DRAFTING"
    FAILEDTODRAFT = "FAILED_TO_DRAFT"
    FAILEDTOREDRAFT = "FAILED_TO_REDRAFT"
    DRAFTED = "DRAFTED"
    REVIEWING = "REVIEWING"
    MERGING = "MERGING"
    MERGED = "MERGED"
    FAILEDTOMERGE = "FAILED_TO_MERGE"
    DELETED = "DELETED"
    REDRAFTING = "REDRAFTING"
    REVERTED = "REVERTED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MergeRequestStage._member_map_.values()))


class Strategy(Enum):
    """An enumeration representing different categories.

    :cvar OVERRIDE: "OVERRIDE"
    :vartype OVERRIDE: str
    :cvar CONFLICTRESOLVE: "CONFLICT_RESOLVE"
    :vartype CONFLICTRESOLVE: str
    :cvar SUBSET: "SUBSET"
    :vartype SUBSET: str
    """

    OVERRIDE = "OVERRIDE"
    CONFLICTRESOLVE = "CONFLICT_RESOLVE"
    SUBSET = "SUBSET"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Strategy._member_map_.values()))


@JsonMap(
    {
        "merge_request_details": "MergeRequestDetails",
        "created_by": "createdBy",
        "created_date": "createdDate",
        "destination_branch_id": "destinationBranchId",
        "destination_branch_name": "destinationBranchName",
        "id_": "id",
        "inactive_date": "inactiveDate",
        "lock_nonce": "lockNonce",
        "locked_by": "lockedBy",
        "locked_date": "lockedDate",
        "merge_request_action": "mergeRequestAction",
        "modified_by": "modifiedBy",
        "modified_date": "modifiedDate",
        "previous_stage": "previousStage",
        "priority_branch": "priorityBranch",
        "source_branch_id": "sourceBranchId",
        "source_branch_name": "sourceBranchName",
    }
)
class MergeRequest(BaseModel):
    """MergeRequest

    :param merge_request_details: merge_request_details
    :type merge_request_details: MergeRequestDetails
    :param created_by: The user who created the merge request., defaults to None
    :type created_by: str, optional
    :param created_date: The date and time the merge request was created., defaults to None
    :type created_date: str, optional
    :param destination_branch_id: The ID of the destination branch., defaults to None
    :type destination_branch_id: str, optional
    :param destination_branch_name: destination_branch_name, defaults to None
    :type destination_branch_name: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param inactive_date: inactive_date, defaults to None
    :type inactive_date: str, optional
    :param lock_nonce: lock_nonce, defaults to None
    :type lock_nonce: int, optional
    :param locked_by: locked_by, defaults to None
    :type locked_by: str, optional
    :param locked_date: locked_date, defaults to None
    :type locked_date: str, optional
    :param merge_request_action: merge_request_action, defaults to None
    :type merge_request_action: MergeRequestAction, optional
    :param modified_by: The user who last modified the merge request., defaults to None
    :type modified_by: str, optional
    :param modified_date: The date and time the merge request was last modified., defaults to None
    :type modified_date: str, optional
    :param note: note, defaults to None
    :type note: str, optional
    :param previous_stage: The previous stage of the merge., defaults to None
    :type previous_stage: PreviousStage, optional
    :param priority_branch: The branch which should take priority in an override merge., defaults to None
    :type priority_branch: PriorityBranch, optional
    :param source_branch_id: The ID of the source branch., defaults to None
    :type source_branch_id: str, optional
    :param source_branch_name: source_branch_name, defaults to None
    :type source_branch_name: str, optional
    :param stage: The current stage of the merge., defaults to None
    :type stage: MergeRequestStage, optional
    :param strategy: The merge strategy., defaults to None
    :type strategy: Strategy, optional
    """

    def __init__(
        self,
        merge_request_details: MergeRequestDetails,
        created_by: str = SENTINEL,
        created_date: str = SENTINEL,
        destination_branch_id: str = SENTINEL,
        destination_branch_name: str = SENTINEL,
        id_: str = SENTINEL,
        inactive_date: str = SENTINEL,
        lock_nonce: int = SENTINEL,
        locked_by: str = SENTINEL,
        locked_date: str = SENTINEL,
        merge_request_action: MergeRequestAction = SENTINEL,
        modified_by: str = SENTINEL,
        modified_date: str = SENTINEL,
        note: str = SENTINEL,
        previous_stage: PreviousStage = SENTINEL,
        priority_branch: PriorityBranch = SENTINEL,
        source_branch_id: str = SENTINEL,
        source_branch_name: str = SENTINEL,
        stage: MergeRequestStage = SENTINEL,
        strategy: Strategy = SENTINEL,
        **kwargs,
    ):
        """MergeRequest

        :param merge_request_details: merge_request_details
        :type merge_request_details: MergeRequestDetails
        :param created_by: The user who created the merge request., defaults to None
        :type created_by: str, optional
        :param created_date: The date and time the merge request was created., defaults to None
        :type created_date: str, optional
        :param destination_branch_id: The ID of the destination branch., defaults to None
        :type destination_branch_id: str, optional
        :param destination_branch_name: destination_branch_name, defaults to None
        :type destination_branch_name: str, optional
        :param id_: id_, defaults to None
        :type id_: str, optional
        :param inactive_date: inactive_date, defaults to None
        :type inactive_date: str, optional
        :param lock_nonce: lock_nonce, defaults to None
        :type lock_nonce: int, optional
        :param locked_by: locked_by, defaults to None
        :type locked_by: str, optional
        :param locked_date: locked_date, defaults to None
        :type locked_date: str, optional
        :param merge_request_action: merge_request_action, defaults to None
        :type merge_request_action: MergeRequestAction, optional
        :param modified_by: The user who last modified the merge request., defaults to None
        :type modified_by: str, optional
        :param modified_date: The date and time the merge request was last modified., defaults to None
        :type modified_date: str, optional
        :param note: note, defaults to None
        :type note: str, optional
        :param previous_stage: The previous stage of the merge., defaults to None
        :type previous_stage: PreviousStage, optional
        :param priority_branch: The branch which should take priority in an override merge., defaults to None
        :type priority_branch: PriorityBranch, optional
        :param source_branch_id: The ID of the source branch., defaults to None
        :type source_branch_id: str, optional
        :param source_branch_name: source_branch_name, defaults to None
        :type source_branch_name: str, optional
        :param stage: The current stage of the merge., defaults to None
        :type stage: MergeRequestStage, optional
        :param strategy: The merge strategy., defaults to None
        :type strategy: Strategy, optional
        """
        self.merge_request_details = self._define_object(
            merge_request_details, MergeRequestDetails
        )
        if created_by is not SENTINEL:
            self.created_by = created_by
        if created_date is not SENTINEL:
            self.created_date = created_date
        if destination_branch_id is not SENTINEL:
            self.destination_branch_id = destination_branch_id
        if destination_branch_name is not SENTINEL:
            self.destination_branch_name = destination_branch_name
        if id_ is not SENTINEL:
            self.id_ = id_
        if inactive_date is not SENTINEL:
            self.inactive_date = inactive_date
        if lock_nonce is not SENTINEL:
            self.lock_nonce = lock_nonce
        if locked_by is not SENTINEL:
            self.locked_by = locked_by
        if locked_date is not SENTINEL:
            self.locked_date = locked_date
        if merge_request_action is not SENTINEL:
            self.merge_request_action = self._enum_matching(
                merge_request_action, MergeRequestAction.list(), "merge_request_action"
            )
        if modified_by is not SENTINEL:
            self.modified_by = modified_by
        if modified_date is not SENTINEL:
            self.modified_date = modified_date
        if note is not SENTINEL:
            self.note = note
        if previous_stage is not SENTINEL:
            self.previous_stage = self._enum_matching(
                previous_stage, PreviousStage.list(), "previous_stage"
            )
        if priority_branch is not SENTINEL:
            self.priority_branch = self._enum_matching(
                priority_branch, PriorityBranch.list(), "priority_branch"
            )
        if source_branch_id is not SENTINEL:
            self.source_branch_id = source_branch_id
        if source_branch_name is not SENTINEL:
            self.source_branch_name = source_branch_name
        if stage is not SENTINEL:
            self.stage = self._enum_matching(stage, MergeRequestStage.list(), "stage")
        if strategy is not SENTINEL:
            self.strategy = self._enum_matching(strategy, Strategy.list(), "strategy")
        self._kwargs = kwargs
