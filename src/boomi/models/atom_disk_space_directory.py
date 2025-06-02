
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"raw_size": "rawSize"})
class AtomDiskSpaceDirectory(BaseModel):
    """AtomDiskSpaceDirectory

    :param file: A specific directory within the attachment’s directory for which this size pertains., defaults to None
    :type file: str, optional
    :param raw_size: The disk space in bytes that is already consumed within the directory., defaults to None
    :type raw_size: int, optional
    :param size: The size of disk space consumed within this directory., defaults to None
    :type size: str, optional
    """

    def __init__(
        self,
        file: str = SENTINEL,
        raw_size: int = SENTINEL,
        size: str = SENTINEL,
        **kwargs
    ):
        """AtomDiskSpaceDirectory

        :param file: A specific directory within the attachment’s directory for which this size pertains., defaults to None
        :type file: str, optional
        :param raw_size: The disk space in bytes that is already consumed within the directory., defaults to None
        :type raw_size: int, optional
        :param size: The size of disk space consumed within this directory., defaults to None
        :type size: str, optional
        """
        if file is not SENTINEL:
            self.file = file
        if raw_size is not SENTINEL:
            self.raw_size = raw_size
        if size is not SENTINEL:
            self.size = size
        self._kwargs = kwargs
