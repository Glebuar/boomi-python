# SftpGetOptions

**Properties**

| Name                    | Type                    | Required | Description |
| :---------------------- | :---------------------- | :------- | :---------- |
| file_to_move            | str                     | ✅       |             |
| max_file_count          | int                     | ✅       |             |
| move_to_directory       | str                     | ✅       |             |
| remote_directory        | str                     | ✅       |             |
| ftp_action              | SftpGetOptionsFtpAction | ❌       |             |
| move_to_force_override  | bool                    | ❌       |             |
| use_default_get_options | bool                    | ❌       |             |

# SftpGetOptionsFtpAction

**Properties**

| Name            | Type | Required | Description       |
| :-------------- | :--- | :------- | :---------------- |
| ACTIONGET       | str  | ✅       | "actionget"       |
| ACTIONGETDELETE | str  | ✅       | "actiongetdelete" |
| ACTIONGETMOVE   | str  | ✅       | "actiongetmove"   |

