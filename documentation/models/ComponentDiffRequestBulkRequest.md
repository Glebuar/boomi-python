# ComponentDiffRequestBulkRequest

**Properties**

| Name    | Type                                | Required | Description                                                                                                                        |
| :------ | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| request | List[BulkId]                        | ❌       |                                                                                                                                    |
| type\_  | ComponentDiffRequestBulkRequestType | ❌       | Read only. The type of component. See the section Component Types later in this topic for a complete list of component type values |

# ComponentDiffRequestBulkRequestType

Read only. The type of component. See the section Component Types later in this topic for a complete list of component type values

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| GET    | str  | ✅       | "GET"       |
| DELETE | str  | ✅       | "DELETE"    |
| UPDATE | str  | ✅       | "UPDATE"    |
| CREATE | str  | ✅       | "CREATE"    |

