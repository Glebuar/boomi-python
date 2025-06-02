# ExecutionRecordQueryConfig

**Properties**

| Name         | Type                                  | Required | Description |
| :----------- | :------------------------------------ | :------- | :---------- |
| query_filter | ExecutionRecordQueryConfigQueryFilter | ✅       |             |
| query_sort   | QuerySort                             | ❌       |             |

# ExecutionRecordQueryConfigQueryFilter

**Properties**

| Name       | Type                      | Required | Description |
| :--------- | :------------------------ | :------- | :---------- |
| expression | ExecutionRecordExpression | ✅       |             |

# QuerySort

**Properties**

| Name       | Type            | Required | Description |
| :--------- | :-------------- | :------- | :---------- |
| sort_field | List[SortField] | ✅       |             |

# SortField

**Properties**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| field_name | str  | ❌       |             |
| sort_order | str  | ❌       |             |

