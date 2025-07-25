# Connector

**Properties**

| Name   | Type | Required | Description                                                                                                                                                                                             |
| :----- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name   | str  | ❌       | The user-facing connector label of the connector type, which mimics the connector type names presented on the **Build** tab of the user interface.                                                      |
| type\_ | str  | ❌       | The internal and unique identifier for connector type, such as `http`, `ftp`, `greatplains`. The [Component Metadata object](/api/platformapi#tag/ComponentMetadata) refers to this field as _subType_. |

