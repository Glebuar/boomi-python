
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "client_ssl_alias": "clientSSLAlias",
        "encrypting_certificate": "encrypting-certificate",
        "session_challenge_certificate": "session-challenge-certificate",
        "sfidsec_encrypt": "sfidsec-encrypt",
        "sfidsec_sign": "sfidsec-sign",
        "verifying_eerp_certificate": "verifying-eerp-certificate",
        "verifying_signature_certificate": "verifying-signature-certificate",
    }
)
class OftpPartnerInfo(BaseModel):
    """OftpPartnerInfo

    :param client_ssl_alias: client_ssl_alias, defaults to None
    :type client_ssl_alias: str, optional
    :param encrypting_certificate: encrypting_certificate, defaults to None
    :type encrypting_certificate: str, optional
    :param session_challenge_certificate: session_challenge_certificate, defaults to None
    :type session_challenge_certificate: str, optional
    :param sfidsec_encrypt: sfidsec_encrypt, defaults to None
    :type sfidsec_encrypt: bool, optional
    :param sfidsec_sign: sfidsec_sign, defaults to None
    :type sfidsec_sign: bool, optional
    :param sfidsign: sfidsign, defaults to None
    :type sfidsign: bool, optional
    :param ssidcmpr: ssidcmpr, defaults to None
    :type ssidcmpr: bool, optional
    :param ssidcode: ssidcode, defaults to None
    :type ssidcode: str, optional
    :param ssidpswd: ssidpswd, defaults to None
    :type ssidpswd: str, optional
    :param verifying_eerp_certificate: verifying_eerp_certificate, defaults to None
    :type verifying_eerp_certificate: str, optional
    :param verifying_signature_certificate: verifying_signature_certificate, defaults to None
    :type verifying_signature_certificate: str, optional
    """

    def __init__(
        self,
        client_ssl_alias: str = SENTINEL,
        encrypting_certificate: str = SENTINEL,
        session_challenge_certificate: str = SENTINEL,
        sfidsec_encrypt: bool = SENTINEL,
        sfidsec_sign: bool = SENTINEL,
        sfidsign: bool = SENTINEL,
        ssidcmpr: bool = SENTINEL,
        ssidcode: str = SENTINEL,
        ssidpswd: str = SENTINEL,
        verifying_eerp_certificate: str = SENTINEL,
        verifying_signature_certificate: str = SENTINEL,
        **kwargs
    ):
        """OftpPartnerInfo

        :param client_ssl_alias: client_ssl_alias, defaults to None
        :type client_ssl_alias: str, optional
        :param encrypting_certificate: encrypting_certificate, defaults to None
        :type encrypting_certificate: str, optional
        :param session_challenge_certificate: session_challenge_certificate, defaults to None
        :type session_challenge_certificate: str, optional
        :param sfidsec_encrypt: sfidsec_encrypt, defaults to None
        :type sfidsec_encrypt: bool, optional
        :param sfidsec_sign: sfidsec_sign, defaults to None
        :type sfidsec_sign: bool, optional
        :param sfidsign: sfidsign, defaults to None
        :type sfidsign: bool, optional
        :param ssidcmpr: ssidcmpr, defaults to None
        :type ssidcmpr: bool, optional
        :param ssidcode: ssidcode, defaults to None
        :type ssidcode: str, optional
        :param ssidpswd: ssidpswd, defaults to None
        :type ssidpswd: str, optional
        :param verifying_eerp_certificate: verifying_eerp_certificate, defaults to None
        :type verifying_eerp_certificate: str, optional
        :param verifying_signature_certificate: verifying_signature_certificate, defaults to None
        :type verifying_signature_certificate: str, optional
        """
        if client_ssl_alias is not SENTINEL:
            self.client_ssl_alias = client_ssl_alias
        if encrypting_certificate is not SENTINEL:
            self.encrypting_certificate = encrypting_certificate
        if session_challenge_certificate is not SENTINEL:
            self.session_challenge_certificate = session_challenge_certificate
        if sfidsec_encrypt is not SENTINEL:
            self.sfidsec_encrypt = sfidsec_encrypt
        if sfidsec_sign is not SENTINEL:
            self.sfidsec_sign = sfidsec_sign
        if sfidsign is not SENTINEL:
            self.sfidsign = sfidsign
        if ssidcmpr is not SENTINEL:
            self.ssidcmpr = ssidcmpr
        if ssidcode is not SENTINEL:
            self.ssidcode = ssidcode
        if ssidpswd is not SENTINEL:
            self.ssidpswd = ssidpswd
        if verifying_eerp_certificate is not SENTINEL:
            self.verifying_eerp_certificate = verifying_eerp_certificate
        if verifying_signature_certificate is not SENTINEL:
            self.verifying_signature_certificate = verifying_signature_certificate
        self._kwargs = kwargs
