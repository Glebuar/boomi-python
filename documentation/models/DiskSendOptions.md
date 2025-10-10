# DiskSendOptions

**Properties**

| Name                     | Type        | Required | Description |
| :----------------------- | :---------- | :------- | :---------- |
| send_directory           | str         | ✅       |             |
| create_directory         | bool        | ❌       |             |
| use_default_send_options | bool        | ❌       |             |
| write_option             | WriteOption | ❌       |             |

# WriteOption

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| UNIQUE | str  | ✅       | "unique"    |
| OVER   | str  | ✅       | "over"      |
| APPEND | str  | ✅       | "append"    |
| ABORT  | str  | ✅       | "abort"     |

