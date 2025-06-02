# AuditLog

**Properties**

| Name               | Type                   | Required | Description                                                                                           |
| :----------------- | :--------------------- | :------- | :---------------------------------------------------------------------------------------------------- |
| audit_log_property | List[AuditLogProperty] | ❌       |                                                                                                       |
| account_id         | str                    | ❌       | The account in which the action occurred.                                                             |
| action             | str                    | ❌       | The action type.                                                                                      |
| container_id       | str                    | ❌       | The ID of the Runtime, Runtime cluster, or Runtime cloud on which the action occurred.                |
| date\_             | str                    | ❌       | The date and time the action occurred.                                                                |
| document_id        | str                    | ❌       | The ID assigned to the Audit Log record.                                                              |
| level              | str                    | ❌       | The severity level of the action: DEBUG, ERROR, INFO, or WARNING.                                     |
| message            | str                    | ❌       | A descriptive message. Not all types of management actions have a message in their audit log entries. |
| modifier           | str                    | ❌       | The action type qualifier.                                                                            |
| source             | str                    | ❌       | Where the action occurred: API, INTERNAL, MOBILE, UI, or UNKNOWN                                      |
| type\_             | str                    | ❌       | The type of object on which the action occurred.                                                      |
| user_id            | str                    | ❌       | The ID \(email address\) of the user who performed the action.                                        |

