# CustomTrackedField

**Properties**

| Name     | Type                   | Required | Description                                                                               |
| :------- | :--------------------- | :------- | :---------------------------------------------------------------------------------------- |
| label    | str                    | ❌       | The display name of the custom tracked field.                                             |
| position | int                    | ❌       | The display position of the custom tracked field.                                         |
| type\_   | CustomTrackedFieldType | ❌       | The type of custom tracked field. Allowed values include character, datetime, and number. |

# CustomTrackedFieldType

The type of custom tracked field. Allowed values include character, datetime, and number.

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| CHARACTER | str  | ✅       | "character" |
| DATETIME  | str  | ✅       | "datetime"  |
| NUMBER    | str  | ✅       | "number"    |

