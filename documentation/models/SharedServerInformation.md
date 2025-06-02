# SharedServerInformation

**Properties**

| Name                    | Type    | Required | Description                                                                                                                                                                                                                                                                                                                                    |
| :---------------------- | :------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_type                | ApiType | ❌       | The level of user management and API management functionality applicable to the shared web server.Options are basic, intermediate, and advanced. The default is intermediate.                                                                                                                                                                  |
| atom_id                 | str     | ❌       | The ID of the Runtime that is hosting the shared web server.                                                                                                                                                                                                                                                                                   |
| auth                    | Auth    | ❌       | The authentication required by the web server. Options are none and basic. If minAuth is set to basic, you must also set auth to basic.                                                                                                                                                                                                        |
| auth_token              | str     | ❌       | If you configure BASIC authentication, this is an authentication token for connecting to the shared web server. You cannot update this with the UPDATE operation.                                                                                                                                                                              |
| check_forwarded_headers | bool    | ❌       | Information regarding the external host, might be forwarded in headers. The embedded Java technology is capable of examining these headers and extracting external host information for response and callback purposes. Set this to true to enable the server to check for this information. The default is false.                             |
| external_host           | str     | ❌       | The external host name or IP for the listener.                                                                                                                                                                                                                                                                                                 |
| external_http_port      | int     | ❌       | The external HTTP port routes to the shared web server listener.                                                                                                                                                                                                                                                                               |
| external_https_port     | int     | ❌       | The external HTTPS port routes to the shared web server listener.                                                                                                                                                                                                                                                                              |
| http_port               | int     | ❌       | The HTTP port on which the web server listens. The default port is 9090.                                                                                                                                                                                                                                                                       |
| https_port              | int     | ❌       | The SSL \(HTTPS\) port on which the web server listens, if applicable. The default port is 9093.                                                                                                                                                                                                                                               |
| internal_host           | str     | ❌       | For multi-homed boxes, the IP address you want to use for binding to a specific interface.                                                                                                                                                                                                                                                     |
| max_threads             | int     | ❌       | The maximum number of handler threads that the listen process spawn. It queues other requests.                                                                                                                                                                                                                                                 |
| min_auth                | MinAuth | ❌       | The minimum authentication required by the web server. Options are none and basic. The are multi-tenant, so the default is set to basic. The default for local Runtimes and Runtime clusters is none.                                                                                                                                          |
| override_url            | bool    | ❌       | Allows manual overriding of the exposed URL used to connect to the shared web server. This value is for informational purposes for any tenant. By default, this is false, meaning the URL is constructed based on the host name or external host name and port or SSL port settings. Set this to true to specify a custom URL attribute value. |
| ssl_certificate_id      | str     | ❌       | The component ID for the SSL certificate used by the server, if applicable.                                                                                                                                                                                                                                                                    |
| url                     | str     | ❌       | The URL for connecting to the shared web server.                                                                                                                                                                                                                                                                                               |

# ApiType

The level of user management and API management functionality applicable to the shared web server.Options are basic, intermediate, and advanced. The default is intermediate.

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| BASIC        | str  | ✅       | "basic"        |
| INTERMEDIATE | str  | ✅       | "intermediate" |
| ADVANCED     | str  | ✅       | "advanced"     |

# Auth

The authentication required by the web server. Options are none and basic. If minAuth is set to basic, you must also set auth to basic.

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| NONE  | str  | ✅       | "none"      |
| BASIC | str  | ✅       | "basic"     |

# MinAuth

The minimum authentication required by the web server. Options are none and basic. The are multi-tenant, so the default is set to basic. The default for local Runtimes and Runtime clusters is none.

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| NONE  | str  | ✅       | "none"      |
| BASIC | str  | ✅       | "basic"     |

