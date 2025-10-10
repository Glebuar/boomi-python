# IntegrationPack

**Properties**

| Name              | Type                            | Required | Description                                                                                                  |
| :---------------- | :------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------- |
| description       | str                             | ✅       | A description of the integration pack.                                                                       |
| id\_              | str                             | ❌       | A unique ID assigned by the system to the integration pack.                                                  |
| installation_type | IntegrationPackInstallationType | ❌       | The type of integration pack. Possible values:\<br /\>- SINGLE — single-attach\<br /\>- MULTI — multi-attach |
| name              | str                             | ❌       | The name of the integration pack.                                                                            |

# IntegrationPackInstallationType

The type of integration pack. Possible values:\<br /\>- SINGLE — single-attach\<br /\>- MULTI — multi-attach

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SINGLE | str  | ✅       | "SINGLE"    |
| MULTI  | str  | ✅       | "MULTI"     |

