# FtpSettings

**Properties**

| Name                 | Type           | Required | Description |
| :------------------- | :------------- | :------- | :---------- |
| ftpssl_options       | FtpsslOptions  | ✅       |             |
| host                 | str            | ✅       |             |
| password             | str            | ✅       |             |
| port                 | int            | ✅       |             |
| user                 | str            | ✅       |             |
| connection_mode      | ConnectionMode | ❌       |             |
| use_default_settings | bool           | ❌       |             |

# ConnectionMode

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| ACTIVE  | str  | ✅       | "active"    |
| PASSIVE | str  | ✅       | "passive"   |

