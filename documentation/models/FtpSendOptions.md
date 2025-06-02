# FtpSendOptions

**Properties**

| Name                     | Type                       | Required | Description |
| :----------------------- | :------------------------- | :------- | :---------- |
| move_to_directory        | str                        | ✅       |             |
| remote_directory         | str                        | ✅       |             |
| ftp_action               | FtpSendOptionsFtpAction    | ❌       |             |
| transfer_type            | FtpSendOptionsTransferType | ❌       |             |
| use_default_send_options | bool                       | ❌       |             |

# FtpSendOptionsFtpAction

**Properties**

| Name               | Type | Required | Description          |
| :----------------- | :--- | :------- | :------------------- |
| ACTIONPUTRENAME    | str  | ✅       | "actionputrename"    |
| ACTIONPUTAPPEND    | str  | ✅       | "actionputappend"    |
| ACTIONPUTERROR     | str  | ✅       | "actionputerror"     |
| ACTIONPUTOVERWRITE | str  | ✅       | "actionputoverwrite" |

# FtpSendOptionsTransferType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| ASCII  | str  | ✅       | "ascii"     |
| BINARY | str  | ✅       | "binary"    |

