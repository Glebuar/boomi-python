
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .private_certificate import PrivateCertificate


@JsonMap(
    {
        "as2_id": "as2Id",
        "enabled_legacy_smime": "enabledLegacySMIME",
        "encryption_private_certificate": "encryptionPrivateCertificate",
        "mdn_signature_private_certificate": "mdnSignaturePrivateCertificate",
        "signing_private_certificate": "signingPrivateCertificate",
    }
)
class As2MyCompanyInfo(BaseModel):
    """As2MyCompanyInfo

    :param as2_id: as2_id
    :type as2_id: str
    :param enabled_legacy_smime: enabled_legacy_smime, defaults to None
    :type enabled_legacy_smime: bool, optional
    :param encryption_private_certificate: encryption_private_certificate
    :type encryption_private_certificate: PrivateCertificate
    :param mdn_signature_private_certificate: mdn_signature_private_certificate
    :type mdn_signature_private_certificate: PrivateCertificate
    :param signing_private_certificate: signing_private_certificate
    :type signing_private_certificate: PrivateCertificate
    """

    def __init__(
        self,
        as2_id: str,
        encryption_private_certificate: PrivateCertificate,
        mdn_signature_private_certificate: PrivateCertificate,
        signing_private_certificate: PrivateCertificate,
        enabled_legacy_smime: bool = SENTINEL,
        **kwargs,
    ):
        """As2MyCompanyInfo

        :param as2_id: as2_id
        :type as2_id: str
        :param enabled_legacy_smime: enabled_legacy_smime, defaults to None
        :type enabled_legacy_smime: bool, optional
        :param encryption_private_certificate: encryption_private_certificate
        :type encryption_private_certificate: PrivateCertificate
        :param mdn_signature_private_certificate: mdn_signature_private_certificate
        :type mdn_signature_private_certificate: PrivateCertificate
        :param signing_private_certificate: signing_private_certificate
        :type signing_private_certificate: PrivateCertificate
        """
        self.as2_id = as2_id
        if enabled_legacy_smime is not SENTINEL:
            self.enabled_legacy_smime = enabled_legacy_smime
        self.encryption_private_certificate = self._define_object(
            encryption_private_certificate, PrivateCertificate
        )
        self.mdn_signature_private_certificate = self._define_object(
            mdn_signature_private_certificate, PrivateCertificate
        )
        self.signing_private_certificate = self._define_object(
            signing_private_certificate, PrivateCertificate
        )
        self._kwargs = kwargs
