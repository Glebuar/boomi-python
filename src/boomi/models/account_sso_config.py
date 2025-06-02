
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "account_id": "accountId",
        "assertion_encryption": "assertionEncryption",
        "authn_context": "authnContext",
        "authn_context_comparison": "authnContextComparison",
        "cert_info": "certInfo",
        "fed_id_from_name_id": "fedIdFromNameId",
        "idp_url": "idpUrl",
        "name_id_policy": "nameIdPolicy",
        "signout_redirect_url": "signoutRedirectUrl",
    }
)
class AccountSsoConfig(BaseModel):
    """AccountSsoConfig

    :param account_id: The account ID., defaults to None
    :type account_id: str, optional
    :param assertion_encryption: assertion_encryption, defaults to None
    :type assertion_encryption: bool, optional
    :param authn_context: PPT - \(Default\) Password Protected Transport, requires a username and password for authentication\<br /\>UNSPECIFIED - Accepts any type of authentication, defaults to None
    :type authn_context: str, optional
    :param authn_context_comparison: EXACT - The resulting authentication context in the authentication statement must be the exact match to at least one of the specified authentication contexts.\<br /\>MINUMUM - The resulting authentication context in the authentication statement must be at least as strong \(as deemed by the responder\) as one of the specified authentication contexts., defaults to None
    :type authn_context_comparison: str, optional
    :param cert_info: Metadata for the public certificate of the identity provider., defaults to None
    :type cert_info: str, optional
    :param certificate: Base64-encoded certificate bytes for the identity provider., defaults to None
    :type certificate: List[str], optional
    :param enabled: *true* — Enables single sign-on for the account. \<br /\>   *false* — Disables single sign-on for the account., defaults to None
    :type enabled: bool, optional
    :param fed_id_from_name_id: *true* — The federation ID is in the NameID element of the Subject element in the SAML Response document.\<br /\> *false*— The federation ID is in the FEDERATION\_ID Attribute element in the SAML Response document., defaults to None
    :type fed_id_from_name_id: bool, optional
    :param idp_url: The URL of the identity provider's single sign-on service., defaults to None
    :type idp_url: str, optional
    :param name_id_policy: *TRANSIENT* — Indicates that the content of the element is a non-constant and temporary value that should not assume any standard meaning; the identifier confirms a user is granted access without revealing the user's actual name or identity\<br /\>*UNSPECIFIED* — Indicates that identity provider can interpret the NameID attribute; the identifier confirms a user is granted access and can reveal the user's real name or identity depending on how it is defined by identity provider.\<br /\>**Important:** Entering any value other than TRANSIENT or UNSPECIFIED for the nameIdPolicy results in an exception.\<br /\>As a service provider, does not interpret the NameID value; a user is identified by comparing the *NameID* value with the *Federation ID* value., defaults to None
    :type name_id_policy: str, optional
    :param signout_redirect_url: After signing out of the, the URL that redirects the user., defaults to None
    :type signout_redirect_url: str, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        assertion_encryption: bool = SENTINEL,
        authn_context: str = SENTINEL,
        authn_context_comparison: str = SENTINEL,
        cert_info: str = SENTINEL,
        certificate: List[str] = SENTINEL,
        enabled: bool = SENTINEL,
        fed_id_from_name_id: bool = SENTINEL,
        idp_url: str = SENTINEL,
        name_id_policy: str = SENTINEL,
        signout_redirect_url: str = SENTINEL,
        **kwargs
    ):
        """AccountSsoConfig

        :param account_id: The account ID., defaults to None
        :type account_id: str, optional
        :param assertion_encryption: assertion_encryption, defaults to None
        :type assertion_encryption: bool, optional
        :param authn_context: PPT - \(Default\) Password Protected Transport, requires a username and password for authentication\<br /\>UNSPECIFIED - Accepts any type of authentication, defaults to None
        :type authn_context: str, optional
        :param authn_context_comparison: EXACT - The resulting authentication context in the authentication statement must be the exact match to at least one of the specified authentication contexts.\<br /\>MINUMUM - The resulting authentication context in the authentication statement must be at least as strong \(as deemed by the responder\) as one of the specified authentication contexts., defaults to None
        :type authn_context_comparison: str, optional
        :param cert_info: Metadata for the public certificate of the identity provider., defaults to None
        :type cert_info: str, optional
        :param certificate: Base64-encoded certificate bytes for the identity provider., defaults to None
        :type certificate: List[str], optional
        :param enabled: *true* — Enables single sign-on for the account. \<br /\>   *false* — Disables single sign-on for the account., defaults to None
        :type enabled: bool, optional
        :param fed_id_from_name_id: *true* — The federation ID is in the NameID element of the Subject element in the SAML Response document.\<br /\> *false*— The federation ID is in the FEDERATION\_ID Attribute element in the SAML Response document., defaults to None
        :type fed_id_from_name_id: bool, optional
        :param idp_url: The URL of the identity provider's single sign-on service., defaults to None
        :type idp_url: str, optional
        :param name_id_policy: *TRANSIENT* — Indicates that the content of the element is a non-constant and temporary value that should not assume any standard meaning; the identifier confirms a user is granted access without revealing the user's actual name or identity\<br /\>*UNSPECIFIED* — Indicates that identity provider can interpret the NameID attribute; the identifier confirms a user is granted access and can reveal the user's real name or identity depending on how it is defined by identity provider.\<br /\>**Important:** Entering any value other than TRANSIENT or UNSPECIFIED for the nameIdPolicy results in an exception.\<br /\>As a service provider, does not interpret the NameID value; a user is identified by comparing the *NameID* value with the *Federation ID* value., defaults to None
        :type name_id_policy: str, optional
        :param signout_redirect_url: After signing out of the, the URL that redirects the user., defaults to None
        :type signout_redirect_url: str, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if assertion_encryption is not SENTINEL:
            self.assertion_encryption = assertion_encryption
        if authn_context is not SENTINEL:
            self.authn_context = authn_context
        if authn_context_comparison is not SENTINEL:
            self.authn_context_comparison = authn_context_comparison
        if cert_info is not SENTINEL:
            self.cert_info = cert_info
        if certificate is not SENTINEL:
            self.certificate = certificate
        if enabled is not SENTINEL:
            self.enabled = enabled
        if fed_id_from_name_id is not SENTINEL:
            self.fed_id_from_name_id = fed_id_from_name_id
        if idp_url is not SENTINEL:
            self.idp_url = idp_url
        if name_id_policy is not SENTINEL:
            self.name_id_policy = name_id_policy
        if signout_redirect_url is not SENTINEL:
            self.signout_redirect_url = signout_redirect_url
        self._kwargs = kwargs
