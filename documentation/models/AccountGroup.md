# AccountGroup

**Properties**

| Name                       | Type                    | Required | Description                                                                                                                              |
| :------------------------- | :---------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| resources                  | Resources               | ❌       |                                                                                                                                          |
| account_id                 | str                     | ❌       | The ID of the primary account under which the account group exists.                                                                      |
| auto_subscribe_alert_level | AutoSubscribeAlertLevel | ❌       | The severity level of email alerts sent to member users in the account group.                                                            |
| default_group              | bool                    | ❌       | true — The account group is All Accounts, which the system creates automatically.\<br /\> false — The account group is not All Accounts. |
| id\_                       | str                     | ❌       | The ID of the account group.                                                                                                             |
| name                       | str                     | ❌       | The name of the account group as displayed on the **Account Information** tab of the **Setup** page.                                     |

# AutoSubscribeAlertLevel

The severity level of email alerts sent to member users in the account group.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| NONE    | str  | ✅       | "none"      |
| INFO    | str  | ✅       | "info"      |
| WARNING | str  | ✅       | "warning"   |
| ERROR   | str  | ✅       | "error"     |

