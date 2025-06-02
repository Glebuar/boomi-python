# SharedWebServerAuthentication

**Properties**

| Name                            | Type                                    | Required | Description |
| :------------------------------ | :-------------------------------------- | :------- | :---------- |
| auth_type                       | str                                     | ✅       |             |
| client_certificate_header_name  | str                                     | ✅       |             |
| login_module_class_name         | str                                     | ✅       |             |
| login_module_options            | SharedWebServerLoginModuleConfiguration | ✅       |             |
| cache_authentication_timeout    | int                                     | ❌       |             |
| cache_authorization_credentials | bool                                    | ❌       |             |

