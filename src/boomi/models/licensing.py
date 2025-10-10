
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .license import License


@JsonMap(
    {
        "enterprise_test": "enterpriseTest",
        "small_business": "smallBusiness",
        "small_business_test": "smallBusinessTest",
        "standard_test": "standardTest",
        "trading_partner": "tradingPartner",
        "trading_partner_test": "tradingPartnerTest",
    }
)
class Licensing(BaseModel):
    """Indicates the number of connections used and purchased in each of the connector type and production/test classifications. The classifications include standard, smallBusiness, enterprise, and tradingPartner.

    :param enterprise: enterprise, defaults to None
    :type enterprise: License, optional
    :param enterprise_test: enterprise_test, defaults to None
    :type enterprise_test: License, optional
    :param small_business: small_business, defaults to None
    :type small_business: License, optional
    :param small_business_test: small_business_test, defaults to None
    :type small_business_test: License, optional
    :param standard: standard, defaults to None
    :type standard: License, optional
    :param standard_test: standard_test, defaults to None
    :type standard_test: License, optional
    :param trading_partner: trading_partner, defaults to None
    :type trading_partner: License, optional
    :param trading_partner_test: trading_partner_test, defaults to None
    :type trading_partner_test: License, optional
    """

    def __init__(
        self,
        enterprise: License = SENTINEL,
        enterprise_test: License = SENTINEL,
        small_business: License = SENTINEL,
        small_business_test: License = SENTINEL,
        standard: License = SENTINEL,
        standard_test: License = SENTINEL,
        trading_partner: License = SENTINEL,
        trading_partner_test: License = SENTINEL,
        **kwargs,
    ):
        """Indicates the number of connections used and purchased in each of the connector type and production/test classifications. The classifications include standard, smallBusiness, enterprise, and tradingPartner.

        :param enterprise: enterprise, defaults to None
        :type enterprise: License, optional
        :param enterprise_test: enterprise_test, defaults to None
        :type enterprise_test: License, optional
        :param small_business: small_business, defaults to None
        :type small_business: License, optional
        :param small_business_test: small_business_test, defaults to None
        :type small_business_test: License, optional
        :param standard: standard, defaults to None
        :type standard: License, optional
        :param standard_test: standard_test, defaults to None
        :type standard_test: License, optional
        :param trading_partner: trading_partner, defaults to None
        :type trading_partner: License, optional
        :param trading_partner_test: trading_partner_test, defaults to None
        :type trading_partner_test: License, optional
        """
        if enterprise is not SENTINEL:
            self.enterprise = self._define_object(enterprise, License)
        if enterprise_test is not SENTINEL:
            self.enterprise_test = self._define_object(enterprise_test, License)
        if small_business is not SENTINEL:
            self.small_business = self._define_object(small_business, License)
        if small_business_test is not SENTINEL:
            self.small_business_test = self._define_object(small_business_test, License)
        if standard is not SENTINEL:
            self.standard = self._define_object(standard, License)
        if standard_test is not SENTINEL:
            self.standard_test = self._define_object(standard_test, License)
        if trading_partner is not SENTINEL:
            self.trading_partner = self._define_object(trading_partner, License)
        if trading_partner_test is not SENTINEL:
            self.trading_partner_test = self._define_object(
                trading_partner_test, License
            )
        self._kwargs = kwargs
