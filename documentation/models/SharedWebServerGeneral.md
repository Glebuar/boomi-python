# SharedWebServerGeneral

**Properties**

| Name                    | Type                            | Required | Description |
| :---------------------- | :------------------------------ | :------- | :---------- |
| api_type                | str                             | ✅       |             |
| authentication          | SharedWebServerAuthentication   | ✅       |             |
| base_url                | str                             | ✅       |             |
| external_host           | str                             | ✅       |             |
| internal_host           | str                             | ✅       |             |
| listener_ports          | ListenerPortConfiguration       | ✅       |             |
| protected_headers       | SharedWebServerProtectedHeaders | ✅       |             |
| ssl_certificate         | str                             | ✅       |             |
| examine_forward_headers | bool                            | ❌       |             |
| max_number_of_threads   | int                             | ❌       |             |
| override_url            | bool                            | ❌       |             |

