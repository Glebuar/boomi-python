# EnvironmentMapExtensionExternalComponentSimpleExpression

**Properties**

| Name     | Type                                                             | Required | Description |
| :------- | :--------------------------------------------------------------- | :------- | :---------- |
| operator | EnvironmentMapExtensionExternalComponentSimpleExpressionOperator | ✅       |             |
| property | EnvironmentMapExtensionExternalComponentSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                                        | ❌       |             |

# EnvironmentMapExtensionExternalComponentSimpleExpressionOperator

**Properties**

| Name               | Type | Required | Description             |
| :----------------- | :--- | :------- | :---------------------- |
| EQUALS             | str  | ✅       | "EQUALS"                |
| LIKE               | str  | ✅       | "LIKE"                  |
| NOTEQUALS          | str  | ✅       | "NOT_EQUALS"            |
| ISNULL             | str  | ✅       | "IS_NULL"               |
| ISNOTNULL          | str  | ✅       | "IS_NOT_NULL"           |
| BETWEEN            | str  | ✅       | "BETWEEN"               |
| GREATERTHAN        | str  | ✅       | "GREATER_THAN"          |
| GREATERTHANOREQUAL | str  | ✅       | "GREATER_THAN_OR_EQUAL" |
| LESSTHAN           | str  | ✅       | "LESS_THAN"             |
| LESSTHANOREQUAL    | str  | ✅       | "LESS_THAN_OR_EQUAL"    |
| CONTAINS           | str  | ✅       | "CONTAINS"              |
| NOTCONTAINS        | str  | ✅       | "NOT_CONTAINS"          |

# EnvironmentMapExtensionExternalComponentSimpleExpressionProperty

**Properties**

| Name                      | Type | Required | Description                    |
| :------------------------ | :--- | :------- | :----------------------------- |
| ACCOUNTID                 | str  | ✅       | "ACCOUNT_ID"                   |
| ENVIRONMENTMAPEXTENSIONID | str  | ✅       | "ENVIRONMENT_MAP_EXTENSION_ID" |
| PACKAGEDCOMPONENTUID      | str  | ✅       | "PACKAGED_COMPONENT_UID"       |
| COMPONENTID               | str  | ✅       | "COMPONENT_ID"                 |
| COMPONENTVERSION          | str  | ✅       | "COMPONENT_VERSION"            |
| COMPONENTNAME             | str  | ✅       | "COMPONENT_NAME"               |
| COMPONENTTYPE             | str  | ✅       | "COMPONENT_TYPE"               |

