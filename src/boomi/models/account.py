
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .licensing import Licensing
from .molecule import Molecule


class AccountStatus(Enum):
    """An enumeration representing different categories.

    :cvar TRIAL: "trial"
    :vartype TRIAL: str
    :cvar ACTIVE: "active"
    :vartype ACTIVE: str
    :cvar SUSPENDED: "suspended"
    :vartype SUSPENDED: str
    :cvar DELETED: "deleted"
    :vartype DELETED: str
    :cvar UNLIMITED: "unlimited"
    :vartype UNLIMITED: str
    """

    TRIAL = "trial"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"
    UNLIMITED = "unlimited"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AccountStatus._member_map_.values()))


class SupportLevel(Enum):
    """An enumeration representing different categories.

    :cvar STANDARD: "standard"
    :vartype STANDARD: str
    :cvar PREMIER: "premier"
    :vartype PREMIER: str
    """

    STANDARD = "standard"
    PREMIER = "premier"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SupportLevel._member_map_.values()))


@JsonMap(
    {
        "account_id": "accountId",
        "date_created": "dateCreated",
        "expiration_date": "expirationDate",
        "over_deployed": "overDeployed",
        "suggestions_enabled": "suggestionsEnabled",
        "support_access": "supportAccess",
        "support_level": "supportLevel",
        "widget_account": "widgetAccount",
    }
)
class Account(BaseModel):
    """Account

    :param account_id: The ID of the account., defaults to None
    :type account_id: str, optional
    :param date_created: The creation date of the account., defaults to None
    :type date_created: str, optional
    :param expiration_date: The scheduled expiration date of the account., defaults to None
    :type expiration_date: str, optional
    :param licensing: Indicates the number of connections used and purchased in each of the connector type and production/test classifications. The classifications include standard, smallBusiness, enterprise, and tradingPartner., defaults to None
    :type licensing: Licensing, optional
    :param molecule: Indicates the number of Runtime clusters available on an account and the number of Runtime clusters currently in use., defaults to None
    :type molecule: Molecule, optional
    :param name: The name of the account., defaults to None
    :type name: str, optional
    :param over_deployed: Indicates the state of an account if one or more additional deployments are made after all available connection licenses have been used for any of the connector class., defaults to None
    :type over_deployed: bool, optional
    :param status: The status of the account. The allowed values are active or deleted., defaults to None
    :type status: AccountStatus, optional
    :param suggestions_enabled: Identifies whether this account has the Boomi Suggest feature enabled., defaults to None
    :type suggestions_enabled: bool, optional
    :param support_access: Identifies whether this account allows support user access., defaults to None
    :type support_access: bool, optional
    :param support_level: The level of support for this account. The allowed values are standard *or premier., defaults to None
    :type support_level: SupportLevel, optional
    :param widget_account: widget_account, defaults to None
    :type widget_account: bool, optional
    """

    def __init__(
        self,
        account_id: str = SENTINEL,
        date_created: str = SENTINEL,
        expiration_date: str = SENTINEL,
        licensing: Licensing = SENTINEL,
        molecule: Molecule = SENTINEL,
        name: str = SENTINEL,
        over_deployed: bool = SENTINEL,
        status: AccountStatus = SENTINEL,
        suggestions_enabled: bool = SENTINEL,
        support_access: bool = SENTINEL,
        support_level: SupportLevel = SENTINEL,
        widget_account: bool = SENTINEL,
        **kwargs,
    ):
        """Account

        :param account_id: The ID of the account., defaults to None
        :type account_id: str, optional
        :param date_created: The creation date of the account., defaults to None
        :type date_created: str, optional
        :param expiration_date: The scheduled expiration date of the account., defaults to None
        :type expiration_date: str, optional
        :param licensing: Indicates the number of connections used and purchased in each of the connector type and production/test classifications. The classifications include standard, smallBusiness, enterprise, and tradingPartner., defaults to None
        :type licensing: Licensing, optional
        :param molecule: Indicates the number of Runtime clusters available on an account and the number of Runtime clusters currently in use., defaults to None
        :type molecule: Molecule, optional
        :param name: The name of the account., defaults to None
        :type name: str, optional
        :param over_deployed: Indicates the state of an account if one or more additional deployments are made after all available connection licenses have been used for any of the connector class., defaults to None
        :type over_deployed: bool, optional
        :param status: The status of the account. The allowed values are active or deleted., defaults to None
        :type status: AccountStatus, optional
        :param suggestions_enabled: Identifies whether this account has the Boomi Suggest feature enabled., defaults to None
        :type suggestions_enabled: bool, optional
        :param support_access: Identifies whether this account allows support user access., defaults to None
        :type support_access: bool, optional
        :param support_level: The level of support for this account. The allowed values are standard *or premier., defaults to None
        :type support_level: SupportLevel, optional
        :param widget_account: widget_account, defaults to None
        :type widget_account: bool, optional
        """
        if account_id is not SENTINEL:
            self.account_id = account_id
        if date_created is not SENTINEL:
            self.date_created = date_created
        if expiration_date is not SENTINEL:
            self.expiration_date = expiration_date
        if licensing is not SENTINEL:
            self.licensing = self._define_object(licensing, Licensing)
        if molecule is not SENTINEL:
            self.molecule = self._define_object(molecule, Molecule)
        if name is not SENTINEL:
            self.name = name
        if over_deployed is not SENTINEL:
            self.over_deployed = over_deployed
        if status is not SENTINEL:
            self.status = self._enum_matching(status, AccountStatus.list(), "status")
        if suggestions_enabled is not SENTINEL:
            self.suggestions_enabled = suggestions_enabled
        if support_access is not SENTINEL:
            self.support_access = support_access
        if support_level is not SENTINEL:
            self.support_level = self._enum_matching(
                support_level, SupportLevel.list(), "support_level"
            )
        if widget_account is not SENTINEL:
            self.widget_account = widget_account
        self._kwargs = kwargs
