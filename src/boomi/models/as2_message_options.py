
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class AttachmentOption(Enum):
    """An enumeration representing different categories.

    :cvar BATCH: "BATCH"
    :vartype BATCH: str
    :cvar DOCUMENTCACHE: "DOCUMENT_CACHE"
    :vartype DOCUMENTCACHE: str
    """

    BATCH = "BATCH"
    DOCUMENTCACHE = "DOCUMENT_CACHE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AttachmentOption._member_map_.values()))


class DataContentType(Enum):
    """An enumeration representing different categories.

    :cvar TEXTPLAIN: "textplain"
    :vartype TEXTPLAIN: str
    :cvar BINARY: "binary"
    :vartype BINARY: str
    :cvar EDIFACT: "edifact"
    :vartype EDIFACT: str
    :cvar EDIX12: "edix12"
    :vartype EDIX12: str
    :cvar APPLICATIONXML: "applicationxml"
    :vartype APPLICATIONXML: str
    :cvar TEXTXML: "textxml"
    :vartype TEXTXML: str
    """

    TEXTPLAIN = "textplain"
    BINARY = "binary"
    EDIFACT = "edifact"
    EDIX12 = "edix12"
    APPLICATIONXML = "applicationxml"
    TEXTXML = "textxml"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DataContentType._member_map_.values()))


class As2MessageOptionsEncryptionAlgorithm(Enum):
    """An enumeration representing different categories.

    :cvar NA: "na"
    :vartype NA: str
    :cvar TRIPLEDES: "tripledes"
    :vartype TRIPLEDES: str
    :cvar DES: "des"
    :vartype DES: str
    :cvar RC2_128: "rc2-128"
    :vartype RC2_128: str
    :cvar RC2_64: "rc2-64"
    :vartype RC2_64: str
    :cvar RC2_40: "rc2-40"
    :vartype RC2_40: str
    :cvar AES128: "aes-128"
    :vartype AES128: str
    :cvar AES192: "aes-192"
    :vartype AES192: str
    :cvar AES256: "aes-256"
    :vartype AES256: str
    """

    NA = "na"
    TRIPLEDES = "tripledes"
    DES = "des"
    RC2_128 = "rc2-128"
    RC2_64 = "rc2-64"
    RC2_40 = "rc2-40"
    AES128 = "aes-128"
    AES192 = "aes-192"
    AES256 = "aes-256"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                As2MessageOptionsEncryptionAlgorithm._member_map_.values(),
            )
        )


class SigningDigestAlg(Enum):
    """An enumeration representing different categories.

    :cvar SHA1: "SHA1"
    :vartype SHA1: str
    :cvar SHA224: "SHA224"
    :vartype SHA224: str
    :cvar SHA256: "SHA256"
    :vartype SHA256: str
    :cvar SHA384: "SHA384"
    :vartype SHA384: str
    :cvar SHA512: "SHA512"
    :vartype SHA512: str
    """

    SHA1 = "SHA1"
    SHA224 = "SHA224"
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SigningDigestAlg._member_map_.values()))


@JsonMap(
    {
        "attachment_cache": "attachmentCache",
        "attachment_option": "attachmentOption",
        "data_content_type": "dataContentType",
        "encryption_algorithm": "encryptionAlgorithm",
        "max_document_count": "maxDocumentCount",
        "multiple_attachments": "multipleAttachments",
        "signing_digest_alg": "signingDigestAlg",
    }
)
class As2MessageOptions(BaseModel):
    """As2MessageOptions

    :param attachment_cache: attachment_cache, defaults to None
    :type attachment_cache: str, optional
    :param attachment_option: attachment_option, defaults to None
    :type attachment_option: AttachmentOption, optional
    :param compressed: compressed, defaults to None
    :type compressed: bool, optional
    :param data_content_type: data_content_type, defaults to None
    :type data_content_type: DataContentType, optional
    :param encrypted: encrypted, defaults to None
    :type encrypted: bool, optional
    :param encryption_algorithm: encryption_algorithm, defaults to None
    :type encryption_algorithm: As2MessageOptionsEncryptionAlgorithm, optional
    :param max_document_count: max_document_count, defaults to None
    :type max_document_count: int, optional
    :param multiple_attachments: multiple_attachments, defaults to None
    :type multiple_attachments: bool, optional
    :param signed: signed, defaults to None
    :type signed: bool, optional
    :param signing_digest_alg: signing_digest_alg, defaults to None
    :type signing_digest_alg: SigningDigestAlg, optional
    :param subject: subject
    :type subject: str
    """

    def __init__(
        self,
        subject: str,
        attachment_cache: str = SENTINEL,
        attachment_option: AttachmentOption = SENTINEL,
        compressed: bool = SENTINEL,
        data_content_type: DataContentType = SENTINEL,
        encrypted: bool = SENTINEL,
        encryption_algorithm: As2MessageOptionsEncryptionAlgorithm = SENTINEL,
        max_document_count: int = SENTINEL,
        multiple_attachments: bool = SENTINEL,
        signed: bool = SENTINEL,
        signing_digest_alg: SigningDigestAlg = SENTINEL,
        **kwargs
    ):
        """As2MessageOptions

        :param attachment_cache: attachment_cache, defaults to None
        :type attachment_cache: str, optional
        :param attachment_option: attachment_option, defaults to None
        :type attachment_option: AttachmentOption, optional
        :param compressed: compressed, defaults to None
        :type compressed: bool, optional
        :param data_content_type: data_content_type, defaults to None
        :type data_content_type: DataContentType, optional
        :param encrypted: encrypted, defaults to None
        :type encrypted: bool, optional
        :param encryption_algorithm: encryption_algorithm, defaults to None
        :type encryption_algorithm: As2MessageOptionsEncryptionAlgorithm, optional
        :param max_document_count: max_document_count, defaults to None
        :type max_document_count: int, optional
        :param multiple_attachments: multiple_attachments, defaults to None
        :type multiple_attachments: bool, optional
        :param signed: signed, defaults to None
        :type signed: bool, optional
        :param signing_digest_alg: signing_digest_alg, defaults to None
        :type signing_digest_alg: SigningDigestAlg, optional
        :param subject: subject
        :type subject: str
        """
        if attachment_cache is not SENTINEL:
            self.attachment_cache = attachment_cache
        if attachment_option is not SENTINEL:
            self.attachment_option = self._enum_matching(
                attachment_option, AttachmentOption.list(), "attachment_option"
            )
        if compressed is not SENTINEL:
            self.compressed = compressed
        if data_content_type is not SENTINEL:
            self.data_content_type = self._enum_matching(
                data_content_type, DataContentType.list(), "data_content_type"
            )
        if encrypted is not SENTINEL:
            self.encrypted = encrypted
        if encryption_algorithm is not SENTINEL:
            self.encryption_algorithm = self._enum_matching(
                encryption_algorithm,
                As2MessageOptionsEncryptionAlgorithm.list(),
                "encryption_algorithm",
            )
        if max_document_count is not SENTINEL:
            self.max_document_count = max_document_count
        if multiple_attachments is not SENTINEL:
            self.multiple_attachments = multiple_attachments
        if signed is not SENTINEL:
            self.signed = signed
        if signing_digest_alg is not SENTINEL:
            self.signing_digest_alg = self._enum_matching(
                signing_digest_alg, SigningDigestAlg.list(), "signing_digest_alg"
            )
        self.subject = subject
        self._kwargs = kwargs
