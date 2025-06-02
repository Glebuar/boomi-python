# ProcessLog

**Properties**

| Name         | Type     | Required | Description                                                                                                                                                                                          |
| :----------- | :------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| execution_id | str      | ❌       | The ID of the process run.                                                                                                                                                                           |
| log_level    | LogLevel | ❌       | The process execution log level with ALL being the default. If you do not specify the log level, you receive all types of logs. The log level is case sensitive; you must use all uppercase letters. |

# LogLevel

The process execution log level with ALL being the default. If you do not specify the log level, you receive all types of logs. The log level is case sensitive; you must use all uppercase letters.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| SEVERE  | str  | ✅       | "SEVERE"    |
| WARNING | str  | ✅       | "WARNING"   |
| INFO    | str  | ✅       | "INFO"      |
| CONFIG  | str  | ✅       | "CONFIG"    |
| FINE    | str  | ✅       | "FINE"      |
| FINER   | str  | ✅       | "FINER"     |
| FINEST  | str  | ✅       | "FINEST"    |
| ALL     | str  | ✅       | "ALL"       |

