
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class AttachmentContentType(Enum):
    """An enumeration representing different categories.

    :cvar APPLICATIONXML: "application/xml"
    :vartype APPLICATIONXML: str
    :cvar APPLICATIONPDF: "application/pdf"
    :vartype APPLICATIONPDF: str
    :cvar APPLICATIONMSWORD: "application/msword"
    :vartype APPLICATIONMSWORD: str
    :cvar IMAGETIFF: "image/tiff"
    :vartype IMAGETIFF: str
    :cvar IMAGEJPEG: "image/jpeg"
    :vartype IMAGEJPEG: str
    :cvar TEXTPLAIN: "text/plain"
    :vartype TEXTPLAIN: str
    """

    APPLICATIONXML = "application/xml"
    APPLICATIONPDF = "application/pdf"
    APPLICATIONMSWORD = "application/msword"
    IMAGETIFF = "image/tiff"
    IMAGEJPEG = "image/jpeg"
    TEXTPLAIN = "text/plain"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AttachmentContentType._member_map_.values()))


@JsonMap(
    {
        "attachment_cache": "attachmentCache",
        "attachment_content_type": "attachmentContentType",
        "multiple_attachments": "multipleAttachments",
    }
)
class AttachmentInfo(BaseModel):
    """AttachmentInfo

    :param attachment_cache: attachment_cache, defaults to None
    :type attachment_cache: str, optional
    :param attachment_content_type: attachment_content_type, defaults to None
    :type attachment_content_type: List[AttachmentContentType], optional
    :param multiple_attachments: multiple_attachments, defaults to None
    :type multiple_attachments: bool, optional
    """

    def __init__(
        self,
        attachment_cache: str = SENTINEL,
        attachment_content_type: List[AttachmentContentType] = SENTINEL,
        multiple_attachments: bool = SENTINEL,
        **kwargs
    ):
        """AttachmentInfo

        :param attachment_cache: attachment_cache, defaults to None
        :type attachment_cache: str, optional
        :param attachment_content_type: attachment_content_type, defaults to None
        :type attachment_content_type: List[AttachmentContentType], optional
        :param multiple_attachments: multiple_attachments, defaults to None
        :type multiple_attachments: bool, optional
        """
        if attachment_cache is not SENTINEL:
            self.attachment_cache = attachment_cache
        if attachment_content_type is not SENTINEL:
            self.attachment_content_type = self._define_list(
                attachment_content_type, AttachmentContentType
            )
        if multiple_attachments is not SENTINEL:
            self.multiple_attachments = multiple_attachments
        self._kwargs = kwargs
