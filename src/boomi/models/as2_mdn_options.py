
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .private_certificate import PrivateCertificate
from .public_certificate import PublicCertificate


class MdnDigestAlg(Enum):
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
        return list(map(lambda x: x.value, MdnDigestAlg._member_map_.values()))


class Synchronous(Enum):
    """An enumeration representing different categories.

    :cvar SYNC: "sync"
    :vartype SYNC: str
    :cvar ASYNC: "async"
    :vartype ASYNC: str
    """

    SYNC = "sync"
    ASYNC = "async"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Synchronous._member_map_.values()))


@JsonMap(
    {
        "external_url": "externalURL",
        "mdn_client_ssl_cert": "mdnClientSSLCert",
        "mdn_digest_alg": "mdnDigestAlg",
        "mdn_ssl_cert": "mdnSSLCert",
        "request_mdn": "requestMDN",
        "use_external_url": "useExternalURL",
        "use_ssl": "useSSL",
    }
)
class As2MdnOptions(BaseModel):
    """As2MdnOptions

    :param external_url: external_url
    :type external_url: str
    :param mdn_client_ssl_cert: mdn_client_ssl_cert
    :type mdn_client_ssl_cert: PrivateCertificate
    :param mdn_digest_alg: mdn_digest_alg, defaults to None
    :type mdn_digest_alg: MdnDigestAlg, optional
    :param mdn_ssl_cert: mdn_ssl_cert
    :type mdn_ssl_cert: PublicCertificate
    :param request_mdn: request_mdn, defaults to None
    :type request_mdn: bool, optional
    :param signed: signed, defaults to None
    :type signed: bool, optional
    :param synchronous: synchronous, defaults to None
    :type synchronous: Synchronous, optional
    :param use_external_url: use_external_url, defaults to None
    :type use_external_url: bool, optional
    :param use_ssl: use_ssl, defaults to None
    :type use_ssl: bool, optional
    """

    def __init__(
        self,
        external_url: str,
        mdn_client_ssl_cert: PrivateCertificate,
        mdn_ssl_cert: PublicCertificate,
        mdn_digest_alg: MdnDigestAlg = SENTINEL,
        request_mdn: bool = SENTINEL,
        signed: bool = SENTINEL,
        synchronous: Synchronous = SENTINEL,
        use_external_url: bool = SENTINEL,
        use_ssl: bool = SENTINEL,
        **kwargs,
    ):
        """As2MdnOptions

        :param external_url: external_url
        :type external_url: str
        :param mdn_client_ssl_cert: mdn_client_ssl_cert
        :type mdn_client_ssl_cert: PrivateCertificate
        :param mdn_digest_alg: mdn_digest_alg, defaults to None
        :type mdn_digest_alg: MdnDigestAlg, optional
        :param mdn_ssl_cert: mdn_ssl_cert
        :type mdn_ssl_cert: PublicCertificate
        :param request_mdn: request_mdn, defaults to None
        :type request_mdn: bool, optional
        :param signed: signed, defaults to None
        :type signed: bool, optional
        :param synchronous: synchronous, defaults to None
        :type synchronous: Synchronous, optional
        :param use_external_url: use_external_url, defaults to None
        :type use_external_url: bool, optional
        :param use_ssl: use_ssl, defaults to None
        :type use_ssl: bool, optional
        """
        self.external_url = external_url
        self.mdn_client_ssl_cert = self._define_object(
            mdn_client_ssl_cert, PrivateCertificate
        )
        if mdn_digest_alg is not SENTINEL:
            self.mdn_digest_alg = self._enum_matching(
                mdn_digest_alg, MdnDigestAlg.list(), "mdn_digest_alg"
            )
        self.mdn_ssl_cert = self._define_object(mdn_ssl_cert, PublicCertificate)
        if request_mdn is not SENTINEL:
            self.request_mdn = request_mdn
        if signed is not SENTINEL:
            self.signed = signed
        if synchronous is not SENTINEL:
            self.synchronous = self._enum_matching(
                synchronous, Synchronous.list(), "synchronous"
            )
        if use_external_url is not SENTINEL:
            self.use_external_url = use_external_url
        if use_ssl is not SENTINEL:
            self.use_ssl = use_ssl
        self._kwargs = kwargs
