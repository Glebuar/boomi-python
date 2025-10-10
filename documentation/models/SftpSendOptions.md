# SftpSendOptions

**Properties**

| Name                     | Type                     | Required | Description |
| :----------------------- | :----------------------- | :------- | :---------- |
| move_to_directory        | str                      | ✅       |             |
| remote_directory         | str                      | ✅       |             |
| ftp_action               | SftpSendOptionsFtpAction | ❌       |             |
| move_to_force_override   | bool                     | ❌       |             |
| use_default_send_options | bool                     | ❌       |             |

# SftpSendOptionsFtpAction

**Properties**

| Name               | Type | Required | Description          |
| :----------------- | :--- | :------- | :------------------- |
| ACTIONPUTRENAME    | str  | ✅       | "actionputrename"    |
| ACTIONPUTAPPEND    | str  | ✅       | "actionputappend"    |
| ACTIONPUTERROR     | str  | ✅       | "actionputerror"     |
| ACTIONPUTOVERWRITE | str  | ✅       | "actionputoverwrite" |

