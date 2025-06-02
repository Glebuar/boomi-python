# PublisherIntegrationPack

**Properties**

| Name                          | Type                                     | Required | Description                                                                                                                                                                                                         |
| :---------------------------- | :--------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| description                   | str                                      | ✅       |                                                                                                                                                                                                                     |
| publisher_packaged_components | PublisherPackagedComponents              | ❌       |                                                                                                                                                                                                                     |
| id\_                          | str                                      | ❌       | A unique ID assigned by the system to the integration pack.                                                                                                                                                         |
| installation_type             | PublisherIntegrationPackInstallationType | ❌       | The type of integration pack. Possible values: - SINGLE — single attachment - MULTI — multiple attachment                                                                                                           |
| name                          | str                                      | ❌       | The name of the integration pack.                                                                                                                                                                                   |
| operation_type                | OperationType                            | ❌       | Specifies the type of operation (ADD or DELETE) to perform when updating the packaged component to the integration pack. This field is mandatory for the Update operation and is not available for other operations |

# PublisherIntegrationPackInstallationType

The type of integration pack. Possible values: - SINGLE — single attachment - MULTI — multiple attachment

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| SINGLE | str  | ✅       | "SINGLE"    |
| MULTI  | str  | ✅       | "MULTI"     |

# OperationType

Specifies the type of operation (ADD or DELETE) to perform when updating the packaged component to the integration pack. This field is mandatory for the Update operation and is not available for other operations

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| ADD    | str  | ✅       | "ADD"       |
| DELETE | str  | ✅       | "DELETE"    |

