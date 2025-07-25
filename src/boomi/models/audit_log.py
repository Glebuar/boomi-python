
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .audit_log_property import AuditLogProperty


@JsonMap(
    {
        "audit_log_property": "AuditLogProperty",
        "account_id": "accountId",
        "container_id": "containerId",
        "date_": "date",
        "document_id": "documentId",
        "type_": "type",
        "user_id": "userId",
    }
)
class AuditLog(BaseModel):
    """AuditLog

    :param audit_log_property: audit_log_property, defaults to None
    :type audit_log_property: List[AuditLogProperty], optional
    :param account_id: The account in which the action occurred., defaults to None
    :type account_id: str, optional
    :param action: The action type., defaults to None
    :type action: str, optional
    :param container_id: The ID of the Runtime, Runtime cluster, or Runtime cloud on which the action occurred., defaults to None
    :type container_id: str, optional
    :param date_: The date and time the action occurred., defaults to None
    :type date_: str, optional
    :param document_id: The ID assigned to the Audit Log record., defaults to None
    :type document_id: str, optional
    :param level: The severity level of the action: DEBUG, ERROR, INFO, or WARNING., defaults to None
    :type level: str, optional
    :param message: A descriptive message. Not all types of management actions have a message in their audit log entries., defaults to None
    :type message: str, optional
    :param modifier: The action type qualifier., defaults to None
    :type modifier: str, optional
    :param source: Where the action occurred: API, INTERNAL, MOBILE, UI, or UNKNOWN, defaults to None
    :type source: str, optional
    :param type_: The type of object on which the action occurred., defaults to None
    :type type_: str, optional
    :param user_id: The ID \(email address\) of the user who performed the action., defaults to None
    :type user_id: str, optional
    """

    def __init__(
        self,
        audit_log_property: List[AuditLogProperty] = SENTINEL,
        account_id: str = SENTINEL,
        action: str = SENTINEL,
        container_id: str = SENTINEL,
        date_: str = SENTINEL,
        document_id: str = SENTINEL,
        level: str = SENTINEL,
        message: str = SENTINEL,
        modifier: str = SENTINEL,
        source: str = SENTINEL,
        type_: str = SENTINEL,
        user_id: str = SENTINEL,
        **kwargs,
    ):
        """AuditLog

        :param audit_log_property: audit_log_property, defaults to None
        :type audit_log_property: List[AuditLogProperty], optional
        :param account_id: The account in which the action occurred., defaults to None
        :type account_id: str, optional
        :param action: The action type., defaults to None
        :type action: str, optional
        :param container_id: The ID of the Runtime, Runtime cluster, or Runtime cloud on which the action occurred., defaults to None
        :type container_id: str, optional
        :param date_: The date and time the action occurred., defaults to None
        :type date_: str, optional
        :param document_id: The ID assigned to the Audit Log record., defaults to None
        :type document_id: str, optional
        :param level: The severity level of the action: DEBUG, ERROR, INFO, or WARNING., defaults to None
        :type level: str, optional
        :param message: A descriptive message. Not all types of management actions have a message in their audit log entries., defaults to None
        :type message: str, optional
        :param modifier: The action type qualifier., defaults to None
        :type modifier: str, optional
        :param source: Where the action occurred: API, INTERNAL, MOBILE, UI, or UNKNOWN, defaults to None
        :type source: str, optional
        :param type_: The type of object on which the action occurred., defaults to None
        :type type_: str, optional
        :param user_id: The ID \(email address\) of the user who performed the action., defaults to None
        :type user_id: str, optional
        """
        if audit_log_property is not SENTINEL:
            self.audit_log_property = self._define_list(
                audit_log_property, AuditLogProperty
            )
        if account_id is not SENTINEL:
            self.account_id = account_id
        if action is not SENTINEL:
            self.action = action
        if container_id is not SENTINEL:
            self.container_id = container_id
        if date_ is not SENTINEL:
            self.date_ = date_
        if document_id is not SENTINEL:
            self.document_id = document_id
        if level is not SENTINEL:
            self.level = level
        if message is not SENTINEL:
            self.message = message
        if modifier is not SENTINEL:
            self.modifier = modifier
        if source is not SENTINEL:
            self.source = source
        if type_ is not SENTINEL:
            self.type_ = type_
        if user_id is not SENTINEL:
            self.user_id = user_id
        self._kwargs = kwargs
