
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class FilterMatchType(Enum):
    """An enumeration representing different categories.

    :cvar WILDCARD: "wildcard"
    :vartype WILDCARD: str
    :cvar REGEX: "regex"
    :vartype REGEX: str
    """

    WILDCARD = "wildcard"
    REGEX = "regex"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, FilterMatchType._member_map_.values()))


@JsonMap(
    {
        "delete_after_read": "deleteAfterRead",
        "file_filter": "fileFilter",
        "filter_match_type": "filterMatchType",
        "get_directory": "getDirectory",
        "max_file_count": "maxFileCount",
        "use_default_get_options": "useDefaultGetOptions",
    }
)
class DiskGetOptions(BaseModel):
    """DiskGetOptions

    :param delete_after_read: delete_after_read, defaults to None
    :type delete_after_read: bool, optional
    :param file_filter: file_filter
    :type file_filter: str
    :param filter_match_type: filter_match_type, defaults to None
    :type filter_match_type: FilterMatchType, optional
    :param get_directory: get_directory
    :type get_directory: str
    :param max_file_count: max_file_count, defaults to None
    :type max_file_count: int, optional
    :param use_default_get_options: use_default_get_options, defaults to None
    :type use_default_get_options: bool, optional
    """

    def __init__(
        self,
        file_filter: str,
        get_directory: str,
        delete_after_read: bool = SENTINEL,
        filter_match_type: FilterMatchType = SENTINEL,
        max_file_count: int = SENTINEL,
        use_default_get_options: bool = SENTINEL,
        **kwargs
    ):
        """DiskGetOptions

        :param delete_after_read: delete_after_read, defaults to None
        :type delete_after_read: bool, optional
        :param file_filter: file_filter
        :type file_filter: str
        :param filter_match_type: filter_match_type, defaults to None
        :type filter_match_type: FilterMatchType, optional
        :param get_directory: get_directory
        :type get_directory: str
        :param max_file_count: max_file_count, defaults to None
        :type max_file_count: int, optional
        :param use_default_get_options: use_default_get_options, defaults to None
        :type use_default_get_options: bool, optional
        """
        if delete_after_read is not SENTINEL:
            self.delete_after_read = delete_after_read
        self.file_filter = file_filter
        if filter_match_type is not SENTINEL:
            self.filter_match_type = self._enum_matching(
                filter_match_type, FilterMatchType.list(), "filter_match_type"
            )
        self.get_directory = get_directory
        if max_file_count is not SENTINEL:
            self.max_file_count = max_file_count
        if use_default_get_options is not SENTINEL:
            self.use_default_get_options = use_default_get_options
        self._kwargs = kwargs
