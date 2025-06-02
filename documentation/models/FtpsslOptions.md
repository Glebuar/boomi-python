# FtpsslOptions

**Properties**

| Name                      | Type               | Required | Description |
| :------------------------ | :----------------- | :------- | :---------- |
| client_ssl_certificate    | PrivateCertificate | ✅       |             |
| sslmode                   | Sslmode            | ❌       |             |
| use_client_authentication | bool               | ❌       |             |

# Sslmode

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| NONE     | str  | ✅       | "none"      |
| EXPLICIT | str  | ✅       | "explicit"  |
| IMPLICIT | str  | ✅       | "implicit"  |

