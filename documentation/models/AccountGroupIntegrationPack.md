# AccountGroupIntegrationPack

**Properties**

| Name                  | Type                                        | Required | Description                                                                                                                                |
| :-------------------- | :------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| account_group_id      | str                                         | ❌       | The ID of the account group.                                                                                                               |
| id\_                  | str                                         | ❌       | A unique ID assigned by the system to the integration pack. This field populates only if you add the integration pack to an account group. |
| installation_type     | AccountGroupIntegrationPackInstallationType | ❌       | The type of integration pack. Possible values: - SINGLE — single attachment - MULTI — multiple attachment                                  |
| integration_pack_id   | str                                         | ❌       | A unique ID assigned by the system to the integration pack.                                                                                |
| integration_pack_name | str                                         | ❌       | The name of the integration pack.                                                                                                          |

# AccountGroupIntegrationPackInstallationType

The type of integration pack. Possible values: - SINGLE — single attachment - MULTI — multiple attachment

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SINGLE | str  | ✅       | "SINGLE"    |
| MULTI  | str  | ✅       | "MULTI"     |

