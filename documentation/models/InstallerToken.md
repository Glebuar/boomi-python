# InstallerToken

**Properties**

| Name             | Type        | Required | Description                                                                                 |
| :--------------- | :---------- | :------- | :------------------------------------------------------------------------------------------ |
| account_id       | str         | ❌       |                                                                                             |
| cloud_id         | str         | ❌       | \(For Runtime cloud installation\) A unique ID assigned by the system to the Runtime cloud. |
| created          | str         | ❌       |                                                                                             |
| duration_minutes | int         | ❌       | The number of minutes for which the installer token is valid, from 30 to 1440.              |
| expiration       | str         | ❌       |                                                                                             |
| install_type     | InstallType | ❌       | - ATOM\<br /\>- MOLECULE\<br /\>- CLOUD\<br /\>- BROKER                                     |
| token            | str         | ❌       |                                                                                             |

# InstallType

- ATOM\<br /\>- MOLECULE\<br /\>- CLOUD\<br /\>- BROKER

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| CLOUD    | str  | ✅       | "CLOUD"     |
| ATOM     | str  | ✅       | "ATOM"      |
| MOLECULE | str  | ✅       | "MOLECULE"  |
| BROKER   | str  | ✅       | "BROKER"    |
| GATEWAY  | str  | ✅       | "GATEWAY"   |

