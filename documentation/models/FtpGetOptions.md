# FtpGetOptions

**Properties**

| Name                    | Type                      | Required | Description |
| :---------------------- | :------------------------ | :------- | :---------- |
| file_to_move            | str                       | ✅       |             |
| max_file_count          | int                       | ✅       |             |
| remote_directory        | str                       | ✅       |             |
| ftp_action              | FtpGetOptionsFtpAction    | ❌       |             |
| transfer_type           | FtpGetOptionsTransferType | ❌       |             |
| use_default_get_options | bool                      | ❌       |             |

# FtpGetOptionsFtpAction

**Properties**

| Name            | Type | Required | Description       |
| :-------------- | :--- | :------- | :---------------- |
| ACTIONGET       | str  | ✅       | "actionget"       |
| ACTIONGETDELETE | str  | ✅       | "actiongetdelete" |
| ACTIONGETMOVE   | str  | ✅       | "actiongetmove"   |

# FtpGetOptionsTransferType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| ASCII  | str  | ✅       | "ascii"     |
| BINARY | str  | ✅       | "binary"    |

