# ComponentReferenceBulkRequest

**Properties**

| Name    | Type                              | Required | Description |
| :------ | :-------------------------------- | :------- | :---------- |
| request | List[BulkId]                      | ❌       |             |
| type\_  | ComponentReferenceBulkRequestType | ❌       |             |

# ComponentReferenceBulkRequestType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| GET    | str  | ✅       | "GET"       |
| DELETE | str  | ✅       | "DELETE"    |
| UPDATE | str  | ✅       | "UPDATE"    |
| CREATE | str  | ✅       | "CREATE"    |

