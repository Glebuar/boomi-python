# Resource

**Properties**

| Name          | Type       | Required | Description                   |
| :------------ | :--------- | :------- | :---------------------------- |
| resource_id   | str        | ✅       | Account group resource ID.    |
| resource_name | str        | ✅       | Account group resource name.  |
| object_type   | ObjectType | ❌       | Resource object type details. |

# ObjectType

Resource object type details.

**Properties**

| Name             | Type | Required | Description         |
| :--------------- | :--- | :------- | :------------------ |
| CLOUD            | str  | ✅       | "Cloud"             |
| CONNECTOR        | str  | ✅       | "Connector"         |
| DATAHUBMODEL     | str  | ✅       | "Data Hub Model"    |
| INTEGRATIONPACK  | str  | ✅       | "Integration Pack"  |
| PUBLISHEDPROCESS | str  | ✅       | "Published Process" |
| ROLE             | str  | ✅       | "Role"              |

