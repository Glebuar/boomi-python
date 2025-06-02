# Account

**Properties**

| Name                | Type          | Required | Description                                                                                                                                                                                                    |
| :------------------ | :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id          | str           | ❌       | The ID of the account.                                                                                                                                                                                         |
| date_created        | str           | ❌       | The creation date of the account.                                                                                                                                                                              |
| expiration_date     | str           | ❌       | The scheduled expiration date of the account.                                                                                                                                                                  |
| licensing           | Licensing     | ❌       | Indicates the number of connections used and purchased in each of the connector type and production/test classifications. The classifications include standard, smallBusiness, enterprise, and tradingPartner. |
| molecule            | Molecule      | ❌       | Indicates the number of Runtime clusters available on an account and the number of Runtime clusters currently in use.                                                                                          |
| name                | str           | ❌       | The name of the account.                                                                                                                                                                                       |
| over_deployed       | bool          | ❌       | Indicates the state of an account if one or more additional deployments are made after all available connection licenses have been used for any of the connector class.                                        |
| status              | AccountStatus | ❌       | The status of the account. The allowed values are active or deleted.                                                                                                                                           |
| suggestions_enabled | bool          | ❌       | Identifies whether this account has the Boomi Suggest feature enabled.                                                                                                                                         |
| support_access      | bool          | ❌       | Identifies whether this account allows support user access.                                                                                                                                                    |
| support_level       | SupportLevel  | ❌       | The level of support for this account. The allowed values are standard \*or premier.                                                                                                                           |
| widget_account      | bool          | ❌       |                                                                                                                                                                                                                |

# AccountStatus

The status of the account. The allowed values are active or deleted.

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| TRIAL     | str  | ✅       | "trial"     |
| ACTIVE    | str  | ✅       | "active"    |
| SUSPENDED | str  | ✅       | "suspended" |
| DELETED   | str  | ✅       | "deleted"   |
| UNLIMITED | str  | ✅       | "unlimited" |

# SupportLevel

The level of support for this account. The allowed values are standard \*or premier.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| STANDARD | str  | ✅       | "standard"  |
| PREMIER  | str  | ✅       | "premier"   |

