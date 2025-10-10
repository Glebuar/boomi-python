
from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .nodes import Nodes


class Capabilities(Enum):
    """An enumeration representing different categories.

    :cvar GATEWAY: "GATEWAY"
    :vartype GATEWAY: str
    :cvar BROKER: "BROKER"
    :vartype BROKER: str
    """

    GATEWAY = "GATEWAY"
    BROKER = "BROKER"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Capabilities._member_map_.values()))


class AtomStatus(Enum):
    """An enumeration representing different categories.

    :cvar UNKNOWN: "UNKNOWN"
    :vartype UNKNOWN: str
    :cvar ONLINE: "ONLINE"
    :vartype ONLINE: str
    :cvar WARNING: "WARNING"
    :vartype WARNING: str
    :cvar OFFLINE: "OFFLINE"
    :vartype OFFLINE: str
    """

    UNKNOWN = "UNKNOWN"
    ONLINE = "ONLINE"
    WARNING = "WARNING"
    OFFLINE = "OFFLINE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AtomStatus._member_map_.values()))


class AtomType(Enum):
    """An enumeration representing different categories.

    :cvar CLOUD: "CLOUD"
    :vartype CLOUD: str
    :cvar MOLECULE: "MOLECULE"
    :vartype MOLECULE: str
    :cvar ATOM: "ATOM"
    :vartype ATOM: str
    """

    CLOUD = "CLOUD"
    MOLECULE = "MOLECULE"
    ATOM = "ATOM"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AtomType._member_map_.values()))


