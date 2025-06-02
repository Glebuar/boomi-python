
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .public_certificate import PublicCertificate


class GlobalUsageCode(Enum):
    """An enumeration representing different categories.

    :cvar TEST: "Test"
    :vartype TEST: str
    :cvar PRODUCTION: "Production"
    :vartype PRODUCTION: str
    """

    TEST = "Test"
    PRODUCTION = "Production"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GlobalUsageCode._member_map_.values()))


class PartnerIdType(Enum):
    """An enumeration representing different categories.

    :cvar DUNS: "DUNS"
    :vartype DUNS: str
    """

    DUNS = "DUNS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PartnerIdType._member_map_.values()))


@JsonMap(
    {
        "encryption_public_certificate": "encryptionPublicCertificate",
        "global_partner_classification_code": "globalPartnerClassificationCode",
        "global_usage_code": "globalUsageCode",
        "partner_id": "partnerId",
        "partner_id_type": "partnerIdType",
        "partner_location": "partnerLocation",
        "signing_public_certificate": "signingPublicCertificate",
        "supply_chain_code": "supplyChainCode",
    }
)
class RosettaNetControlInfo(BaseModel):
    """RosettaNetControlInfo

    :param encryption_public_certificate: encryption_public_certificate, defaults to None
    :type encryption_public_certificate: PublicCertificate, optional
    :param global_partner_classification_code: global_partner_classification_code, defaults to None
    :type global_partner_classification_code: str, optional
    :param global_usage_code: global_usage_code, defaults to None
    :type global_usage_code: GlobalUsageCode, optional
    :param partner_id: partner_id, defaults to None
    :type partner_id: str, optional
    :param partner_id_type: partner_id_type, defaults to None
    :type partner_id_type: PartnerIdType, optional
    :param partner_location: partner_location, defaults to None
    :type partner_location: str, optional
    :param signing_public_certificate: signing_public_certificate, defaults to None
    :type signing_public_certificate: PublicCertificate, optional
    :param supply_chain_code: supply_chain_code, defaults to None
    :type supply_chain_code: str, optional
    """

    def __init__(
        self,
        encryption_public_certificate: PublicCertificate = SENTINEL,
        global_partner_classification_code: str = SENTINEL,
        global_usage_code: GlobalUsageCode = SENTINEL,
        partner_id: str = SENTINEL,
        partner_id_type: PartnerIdType = SENTINEL,
        partner_location: str = SENTINEL,
        signing_public_certificate: PublicCertificate = SENTINEL,
        supply_chain_code: str = SENTINEL,
        **kwargs,
    ):
        """RosettaNetControlInfo

        :param encryption_public_certificate: encryption_public_certificate, defaults to None
        :type encryption_public_certificate: PublicCertificate, optional
        :param global_partner_classification_code: global_partner_classification_code, defaults to None
        :type global_partner_classification_code: str, optional
        :param global_usage_code: global_usage_code, defaults to None
        :type global_usage_code: GlobalUsageCode, optional
        :param partner_id: partner_id, defaults to None
        :type partner_id: str, optional
        :param partner_id_type: partner_id_type, defaults to None
        :type partner_id_type: PartnerIdType, optional
        :param partner_location: partner_location, defaults to None
        :type partner_location: str, optional
        :param signing_public_certificate: signing_public_certificate, defaults to None
        :type signing_public_certificate: PublicCertificate, optional
        :param supply_chain_code: supply_chain_code, defaults to None
        :type supply_chain_code: str, optional
        """
        if encryption_public_certificate is not SENTINEL:
            self.encryption_public_certificate = self._define_object(
                encryption_public_certificate, PublicCertificate
            )
        if global_partner_classification_code is not SENTINEL:
            self.global_partner_classification_code = global_partner_classification_code
        if global_usage_code is not SENTINEL:
            self.global_usage_code = self._enum_matching(
                global_usage_code, GlobalUsageCode.list(), "global_usage_code"
            )
        if partner_id is not SENTINEL:
            self.partner_id = partner_id
        if partner_id_type is not SENTINEL:
            self.partner_id_type = self._enum_matching(
                partner_id_type, PartnerIdType.list(), "partner_id_type"
            )
        if partner_location is not SENTINEL:
            self.partner_location = partner_location
        if signing_public_certificate is not SENTINEL:
            self.signing_public_certificate = self._define_object(
                signing_public_certificate, PublicCertificate
            )
        if supply_chain_code is not SENTINEL:
            self.supply_chain_code = supply_chain_code
        self._kwargs = kwargs
