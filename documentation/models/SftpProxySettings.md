# SftpProxySettings

**Properties**

| Name          | Type                  | Required | Description |
| :------------ | :-------------------- | :------- | :---------- |
| host          | str                   | ✅       |             |
| password      | str                   | ✅       |             |
| port          | int                   | ✅       |             |
| user          | str                   | ✅       |             |
| proxy_enabled | bool                  | ❌       |             |
| type\_        | SftpProxySettingsType | ❌       |             |

# SftpProxySettingsType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| ATOM   | str  | ✅       | "ATOM"      |
| HTTP   | str  | ✅       | "HTTP"      |
| SOCKS4 | str  | ✅       | "SOCKS4"    |
| SOCKS5 | str  | ✅       | "SOCKS5"    |

