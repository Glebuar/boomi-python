
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ContentTransferEncoding(Enum):
    """An enumeration representing different categories.

    :cvar BINARY: "binary"
    :vartype BINARY: str
    :cvar BASE64: "base64"
    :vartype BASE64: str
    """

    BINARY = "binary"
    BASE64 = "base64"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ContentTransferEncoding._member_map_.values())
        )


class RosettaNetMessageOptionsEncryptionAlgorithm(Enum):
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
                RosettaNetMessageOptionsEncryptionAlgorithm._member_map_.values(),
            )
        )


class SignatureDigestAlgorithm(Enum):
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
        return list(
            map(lambda x: x.value, SignatureDigestAlgorithm._member_map_.values())
        )


@JsonMap(
    {
        "attachment_cache": "attachmentCache",
        "content_transfer_encoding": "contentTransferEncoding",
        "encrypt_service_header": "encryptServiceHeader",
        "encryption_algorithm": "encryptionAlgorithm",
        "signature_digest_algorithm": "signatureDigestAlgorithm",
    }
)
class RosettaNetMessageOptions(BaseModel):
    """RosettaNetMessageOptions

    :param attachment_cache: attachment_cache, defaults to None
    :type attachment_cache: str, optional
    :param compressed: compressed, defaults to None
    :type compressed: bool, optional
    :param content_transfer_encoding: content_transfer_encoding, defaults to None
    :type content_transfer_encoding: ContentTransferEncoding, optional
    :param encrypt_service_header: encrypt_service_header, defaults to None
    :type encrypt_service_header: bool, optional
    :param encrypted: encrypted, defaults to None
    :type encrypted: bool, optional
    :param encryption_algorithm: encryption_algorithm, defaults to None
    :type encryption_algorithm: RosettaNetMessageOptionsEncryptionAlgorithm, optional
    :param signature_digest_algorithm: signature_digest_algorithm, defaults to None
    :type signature_digest_algorithm: SignatureDigestAlgorithm, optional
    :param signed: signed, defaults to None
    :type signed: bool, optional
    """

    def __init__(
        self,
        attachment_cache: str = SENTINEL,
        compressed: bool = SENTINEL,
        content_transfer_encoding: ContentTransferEncoding = SENTINEL,
        encrypt_service_header: bool = SENTINEL,
        encrypted: bool = SENTINEL,
        encryption_algorithm: RosettaNetMessageOptionsEncryptionAlgorithm = SENTINEL,
        signature_digest_algorithm: SignatureDigestAlgorithm = SENTINEL,
        signed: bool = SENTINEL,
        **kwargs
    ):
        """RosettaNetMessageOptions

        :param attachment_cache: attachment_cache, defaults to None
        :type attachment_cache: str, optional
        :param compressed: compressed, defaults to None
        :type compressed: bool, optional
        :param content_transfer_encoding: content_transfer_encoding, defaults to None
        :type content_transfer_encoding: ContentTransferEncoding, optional
        :param encrypt_service_header: encrypt_service_header, defaults to None
        :type encrypt_service_header: bool, optional
        :param encrypted: encrypted, defaults to None
        :type encrypted: bool, optional
        :param encryption_algorithm: encryption_algorithm, defaults to None
        :type encryption_algorithm: RosettaNetMessageOptionsEncryptionAlgorithm, optional
        :param signature_digest_algorithm: signature_digest_algorithm, defaults to None
        :type signature_digest_algorithm: SignatureDigestAlgorithm, optional
        :param signed: signed, defaults to None
        :type signed: bool, optional
        """
        if attachment_cache is not SENTINEL:
            self.attachment_cache = attachment_cache
        if compressed is not SENTINEL:
            self.compressed = compressed
        if content_transfer_encoding is not SENTINEL:
            self.content_transfer_encoding = self._enum_matching(
                content_transfer_encoding,
                ContentTransferEncoding.list(),
                "content_transfer_encoding",
            )
        if encrypt_service_header is not SENTINEL:
            self.encrypt_service_header = encrypt_service_header
        if encrypted is not SENTINEL:
            self.encrypted = encrypted
        if encryption_algorithm is not SENTINEL:
            self.encryption_algorithm = self._enum_matching(
                encryption_algorithm,
                RosettaNetMessageOptionsEncryptionAlgorithm.list(),
                "encryption_algorithm",
            )
        if signature_digest_algorithm is not SENTINEL:
            self.signature_digest_algorithm = self._enum_matching(
                signature_digest_algorithm,
                SignatureDigestAlgorithm.list(),
                "signature_digest_algorithm",
            )
        if signed is not SENTINEL:
            self.signed = signed
        self._kwargs = kwargs
