
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .atom_disk_space_directory import AtomDiskSpaceDirectory


@JsonMap(
    {
        "disk_space_directory": "DiskSpaceDirectory",
        "quota_limit": "quotaLimit",
        "raw_quota_limit": "rawQuotaLimit",
        "raw_total_size": "rawTotalSize",
        "total_size": "totalSize",
    }
)
class AtomDiskSpace(BaseModel):
    """AtomDiskSpace

    :param disk_space_directory: disk_space_directory, defaults to None
    :type disk_space_directory: List[AtomDiskSpaceDirectory], optional
    :param quota_limit: The total amount of disk space available for consumption by this attachment., defaults to None
    :type quota_limit: str, optional
    :param raw_quota_limit: The total number of bytes available for consumption by this attachment., defaults to None
    :type raw_quota_limit: int, optional
    :param raw_total_size: The disk space in bytes that is already consumed by the given attachment., defaults to None
    :type raw_total_size: int, optional
    :param total_size: The size of disk space already consumed by the given attachment., defaults to None
    :type total_size: str, optional
    """

    def __init__(
        self,
        disk_space_directory: List[AtomDiskSpaceDirectory] = SENTINEL,
        quota_limit: str = SENTINEL,
        raw_quota_limit: int = SENTINEL,
        raw_total_size: int = SENTINEL,
        total_size: str = SENTINEL,
        **kwargs,
    ):
        """AtomDiskSpace

        :param disk_space_directory: disk_space_directory, defaults to None
        :type disk_space_directory: List[AtomDiskSpaceDirectory], optional
        :param quota_limit: The total amount of disk space available for consumption by this attachment., defaults to None
        :type quota_limit: str, optional
        :param raw_quota_limit: The total number of bytes available for consumption by this attachment., defaults to None
        :type raw_quota_limit: int, optional
        :param raw_total_size: The disk space in bytes that is already consumed by the given attachment., defaults to None
        :type raw_total_size: int, optional
        :param total_size: The size of disk space already consumed by the given attachment., defaults to None
        :type total_size: str, optional
        """
        if disk_space_directory is not SENTINEL:
            self.disk_space_directory = self._define_list(
                disk_space_directory, AtomDiskSpaceDirectory
            )
        if quota_limit is not SENTINEL:
            self.quota_limit = quota_limit
        if raw_quota_limit is not SENTINEL:
            self.raw_quota_limit = raw_quota_limit
        if raw_total_size is not SENTINEL:
            self.raw_total_size = raw_total_size
        if total_size is not SENTINEL:
            self.total_size = total_size
        self._kwargs = kwargs
