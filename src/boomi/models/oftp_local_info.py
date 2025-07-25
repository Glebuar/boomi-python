
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "decrypting_certificate": "decrypting-certificate",
        "session_authentication_certificate": "session-authentication-certificate",
        "signing_certificate": "signing-certificate",
        "signing_eerp_certificate": "signing-eerp-certificate",
    }
)
class OftpLocalInfo(BaseModel):
    """OftpLocalInfo

    :param decrypting_certificate: decrypting_certificate, defaults to None
    :type decrypting_certificate: str, optional
    :param session_authentication_certificate: session_authentication_certificate, defaults to None
    :type session_authentication_certificate: str, optional
    :param signing_certificate: signing_certificate, defaults to None
    :type signing_certificate: str, optional
    :param signing_eerp_certificate: signing_eerp_certificate, defaults to None
    :type signing_eerp_certificate: str, optional
    :param ssidcode: ssidcode, defaults to None
    :type ssidcode: str, optional
    :param ssidpswd: ssidpswd, defaults to None
    :type ssidpswd: str, optional
    """

    def __init__(
        self,
        decrypting_certificate: str = SENTINEL,
        session_authentication_certificate: str = SENTINEL,
        signing_certificate: str = SENTINEL,
        signing_eerp_certificate: str = SENTINEL,
        ssidcode: str = SENTINEL,
        ssidpswd: str = SENTINEL,
        **kwargs
    ):
        """OftpLocalInfo

        :param decrypting_certificate: decrypting_certificate, defaults to None
        :type decrypting_certificate: str, optional
        :param session_authentication_certificate: session_authentication_certificate, defaults to None
        :type session_authentication_certificate: str, optional
        :param signing_certificate: signing_certificate, defaults to None
        :type signing_certificate: str, optional
        :param signing_eerp_certificate: signing_eerp_certificate, defaults to None
        :type signing_eerp_certificate: str, optional
        :param ssidcode: ssidcode, defaults to None
        :type ssidcode: str, optional
        :param ssidpswd: ssidpswd, defaults to None
        :type ssidpswd: str, optional
        """
        if decrypting_certificate is not SENTINEL:
            self.decrypting_certificate = decrypting_certificate
        if session_authentication_certificate is not SENTINEL:
            self.session_authentication_certificate = session_authentication_certificate
        if signing_certificate is not SENTINEL:
            self.signing_certificate = signing_certificate
        if signing_eerp_certificate is not SENTINEL:
            self.signing_eerp_certificate = signing_eerp_certificate
        if ssidcode is not SENTINEL:
            self.ssidcode = ssidcode
        if ssidpswd is not SENTINEL:
            self.ssidpswd = ssidpswd
        self._kwargs = kwargs
