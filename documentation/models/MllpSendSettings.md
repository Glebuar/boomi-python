# MllpSendSettings

**Properties**

| Name               | Type           | Required | Description |
| :----------------- | :------------- | :------- | :---------- |
| mllpssl_options    | MllpsslOptions | ✅       |             |
| end_block          | EdiDelimiter   | ✅       |             |
| end_data           | EdiDelimiter   | ✅       |             |
| host               | str            | ✅       |             |
| port               | int            | ✅       |             |
| start_block        | EdiDelimiter   | ✅       |             |
| halt_timeout       | bool           | ❌       |             |
| inactivity_timeout | int            | ❌       |             |
| max_connections    | int            | ❌       |             |
| max_retry          | int            | ❌       |             |
| persistent         | bool           | ❌       |             |
| receive_timeout    | int            | ❌       |             |
| send_timeout       | int            | ❌       |             |