@JsonMap(
    {
        "cloud_id": "cloudId",
        "cloud_molecule_id": "cloudMoleculeId",
        "cloud_molecule_name": "cloudMoleculeName",
        "cloud_name": "cloudName",
        "cloud_owner_name": "cloudOwnerName",
        "created_by": "createdBy",
        "current_version": "currentVersion",
        "date_installed": "dateInstalled",
        "force_restart_time": "forceRestartTime",
        "host_name": "hostName",
        "id_": "id",
        "instance_id": "instanceId",
        "is_cloud_attachment": "isCloudAttachment",
        "purge_history_days": "purgeHistoryDays",
        "purge_immediate": "purgeImmediate",
        "type_": "type",
        "status_detail": "statusDetail",
    }
)
class Atom(BaseModel):
    """Atom

    :param capabilities: capabilities, defaults to None
    :type capabilities: List[Capabilities], optional
    :param cloud_id: \(For Runtimes attached to Runtime clouds\) A unique ID assigned by the system to the Runtime cloud., defaults to None
    :type cloud_id: str, optional
    :param cloud_molecule_id: ID of the Runtime cloud cluster to which the Cloud Attachment is assigned. This field is populated only for Cloud Attachments., defaults to None
    :type cloud_molecule_id: str, optional
    :param cloud_molecule_name: The name of the Runtime cloud cluster to which the Cloud Attachment is assigned. This field is populated only for Cloud Attachments., defaults to None
    :type cloud_molecule_name: str, optional
    :param cloud_name: The name of the associated Runtime cloud. This field is populated only for Cloud Attachments and Cloud runtime clusters., defaults to None
    :type cloud_name: str, optional
    :param cloud_owner_name: The account name of the associated Runtime cloud’s owner., defaults to None
    :type cloud_owner_name: str, optional
    :param cluster: cluster, defaults to None
    :type cluster: Nodes, optional
    :param created_by: The user ID (email address) of a user who created the Runtime., defaults to None
    :type created_by: str, optional
    :param current_version: A string that identifies the Runtime, Runtime cluster, or Runtime cloud's latest build., defaults to None
    :type current_version: str, optional
    :param date_installed: The installation date and time of the Runtime, Runtime cluster, or Runtime cloud. For Runtimes attached to a Runtime cloud, this is the installation date and time of the Runtime cloud., defaults to None
    :type date_installed: str, optional
    :param force_restart_time: The length of time, in milliseconds, that the platform waits before it forces the Runtime \(or Runtime cluster or Runtime cloud\) to restart after changes to the Atom’s configuration. Changes do not take effect until a restart occurs. However, regardless of this value, in a Runtime cluster or Runtime cloud that uses forked execution, automatic restart is deferred until currently running processes are complete., defaults to None
    :type force_restart_time: int, optional
    :param host_name: The name or IP address of the installation machine for the Runtime, Runtime cluster, or Runtime cloud. If the Runtime is attached to a Runtime cloud, the name of the Runtime cloud appears., defaults to None
    :type host_name: str, optional
    :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud., defaults to None
    :type id_: str, optional
    :param instance_id: \(For Runtimes attached to Runtime clouds\) A unique ID for the Runtime. The ID consists of the owning account ID followed by a period and a suffix., defaults to None
    :type instance_id: str, optional
    :param is_cloud_attachment: Indicates if a Runtime is a Cloud Attachment. It is set to `True` for the Cloud Attachment; otherwise, it is False for other Runtime. It is only populated for Cloud Attachments and Cloud runtime clusters., defaults to None
    :type is_cloud_attachment: bool, optional
    :param name: A user-defined name for the Runtime, Runtime cluster, or Runtime cloud., defaults to None
    :type name: str, optional
    :param purge_history_days: The number of days after a process run when the purging of logs, processed documents, and temporary data occurs. The default is 30 days. The maximum is 9999. A value of 0 disables purging., defaults to None
    :type purge_history_days: int, optional
    :param purge_immediate: If true, purges processed documents and temporary data immediately after a process ends. If you set this to true, also set purgeHistoryDays to a value greater than 0, such as 1. This combination not only purges your data right away, but also runs an extra cleanup process on a daily basis., defaults to None
    :type purge_immediate: bool, optional
    :param status: The status of the Runtime. Possible values are: UNKNOWN, ONLINE, WARNING, OFFLINE, defaults to None
    :type status: AtomStatus, optional
    :param type_: The type of Runtime. Possible values are: Cloud, Molecule, Atom, defaults to None
    :type type_: AtomType, optional
    :param status_detail: Provides more granular status details for the runtime. \<details\> \<summary\>Possible values:\</summary\>   When the runtime status is ONLINE:   - ONLINE_RUNNING   - ONLINE_STOPPING   - ONLINE_STARTING   - CLUSTER_ISSUE   - RESTARTING   - RESTARTING_TOO_LONG   - RESTARTING_DEAD   When the runtime status is OFFLINE:   - OFFLINE   - OFFLINE_NOT_STOPPED   - OFFLINE_NOT_INITIALIZED   - OFFLINE_WITH_ERROR   - OFFLINE_WITH_CLUSTER_ISSUE   - DELETED   - OFFBOARDING   When the runtime status is WARNING: CLUSTER_ISSUE   When the runtime status is UNKNOWN: UNKNOWN   \</details\>, defaults to None
    :type status_detail: str, optional
    """

    def __init__(
        self,
        capabilities: List[Capabilities] = SENTINEL,
        cloud_id: str = SENTINEL,
        cloud_molecule_id: str = SENTINEL,
        cloud_molecule_name: str = SENTINEL,
        cloud_name: str = SENTINEL,
        cloud_owner_name: str = SENTINEL,
        cluster: Nodes = SENTINEL,
        created_by: str = SENTINEL,
        current_version: str = SENTINEL,
        date_installed: str = SENTINEL,
        force_restart_time: int = SENTINEL,
        host_name: str = SENTINEL,
        id_: str = SENTINEL,
        instance_id: str = SENTINEL,
        is_cloud_attachment: bool = SENTINEL,
        name: str = SENTINEL,
        purge_history_days: int = SENTINEL,
        purge_immediate: bool = SENTINEL,
        status: AtomStatus = SENTINEL,
        type_: AtomType = SENTINEL,
        status_detail: str = SENTINEL,
        **kwargs,
    ):
        """Atom

        :param capabilities: capabilities, defaults to None
        :type capabilities: List[Capabilities], optional
        :param cloud_id: \(For Runtimes attached to Runtime clouds\) A unique ID assigned by the system to the Runtime cloud., defaults to None
        :type cloud_id: str, optional
        :param cloud_molecule_id: ID of the Runtime cloud cluster to which the Cloud Attachment is assigned. This field is populated only for Cloud Attachments., defaults to None
        :type cloud_molecule_id: str, optional
        :param cloud_molecule_name: The name of the Runtime cloud cluster to which the Cloud Attachment is assigned. This field is populated only for Cloud Attachments., defaults to None
        :type cloud_molecule_name: str, optional
        :param cloud_name: The name of the associated Runtime cloud. This field is populated only for Cloud Attachments and Cloud runtime clusters., defaults to None
        :type cloud_name: str, optional
        :param cloud_owner_name: The account name of the associated Runtime cloud’s owner., defaults to None
        :type cloud_owner_name: str, optional
        :param cluster: cluster, defaults to None
        :type cluster: Nodes, optional
        :param created_by: The user ID (email address) of a user who created the Runtime., defaults to None
        :type created_by: str, optional
        :param current_version: A string that identifies the Runtime, Runtime cluster, or Runtime cloud's latest build., defaults to None
        :type current_version: str, optional
        :param date_installed: The installation date and time of the Runtime, Runtime cluster, or Runtime cloud. For Runtimes attached to a Runtime cloud, this is the installation date and time of the Runtime cloud., defaults to None
        :type date_installed: str, optional
        :param force_restart_time: The length of time, in milliseconds, that the platform waits before it forces the Runtime \(or Runtime cluster or Runtime cloud\) to restart after changes to the Atom’s configuration. Changes do not take effect until a restart occurs. However, regardless of this value, in a Runtime cluster or Runtime cloud that uses forked execution, automatic restart is deferred until currently running processes are complete., defaults to None
        :type force_restart_time: int, optional
        :param host_name: The name or IP address of the installation machine for the Runtime, Runtime cluster, or Runtime cloud. If the Runtime is attached to a Runtime cloud, the name of the Runtime cloud appears., defaults to None
        :type host_name: str, optional
        :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud., defaults to None
        :type id_: str, optional
        :param instance_id: \(For Runtimes attached to Runtime clouds\) A unique ID for the Runtime. The ID consists of the owning account ID followed by a period and a suffix., defaults to None
        :type instance_id: str, optional
        :param is_cloud_attachment: Indicates if a Runtime is a Cloud Attachment. It is set to `True` for the Cloud Attachment; otherwise, it is False for other Runtime. It is only populated for Cloud Attachments and Cloud runtime clusters., defaults to None
        :type is_cloud_attachment: bool, optional
        :param name: A user-defined name for the Runtime, Runtime cluster, or Runtime cloud., defaults to None
        :type name: str, optional
        :param purge_history_days: The number of days after a process run when the purging of logs, processed documents, and temporary data occurs. The default is 30 days. The maximum is 9999. A value of 0 disables purging., defaults to None
        :type purge_history_days: int, optional
        :param purge_immediate: If true, purges processed documents and temporary data immediately after a process ends. If you set this to true, also set purgeHistoryDays to a value greater than 0, such as 1. This combination not only purges your data right away, but also runs an extra cleanup process on a daily basis., defaults to None
        :type purge_immediate: bool, optional
        :param status: The status of the Runtime. Possible values are: UNKNOWN, ONLINE, WARNING, OFFLINE, defaults to None
        :type status: AtomStatus, optional
        :param type_: The type of Runtime. Possible values are: Cloud, Molecule, Atom, defaults to None
        :type type_: AtomType, optional
        :param status_detail: Provides more granular status details for the runtime. \<details\> \<summary\>Possible values:\</summary\>   When the runtime status is ONLINE:   - ONLINE_RUNNING   - ONLINE_STOPPING   - ONLINE_STARTING   - CLUSTER_ISSUE   - RESTARTING   - RESTARTING_TOO_LONG   - RESTARTING_DEAD   When the runtime status is OFFLINE:   - OFFLINE   - OFFLINE_NOT_STOPPED   - OFFLINE_NOT_INITIALIZED   - OFFLINE_WITH_ERROR   - OFFLINE_WITH_CLUSTER_ISSUE   - DELETED   - OFFBOARDING   When the runtime status is WARNING: CLUSTER_ISSUE   When the runtime status is UNKNOWN: UNKNOWN   \</details\>, defaults to None
        :type status_detail: str, optional
        """
        if capabilities is not SENTINEL:
            self.capabilities = self._define_list(capabilities, Capabilities)
        if cloud_id is not SENTINEL:
            self.cloud_id = cloud_id
        if cloud_molecule_id is not SENTINEL:
            self.cloud_molecule_id = cloud_molecule_id
        if cloud_molecule_name is not SENTINEL:
            self.cloud_molecule_name = cloud_molecule_name
        if cloud_name is not SENTINEL:
            self.cloud_name = cloud_name
        if cloud_owner_name is not SENTINEL:
            self.cloud_owner_name = cloud_owner_name
        if cluster is not SENTINEL:
            self.cluster = self._define_object(cluster, Nodes)
        if created_by is not SENTINEL:
            self.created_by = created_by
        if current_version is not SENTINEL:
            self.current_version = current_version
        if date_installed is not SENTINEL:
            self.date_installed = date_installed
        if force_restart_time is not SENTINEL:
            self.force_restart_time = force_restart_time
        if host_name is not SENTINEL:
            self.host_name = host_name
        if id_ is not SENTINEL:
            self.id_ = id_
        if instance_id is not SENTINEL:
            self.instance_id = instance_id
        if is_cloud_attachment is not SENTINEL:
            self.is_cloud_attachment = is_cloud_attachment
        if name is not SENTINEL:
            self.name = name
        if purge_history_days is not SENTINEL:
            self.purge_history_days = purge_history_days
        if purge_immediate is not SENTINEL:
            self.purge_immediate = purge_immediate
        if status is not SENTINEL:
            self.status = self._enum_matching(status, AtomStatus.list(), "status")
        if type_ is not SENTINEL:
            self.type_ = self._enum_matching(type_, AtomType.list(), "type_")
        if status_detail is not SENTINEL:
            self.status_detail = status_detail
        self._kwargs = kwargs
