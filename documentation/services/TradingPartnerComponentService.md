# TradingPartnerComponentService

A list of all methods in the `TradingPartnerComponentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :---------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_trading_partner_component](#create_trading_partner_component)         | - This operation creates a Trading Partner Component object with a specified component name. - The request body requires the standard, classification, and componentName fields. If you omit the folderName field, you must use the folderId field — and vice versa. If you omit the componentID field and the IDs of any certificates you want to create, their values are assigned when you create the components. If you leave off the folderID field when creating a component, it assigns a value. - Includes the organizationId field only if the trading partner is to reference an Organization component, in which case the field value is the ID of the Organization component. A request specifying the organizationId field populates the ContactInformation fields with the data from the referenced Organization component.                                                                                                                                                                         |
| [get_trading_partner_component](#get_trading_partner_component)               | The ordinary GET operation returns a single Trading Partner Component object based on the supplied ID. A GET operation specifying the ID of a deleted Trading Partner component retrieves the component. In the component, the deleted field’s value is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [update_trading_partner_component](#update_trading_partner_component)         | This operation overwrites the Trading Partner Component object with the specified component ID except as described: - If the fields are empty, an UPDATE operation specifying the organizationId field populates the ContactInformation fields with the data from the referenced Organization component. However, if those fields have values, they are not overwritten. An UPDATE operation specifying the ID of a deleted Trading Partner component restores the component to a non-deleted state, assuming the request is otherwise valid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [delete_trading_partner_component](#delete_trading_partner_component)         | The DELETE operation deletes the Trading Partner Component object with a specific component ID. A DELETE operation specifying the ID of a deleted Trading Partner component returns a false response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [bulk_trading_partner_component](#bulk_trading_partner_component)             | The bulk GET operation returns multiple Trading Partner Component objects based on the supplied IDs, to a maximum of 100.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [query_trading_partner_component](#query_trading_partner_component)           | The QUERY operation returns each Trading Partner component that meets the specified filtering criteria. - The name field in a QUERY filter represents the object’s componentName field. - Only the LIKE operator is allowed with a name filter. Likewise, you can only use the EQUALS operator with a classification, standard, identifier filter, or a communication method filter (as2, disk, ftp, http, mllp, sftp). Filtering on a communication method field requests Trading Partner components by defining the communication method. - If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator. The QUERY request does not support the logical OR operator. - The QUERY results omit the folderName field. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_trading_partner_component](#query_more_trading_partner_component) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## create_trading_partner_component

- This operation creates a Trading Partner Component object with a specified component name. - The request body requires the standard, classification, and componentName fields. If you omit the folderName field, you must use the folderId field — and vice versa. If you omit the componentID field and the IDs of any certificates you want to create, their values are assigned when you create the components. If you leave off the folderID field when creating a component, it assigns a value. - Includes the organizationId field only if the trading partner is to reference an Organization component, in which case the field value is the ID of the Organization component. A request specifying the organizationId field populates the ContactInformation fields with the data from the referenced Organization component.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [TradingPartnerComponent](../models/TradingPartnerComponent.md) | ❌       | The request body. |

**Return Type**

`TradingPartnerComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerComponent

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerComponent(
    contact_info={
        "address1": "address1",
        "address2": "address2",
        "city": "city",
        "contact_name": "contactName",
        "country": "country",
        "email": "email",
        "fax": "fax",
        "phone": "phone",
        "postalcode": "postalcode",
        "state": "state"
    },
    partner_communication={
        "as2_communication_options": {
            "as2_default_partner_settings": {
                "auth_settings": {
                    "password": "password",
                    "user": "user"
                },
                "authentication_type": "NONE",
                "client_ssl_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId",
                    "pass_phrase": "passPhrase"
                },
                "ssl_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId"
                },
                "url": "url",
                "use_default_settings": False,
                "verify_hostname": False
            },
            "as2_receive_options": {
                "as2_default_partner_info": {
                    "listen_attachment_settings": {
                        "attachment_cache": "attachmentCache",
                        "attachment_content_type": [
                            "application/xml"
                        ],
                        "multiple_attachments": False
                    },
                    "listen_auth_settings": {
                        "password": "password",
                        "user": "user"
                    },
                    "as2_id": "as2Id",
                    "basic_auth_enabled": True,
                    "client_ssl_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "enabled_legacy_smime": False,
                    "encryption_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "mdn_signature_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "messages_to_check_for_duplicates": 0,
                    "reject_duplicate_messages": False,
                    "signing_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    }
                },
                "as2_default_partner_mdn_options": {
                    "external_url": "externalURL",
                    "mdn_client_ssl_cert": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "mdn_digest_alg": "SHA1",
                    "mdn_ssl_cert": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "request_mdn": True,
                    "signed": True,
                    "synchronous": "sync",
                    "use_external_url": False,
                    "use_ssl": False
                },
                "as2_default_partner_message_options": {
                    "attachment_cache": "attachmentCache",
                    "attachment_option": "BATCH",
                    "compressed": True,
                    "data_content_type": "textplain",
                    "encrypted": True,
                    "encryption_algorithm": "na",
                    "max_document_count": 4,
                    "multiple_attachments": True,
                    "signed": True,
                    "signing_digest_alg": "SHA1",
                    "subject": "subject"
                },
                "as2_my_company_info": {
                    "as2_id": "as2Id",
                    "enabled_legacy_smime": False,
                    "encryption_private_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "mdn_signature_private_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "signing_private_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    }
                }
            },
            "as2_send_options": {
                "as2_mdn_options": {
                    "external_url": "externalURL",
                    "mdn_client_ssl_cert": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "mdn_digest_alg": "SHA1",
                    "mdn_ssl_cert": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "request_mdn": True,
                    "signed": True,
                    "synchronous": "sync",
                    "use_external_url": False,
                    "use_ssl": False
                },
                "as2_message_options": {
                    "attachment_cache": "attachmentCache",
                    "attachment_option": "BATCH",
                    "compressed": True,
                    "data_content_type": "textplain",
                    "encrypted": True,
                    "encryption_algorithm": "na",
                    "max_document_count": 4,
                    "multiple_attachments": True,
                    "signed": True,
                    "signing_digest_alg": "SHA1",
                    "subject": "subject"
                },
                "as2_partner_info": {
                    "listen_attachment_settings": {
                        "attachment_cache": "attachmentCache",
                        "attachment_content_type": [
                            "application/xml"
                        ],
                        "multiple_attachments": False
                    },
                    "listen_auth_settings": {
                        "password": "password",
                        "user": "user"
                    },
                    "as2_id": "as2Id",
                    "basic_auth_enabled": True,
                    "client_ssl_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "enabled_legacy_smime": False,
                    "encryption_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "mdn_signature_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "messages_to_check_for_duplicates": 0,
                    "reject_duplicate_messages": False,
                    "signing_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    }
                }
            },
            "as2_send_settings": {
                "auth_settings": {
                    "password": "password",
                    "user": "user"
                },
                "authentication_type": "NONE",
                "client_ssl_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId",
                    "pass_phrase": "passPhrase"
                },
                "ssl_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId"
                },
                "url": "url",
                "use_default_settings": False,
                "verify_hostname": False
            },
            "communication_setting": "default",
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "disk_communication_options": {
            "communication_setting": "default",
            "disk_get_options": {
                "delete_after_read": False,
                "file_filter": "fileFilter",
                "filter_match_type": "wildcard",
                "get_directory": "getDirectory",
                "max_file_count": 2,
                "use_default_get_options": True
            },
            "disk_send_options": {
                "create_directory": False,
                "send_directory": "sendDirectory",
                "use_default_send_options": True,
                "write_option": "unique"
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "ftp_communication_options": {
            "communication_setting": "default",
            "ftp_get_options": {
                "file_to_move": "fileToMove",
                "ftp_action": "actionget",
                "max_file_count": 1,
                "remote_directory": "remoteDirectory",
                "transfer_type": "ascii",
                "use_default_get_options": True
            },
            "ftp_send_options": {
                "ftp_action": "actionputrename",
                "move_to_directory": "moveToDirectory",
                "remote_directory": "remoteDirectory",
                "transfer_type": "ascii",
                "use_default_send_options": True
            },
            "ftp_settings": {
                "ftpssl_options": {
                    "client_ssl_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "sslmode": "none",
                    "use_client_authentication": True
                },
                "connection_mode": "active",
                "host": "host",
                "password": "password",
                "port": 1,
                "use_default_settings": True,
                "user": "user"
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "http_communication_options": {
            "communication_setting": "default",
            "http_get_options": {
                "data_content_type": "dataContentType",
                "follow_redirects": True,
                "method_type": "GET",
                "path_elements": {
                    "element": [
                        {
                            "name": "name"
                        }
                    ]
                },
                "reflect_headers": {
                    "element": [
                        {
                            "name": "name"
                        }
                    ]
                },
                "request_headers": {
                    "header": [
                        {
                            "header_field_name": "headerFieldName",
                            "target_property_name": "targetPropertyName"
                        }
                    ]
                },
                "request_profile": "requestProfile",
                "request_profile_type": "NONE",
                "response_header_mapping": {
                    "header": [
                        {
                            "header_field_name": "headerFieldName",
                            "target_property_name": "targetPropertyName"
                        }
                    ]
                },
                "response_profile": "responseProfile",
                "response_profile_type": "NONE",
                "return_errors": True,
                "use_default_options": True
            },
            "http_listen_options": {
                "mime_passthrough": True,
                "object_name": "objectName",
                "operation_type": "operationType",
                "password": "password",
                "use_default_listen_options": False,
                "username": "username"
            },
            "http_send_options": {
                "data_content_type": "dataContentType",
                "follow_redirects": True,
                "method_type": "GET",
                "path_elements": {
                    "element": [
                        {
                            "name": "name"
                        }
                    ]
                },
                "reflect_headers": {
                    "element": [
                        {
                            "name": "name"
                        }
                    ]
                },
                "request_headers": {
                    "header": [
                        {
                            "header_field_name": "headerFieldName",
                            "target_property_name": "targetPropertyName"
                        }
                    ]
                },
                "request_profile": "requestProfile",
                "request_profile_type": "NONE",
                "response_header_mapping": {
                    "header": [
                        {
                            "header_field_name": "headerFieldName",
                            "target_property_name": "targetPropertyName"
                        }
                    ]
                },
                "response_profile": "responseProfile",
                "response_profile_type": "NONE",
                "return_errors": False,
                "return_responses": False,
                "use_default_options": False
            },
            "http_settings": {
                "http_auth_settings": {
                    "password": "password",
                    "user": "user"
                },
                "httpo_auth2_settings": {
                    "access_token_endpoint": {
                        "ssl_options": {
                            "clientauth": False,
                            "clientsslalias": "clientsslalias",
                            "trust_server_cert": False,
                            "trustedcertalias": "trustedcertalias"
                        },
                        "url": "url"
                    },
                    "access_token_parameters": {
                        "parameter": [
                            {
                                "name": "name",
                                "value": "value"
                            }
                        ]
                    },
                    "authorization_parameters": {
                        "parameter": [
                            {
                                "name": "name",
                                "value": "value"
                            }
                        ]
                    },
                    "authorization_token_endpoint": {
                        "ssl_options": {
                            "clientauth": False,
                            "clientsslalias": "clientsslalias",
                            "trust_server_cert": False,
                            "trustedcertalias": "trustedcertalias"
                        },
                        "url": "url"
                    },
                    "credentials": {
                        "access_token": "accessToken",
                        "access_token_key": "accessTokenKey",
                        "client_id": "clientId",
                        "client_secret": "clientSecret",
                        "use_refresh_token": True
                    },
                    "grant_type": "code",
                    "scope": "scope"
                },
                "httpo_auth_settings": {
                    "access_token": "accessToken",
                    "access_token_url": "accessTokenURL",
                    "authorization_url": "authorizationURL",
                    "consumer_key": "consumerKey",
                    "consumer_secret": "consumerSecret",
                    "realm": "realm",
                    "request_token_url": "requestTokenURL",
                    "signature_method": "SHA1",
                    "suppress_blank_access_token": True,
                    "token_secret": "tokenSecret"
                },
                "httpssl_options": {
                    "clientauth": False,
                    "clientsslalias": "clientsslalias",
                    "trust_server_cert": False,
                    "trustedcertalias": "trustedcertalias"
                },
                "authentication_type": "NONE",
                "connect_timeout": 3,
                "cookie_scope": "IGNORED",
                "read_timeout": 2,
                "url": "url",
                "use_basic_auth": False,
                "use_custom_auth": False,
                "use_default_settings": False
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "mllp_communication_options": {
            "mllp_send_settings": {
                "mllpssl_options": {
                    "client_ssl_alias": "clientSSLAlias",
                    "ssl_alias": "sslAlias",
                    "use_client_ssl": True,
                    "use_ssl": True
                },
                "end_block": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "end_data": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "halt_timeout": False,
                "host": "host",
                "inactivity_timeout": 60,
                "max_connections": 10,
                "max_retry": 8,
                "persistent": False,
                "port": 7,
                "receive_timeout": 120,
                "send_timeout": 120,
                "start_block": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                }
            }
        },
        "oftp_communication_options": {
            "communication_setting": "default",
            "oftp_connection_settings": {
                "client_ssl_alias": "clientSSLAlias",
                "default_oftp_connection_settings": {
                    "client_ssl_alias": "clientSSLAlias",
                    "host": "host",
                    "my_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    },
                    "port": 8,
                    "sfidciph": 4,
                    "ssidauth": False,
                    "tls": False,
                    "use_client_ssl": True,
                    "use_gateway": False
                },
                "host": "host",
                "my_partner_info": {
                    "client_ssl_alias": "clientSSLAlias",
                    "encrypting_certificate": "encrypting-certificate",
                    "session_challenge_certificate": "session-challenge-certificate",
                    "sfidsec_encrypt": True,
                    "sfidsec_sign": True,
                    "sfidsign": False,
                    "ssidcmpr": True,
                    "ssidcode": "ssidcode",
                    "ssidpswd": "ssidpswd",
                    "verifying_eerp_certificate": "verifying-eerp-certificate",
                    "verifying_signature_certificate": "verifying-signature-certificate"
                },
                "port": 4,
                "sfidciph": 5,
                "ssidauth": False,
                "tls": False,
                "use_client_ssl": True,
                "use_gateway": False
            },
            "oftp_get_options": {
                "oftp_partner_group": {
                    "default_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    },
                    "my_company_info": {
                        "decrypting_certificate": "decrypting-certificate",
                        "session_authentication_certificate": "session-authentication-certificate",
                        "signing_certificate": "signing-certificate",
                        "signing_eerp_certificate": "signing-eerp-certificate",
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd"
                    },
                    "my_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    }
                },
                "partner_group_id": "partnerGroupId"
            },
            "oftp_send_options": {
                "oftp_partner_group": {
                    "default_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    },
                    "my_company_info": {
                        "decrypting_certificate": "decrypting-certificate",
                        "session_authentication_certificate": "session-authentication-certificate",
                        "signing_certificate": "signing-certificate",
                        "signing_eerp_certificate": "signing-eerp-certificate",
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd"
                    },
                    "my_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    }
                },
                "oftp_send_options": {
                    "cd": False,
                    "default_partner_settings": {
                        "cd": False,
                        "operation": "operation",
                        "sfiddesc": "sfiddesc",
                        "sfiddsn": "sfiddsn"
                    },
                    "operation": "operation",
                    "sfiddesc": "sfiddesc",
                    "sfiddsn": "sfiddsn"
                },
                "partner_group_id": "partnerGroupId"
            },
            "oftp_server_listen_options": {
                "oftp_listen_options": {
                    "gateway_partner_group": {
                        "default_partner_info": {
                            "client_ssl_alias": "clientSSLAlias",
                            "encrypting_certificate": "encrypting-certificate",
                            "session_challenge_certificate": "session-challenge-certificate",
                            "sfidsec_encrypt": True,
                            "sfidsec_sign": True,
                            "sfidsign": False,
                            "ssidcmpr": True,
                            "ssidcode": "ssidcode",
                            "ssidpswd": "ssidpswd",
                            "verifying_eerp_certificate": "verifying-eerp-certificate",
                            "verifying_signature_certificate": "verifying-signature-certificate"
                        },
                        "my_company_info": {
                            "decrypting_certificate": "decrypting-certificate",
                            "session_authentication_certificate": "session-authentication-certificate",
                            "signing_certificate": "signing-certificate",
                            "signing_eerp_certificate": "signing-eerp-certificate",
                            "ssidcode": "ssidcode",
                            "ssidpswd": "ssidpswd"
                        },
                        "my_partner_info": {
                            "client_ssl_alias": "clientSSLAlias",
                            "encrypting_certificate": "encrypting-certificate",
                            "session_challenge_certificate": "session-challenge-certificate",
                            "sfidsec_encrypt": True,
                            "sfidsec_sign": True,
                            "sfidsign": False,
                            "ssidcmpr": True,
                            "ssidcode": "ssidcode",
                            "ssidpswd": "ssidpswd",
                            "verifying_eerp_certificate": "verifying-eerp-certificate",
                            "verifying_signature_certificate": "verifying-signature-certificate"
                        }
                    },
                    "operation": "operation",
                    "use_gateway": False
                },
                "oftp_partner_group": {
                    "default_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    },
                    "my_company_info": {
                        "decrypting_certificate": "decrypting-certificate",
                        "session_authentication_certificate": "session-authentication-certificate",
                        "signing_certificate": "signing-certificate",
                        "signing_eerp_certificate": "signing-eerp-certificate",
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd"
                    },
                    "my_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    }
                },
                "partner_group_id": "partnerGroupId"
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "sftp_communication_options": {
            "communication_setting": "default",
            "sftp_get_options": {
                "file_to_move": "fileToMove",
                "ftp_action": "actionget",
                "max_file_count": 2,
                "move_to_directory": "moveToDirectory",
                "move_to_force_override": True,
                "remote_directory": "remoteDirectory",
                "use_default_get_options": True
            },
            "sftp_send_options": {
                "ftp_action": "actionputrename",
                "move_to_directory": "moveToDirectory",
                "move_to_force_override": True,
                "remote_directory": "remoteDirectory",
                "use_default_send_options": False
            },
            "sftp_settings": {
                "sftp_proxy_settings": {
                    "host": "host",
                    "password": "password",
                    "port": 5,
                    "proxy_enabled": True,
                    "type_": "ATOM",
                    "user": "user"
                },
                "sftpssh_options": {
                    "dh_key_size_max1024": False,
                    "known_host_entry": "knownHostEntry",
                    "sshkeyauth": False,
                    "sshkeypassword": "sshkeypassword",
                    "sshkeypath": "sshkeypath"
                },
                "host": "host",
                "password": "password",
                "port": 4,
                "use_default_settings": False,
                "user": "user"
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        }
    },
    partner_communication_types=[
        "PartnerCommunicationTypes"
    ],
    partner_document_types={
        "partner_document_type": [
            {
                "expect_ack_for_outbound": False,
                "invalid_document_routing": "documentsPath",
                "name": "name",
                "profile_id": "profileId",
                "qualifier_validation": True,
                "type_id": "typeId",
                "use999_ack": False,
                "use_ta1_ack": True,
                "validate_outbound_transaction_sets": True
            }
        ]
    },
    partner_info={
        "custom_partner_info": {},
        "edifact_partner_info": {
            "edifact_control_info": {
                "unb_control_info": {
                    "ack_request": False,
                    "app_reference": "appReference",
                    "comm_agreement": "commAgreement",
                    "interchange_address": "interchangeAddress",
                    "interchange_id": "interchangeId",
                    "interchange_id_qual": "EDIFACTIDQUAL_NA",
                    "interchange_sub_address": "interchangeSubAddress",
                    "priority": "NA",
                    "reference_password": "referencePassword",
                    "reference_password_qualifier": "NA",
                    "syntax_id": "UNOA",
                    "syntax_version": "EDIFACTSYNTAXVERSION_1",
                    "test_indicator": "EDIFACTTEST_NA"
                },
                "ung_control_info": {
                    "application_id": "applicationId",
                    "application_id_qual": "EDIFACTIDQUAL_NA",
                    "use_functional_groups": False
                },
                "unh_control_info": {
                    "assoc_assigned_code": "assocAssignedCode",
                    "common_access_ref": "commonAccessRef",
                    "controlling_agency": "AA",
                    "release": "EDIFACTRELEASE_1",
                    "version": "EDIFACTVERSION_1"
                }
            },
            "edifact_options": {
                "acknowledgementoption": "donotackitem",
                "composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "envelopeoption": "groupall",
                "filteracknowledgements": False,
                "include_una": True,
                "outbound_interchange_validation": False,
                "outbound_validation_option": "filterError",
                "reject_duplicate_unb": False,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                }
            }
        },
        "hl7_partner_info": {
            "hl7_control_info": {
                "msh_control_info": {
                    "application": {
                        "namespace_id": "namespaceId",
                        "universal_id": "universalId",
                        "universal_id_type": "universalIdType"
                    },
                    "facility": {
                        "namespace_id": "namespaceId",
                        "universal_id": "universalId",
                        "universal_id_type": "universalIdType"
                    },
                    "network_address": {
                        "namespace_id": "namespaceId",
                        "universal_id": "universalId",
                        "universal_id_type": "universalIdType"
                    },
                    "processing_id": {
                        "processing_id": "D",
                        "processing_mode": "A"
                    }
                }
            },
            "hl7_options": {
                "acceptackoption": "AL",
                "appackoption": "AL",
                "batchoption": "none",
                "composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "filteracknowledgements": True,
                "outbound_interchange_validation": True,
                "outbound_validation_option": "filterError",
                "reject_duplicates": False,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                },
                "sub_composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                }
            }
        },
        "odette_partner_info": {
            "odette_control_info": {
                "odette_unb_control_info": {
                    "ack_request": False,
                    "app_reference": "appReference",
                    "comm_agreement": "commAgreement",
                    "interchange_address": "interchangeAddress",
                    "interchange_id": "interchangeId",
                    "interchange_id_qual": "ODETTEIDQUAL_NA",
                    "interchange_sub_address": "interchangeSubAddress",
                    "priority": "NA",
                    "reference_password": "referencePassword",
                    "reference_password_qualifier": "NA",
                    "syntax_id": "UNOA",
                    "syntax_version": "ODETTESYNTAXVERSION_1",
                    "test_indicator": "ODETTETEST_NA"
                },
                "odette_unh_control_info": {
                    "assoc_assigned_code": "assocAssignedCode",
                    "common_access_ref": "commonAccessRef",
                    "controlling_agency": "AA",
                    "release": "ODETTERELEASE_1",
                    "version": "ODETTEVERSION_1"
                }
            },
            "odette_options": {
                "acknowledgementoption": "donotackitem",
                "composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "envelopeoption": "groupall",
                "filteracknowledgements": False,
                "include_una": True,
                "outbound_interchange_validation": False,
                "outbound_validation_option": "filterError",
                "reject_duplicate_unb": True,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                }
            }
        },
        "rosetta_net_partner_info": {
            "rosetta_net_control_info": {
                "encryption_public_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId"
                },
                "global_partner_classification_code": "globalPartnerClassificationCode",
                "global_usage_code": "Test",
                "partner_id": "partnerId",
                "partner_id_type": "DUNS",
                "partner_location": "partnerLocation",
                "signing_public_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId"
                },
                "supply_chain_code": "supplyChainCode"
            },
            "rosetta_net_message_options": {
                "attachment_cache": "attachmentCache",
                "compressed": False,
                "content_transfer_encoding": "binary",
                "encrypt_service_header": True,
                "encrypted": True,
                "encryption_algorithm": "na",
                "signature_digest_algorithm": "SHA1",
                "signed": True
            },
            "rosetta_net_options": {
                "filter_signals": True,
                "outbound_document_validation": False,
                "reject_duplicate_transactions": True,
                "version": "v11"
            }
        },
        "tradacoms_partner_info": {
            "tradacoms_control_info": {
                "stx_control_info": {
                    "interchange_id": "interchangeId",
                    "interchange_id_qualifier": "interchangeIdQualifier"
                }
            },
            "tradacoms_options": {
                "composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "filter_acknowledgements": True,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                },
                "use_reconciliation_message": True
            }
        },
        "x12_partner_info": {
            "x12_control_info": {
                "gs_control_info": {
                    "applicationcode": "applicationcode",
                    "gs_version": "gsVersion",
                    "respagencycode": "T"
                },
                "isa_control_info": {
                    "ackrequested": False,
                    "authorization_information": "authorizationInformation",
                    "authorization_information_qualifier": "X12AUTHQUAL_00",
                    "component_element_separator": "componentElementSeparator",
                    "interchange_id": "interchangeId",
                    "interchange_id_qualifier": "X12IDQUAL_01",
                    "security_information": "securityInformation",
                    "security_information_qualifier": "X12SECQUAL_00",
                    "standard_identification": "standardIdentification",
                    "testindicator": "P",
                    "version": "version"
                }
            },
            "x12_options": {
                "acknowledgementoption": "donotackitem",
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "envelopeoption": "groupall",
                "filteracknowledgements": False,
                "outbound_interchange_validation": False,
                "outbound_validation_option": "filterError",
                "reject_duplicate_interchange": False,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                }
            }
        }
    },
    classification="tradingpartner",
    component_id="12345678-9abc-def0-1234-56789abcdef0",
    component_name="Best Wholesaling",
    deleted=True,
    description="description",
    folder_id="11356",
    folder_name="Home:TPs",
    identifier="identifier",
    organization_id="organizationId",
    standard="x12"
)

result = sdk.trading_partner_component.create_trading_partner_component(request_body=request_body)

print(result)
```

## get_trading_partner_component

The ordinary GET operation returns a single Trading Partner Component object based on the supplied ID. A GET operation specifying the ID of a deleted Trading Partner component retrieves the component. In the component, the deleted field’s value is true.

- HTTP Method: `GET`
- Endpoint: `/TradingPartnerComponent/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`TradingPartnerComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.trading_partner_component.get_trading_partner_component(id_="id")

print(result)
```

## update_trading_partner_component

This operation overwrites the Trading Partner Component object with the specified component ID except as described: - If the fields are empty, an UPDATE operation specifying the organizationId field populates the ContactInformation fields with the data from the referenced Organization component. However, if those fields have values, they are not overwritten. An UPDATE operation specifying the ID of a deleted Trading Partner component restores the component to a non-deleted state, assuming the request is otherwise valid.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/{id}`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [TradingPartnerComponent](../models/TradingPartnerComponent.md) | ❌       | The request body. |
| id\_         | str                                                             | ✅       |                   |

**Return Type**

`TradingPartnerComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerComponent

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerComponent(
    contact_info={
        "address1": "address1",
        "address2": "address2",
        "city": "city",
        "contact_name": "contactName",
        "country": "country",
        "email": "email",
        "fax": "fax",
        "phone": "phone",
        "postalcode": "postalcode",
        "state": "state"
    },
    partner_communication={
        "as2_communication_options": {
            "as2_default_partner_settings": {
                "auth_settings": {
                    "password": "password",
                    "user": "user"
                },
                "authentication_type": "NONE",
                "client_ssl_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId",
                    "pass_phrase": "passPhrase"
                },
                "ssl_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId"
                },
                "url": "url",
                "use_default_settings": False,
                "verify_hostname": False
            },
            "as2_receive_options": {
                "as2_default_partner_info": {
                    "listen_attachment_settings": {
                        "attachment_cache": "attachmentCache",
                        "attachment_content_type": [
                            "application/xml"
                        ],
                        "multiple_attachments": False
                    },
                    "listen_auth_settings": {
                        "password": "password",
                        "user": "user"
                    },
                    "as2_id": "as2Id",
                    "basic_auth_enabled": True,
                    "client_ssl_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "enabled_legacy_smime": False,
                    "encryption_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "mdn_signature_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "messages_to_check_for_duplicates": 0,
                    "reject_duplicate_messages": False,
                    "signing_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    }
                },
                "as2_default_partner_mdn_options": {
                    "external_url": "externalURL",
                    "mdn_client_ssl_cert": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "mdn_digest_alg": "SHA1",
                    "mdn_ssl_cert": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "request_mdn": True,
                    "signed": True,
                    "synchronous": "sync",
                    "use_external_url": False,
                    "use_ssl": False
                },
                "as2_default_partner_message_options": {
                    "attachment_cache": "attachmentCache",
                    "attachment_option": "BATCH",
                    "compressed": True,
                    "data_content_type": "textplain",
                    "encrypted": True,
                    "encryption_algorithm": "na",
                    "max_document_count": 4,
                    "multiple_attachments": True,
                    "signed": True,
                    "signing_digest_alg": "SHA1",
                    "subject": "subject"
                },
                "as2_my_company_info": {
                    "as2_id": "as2Id",
                    "enabled_legacy_smime": False,
                    "encryption_private_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "mdn_signature_private_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "signing_private_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    }
                }
            },
            "as2_send_options": {
                "as2_mdn_options": {
                    "external_url": "externalURL",
                    "mdn_client_ssl_cert": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "mdn_digest_alg": "SHA1",
                    "mdn_ssl_cert": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "request_mdn": True,
                    "signed": True,
                    "synchronous": "sync",
                    "use_external_url": False,
                    "use_ssl": False
                },
                "as2_message_options": {
                    "attachment_cache": "attachmentCache",
                    "attachment_option": "BATCH",
                    "compressed": True,
                    "data_content_type": "textplain",
                    "encrypted": True,
                    "encryption_algorithm": "na",
                    "max_document_count": 4,
                    "multiple_attachments": True,
                    "signed": True,
                    "signing_digest_alg": "SHA1",
                    "subject": "subject"
                },
                "as2_partner_info": {
                    "listen_attachment_settings": {
                        "attachment_cache": "attachmentCache",
                        "attachment_content_type": [
                            "application/xml"
                        ],
                        "multiple_attachments": False
                    },
                    "listen_auth_settings": {
                        "password": "password",
                        "user": "user"
                    },
                    "as2_id": "as2Id",
                    "basic_auth_enabled": True,
                    "client_ssl_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "enabled_legacy_smime": False,
                    "encryption_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "mdn_signature_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    },
                    "messages_to_check_for_duplicates": 0,
                    "reject_duplicate_messages": False,
                    "signing_public_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId"
                    }
                }
            },
            "as2_send_settings": {
                "auth_settings": {
                    "password": "password",
                    "user": "user"
                },
                "authentication_type": "NONE",
                "client_ssl_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId",
                    "pass_phrase": "passPhrase"
                },
                "ssl_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId"
                },
                "url": "url",
                "use_default_settings": False,
                "verify_hostname": False
            },
            "communication_setting": "default",
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "disk_communication_options": {
            "communication_setting": "default",
            "disk_get_options": {
                "delete_after_read": False,
                "file_filter": "fileFilter",
                "filter_match_type": "wildcard",
                "get_directory": "getDirectory",
                "max_file_count": 2,
                "use_default_get_options": True
            },
            "disk_send_options": {
                "create_directory": False,
                "send_directory": "sendDirectory",
                "use_default_send_options": True,
                "write_option": "unique"
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "ftp_communication_options": {
            "communication_setting": "default",
            "ftp_get_options": {
                "file_to_move": "fileToMove",
                "ftp_action": "actionget",
                "max_file_count": 1,
                "remote_directory": "remoteDirectory",
                "transfer_type": "ascii",
                "use_default_get_options": True
            },
            "ftp_send_options": {
                "ftp_action": "actionputrename",
                "move_to_directory": "moveToDirectory",
                "remote_directory": "remoteDirectory",
                "transfer_type": "ascii",
                "use_default_send_options": True
            },
            "ftp_settings": {
                "ftpssl_options": {
                    "client_ssl_certificate": {
                        "alias": "alias",
                        "certificate": [
                            "certificate"
                        ],
                        "component_id": "componentId",
                        "pass_phrase": "passPhrase"
                    },
                    "sslmode": "none",
                    "use_client_authentication": True
                },
                "connection_mode": "active",
                "host": "host",
                "password": "password",
                "port": 1,
                "use_default_settings": True,
                "user": "user"
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "http_communication_options": {
            "communication_setting": "default",
            "http_get_options": {
                "data_content_type": "dataContentType",
                "follow_redirects": True,
                "method_type": "GET",
                "path_elements": {
                    "element": [
                        {
                            "name": "name"
                        }
                    ]
                },
                "reflect_headers": {
                    "element": [
                        {
                            "name": "name"
                        }
                    ]
                },
                "request_headers": {
                    "header": [
                        {
                            "header_field_name": "headerFieldName",
                            "target_property_name": "targetPropertyName"
                        }
                    ]
                },
                "request_profile": "requestProfile",
                "request_profile_type": "NONE",
                "response_header_mapping": {
                    "header": [
                        {
                            "header_field_name": "headerFieldName",
                            "target_property_name": "targetPropertyName"
                        }
                    ]
                },
                "response_profile": "responseProfile",
                "response_profile_type": "NONE",
                "return_errors": True,
                "use_default_options": True
            },
            "http_listen_options": {
                "mime_passthrough": True,
                "object_name": "objectName",
                "operation_type": "operationType",
                "password": "password",
                "use_default_listen_options": False,
                "username": "username"
            },
            "http_send_options": {
                "data_content_type": "dataContentType",
                "follow_redirects": True,
                "method_type": "GET",
                "path_elements": {
                    "element": [
                        {
                            "name": "name"
                        }
                    ]
                },
                "reflect_headers": {
                    "element": [
                        {
                            "name": "name"
                        }
                    ]
                },
                "request_headers": {
                    "header": [
                        {
                            "header_field_name": "headerFieldName",
                            "target_property_name": "targetPropertyName"
                        }
                    ]
                },
                "request_profile": "requestProfile",
                "request_profile_type": "NONE",
                "response_header_mapping": {
                    "header": [
                        {
                            "header_field_name": "headerFieldName",
                            "target_property_name": "targetPropertyName"
                        }
                    ]
                },
                "response_profile": "responseProfile",
                "response_profile_type": "NONE",
                "return_errors": False,
                "return_responses": False,
                "use_default_options": False
            },
            "http_settings": {
                "http_auth_settings": {
                    "password": "password",
                    "user": "user"
                },
                "httpo_auth2_settings": {
                    "access_token_endpoint": {
                        "ssl_options": {
                            "clientauth": False,
                            "clientsslalias": "clientsslalias",
                            "trust_server_cert": False,
                            "trustedcertalias": "trustedcertalias"
                        },
                        "url": "url"
                    },
                    "access_token_parameters": {
                        "parameter": [
                            {
                                "name": "name",
                                "value": "value"
                            }
                        ]
                    },
                    "authorization_parameters": {
                        "parameter": [
                            {
                                "name": "name",
                                "value": "value"
                            }
                        ]
                    },
                    "authorization_token_endpoint": {
                        "ssl_options": {
                            "clientauth": False,
                            "clientsslalias": "clientsslalias",
                            "trust_server_cert": False,
                            "trustedcertalias": "trustedcertalias"
                        },
                        "url": "url"
                    },
                    "credentials": {
                        "access_token": "accessToken",
                        "access_token_key": "accessTokenKey",
                        "client_id": "clientId",
                        "client_secret": "clientSecret",
                        "use_refresh_token": True
                    },
                    "grant_type": "code",
                    "scope": "scope"
                },
                "httpo_auth_settings": {
                    "access_token": "accessToken",
                    "access_token_url": "accessTokenURL",
                    "authorization_url": "authorizationURL",
                    "consumer_key": "consumerKey",
                    "consumer_secret": "consumerSecret",
                    "realm": "realm",
                    "request_token_url": "requestTokenURL",
                    "signature_method": "SHA1",
                    "suppress_blank_access_token": True,
                    "token_secret": "tokenSecret"
                },
                "httpssl_options": {
                    "clientauth": False,
                    "clientsslalias": "clientsslalias",
                    "trust_server_cert": False,
                    "trustedcertalias": "trustedcertalias"
                },
                "authentication_type": "NONE",
                "connect_timeout": 3,
                "cookie_scope": "IGNORED",
                "read_timeout": 2,
                "url": "url",
                "use_basic_auth": False,
                "use_custom_auth": False,
                "use_default_settings": False
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "mllp_communication_options": {
            "mllp_send_settings": {
                "mllpssl_options": {
                    "client_ssl_alias": "clientSSLAlias",
                    "ssl_alias": "sslAlias",
                    "use_client_ssl": True,
                    "use_ssl": True
                },
                "end_block": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "end_data": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "halt_timeout": False,
                "host": "host",
                "inactivity_timeout": 60,
                "max_connections": 10,
                "max_retry": 8,
                "persistent": False,
                "port": 7,
                "receive_timeout": 120,
                "send_timeout": 120,
                "start_block": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                }
            }
        },
        "oftp_communication_options": {
            "communication_setting": "default",
            "oftp_connection_settings": {
                "client_ssl_alias": "clientSSLAlias",
                "default_oftp_connection_settings": {
                    "client_ssl_alias": "clientSSLAlias",
                    "host": "host",
                    "my_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    },
                    "port": 8,
                    "sfidciph": 4,
                    "ssidauth": False,
                    "tls": False,
                    "use_client_ssl": True,
                    "use_gateway": False
                },
                "host": "host",
                "my_partner_info": {
                    "client_ssl_alias": "clientSSLAlias",
                    "encrypting_certificate": "encrypting-certificate",
                    "session_challenge_certificate": "session-challenge-certificate",
                    "sfidsec_encrypt": True,
                    "sfidsec_sign": True,
                    "sfidsign": False,
                    "ssidcmpr": True,
                    "ssidcode": "ssidcode",
                    "ssidpswd": "ssidpswd",
                    "verifying_eerp_certificate": "verifying-eerp-certificate",
                    "verifying_signature_certificate": "verifying-signature-certificate"
                },
                "port": 4,
                "sfidciph": 5,
                "ssidauth": False,
                "tls": False,
                "use_client_ssl": True,
                "use_gateway": False
            },
            "oftp_get_options": {
                "oftp_partner_group": {
                    "default_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    },
                    "my_company_info": {
                        "decrypting_certificate": "decrypting-certificate",
                        "session_authentication_certificate": "session-authentication-certificate",
                        "signing_certificate": "signing-certificate",
                        "signing_eerp_certificate": "signing-eerp-certificate",
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd"
                    },
                    "my_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    }
                },
                "partner_group_id": "partnerGroupId"
            },
            "oftp_send_options": {
                "oftp_partner_group": {
                    "default_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    },
                    "my_company_info": {
                        "decrypting_certificate": "decrypting-certificate",
                        "session_authentication_certificate": "session-authentication-certificate",
                        "signing_certificate": "signing-certificate",
                        "signing_eerp_certificate": "signing-eerp-certificate",
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd"
                    },
                    "my_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    }
                },
                "oftp_send_options": {
                    "cd": False,
                    "default_partner_settings": {
                        "cd": False,
                        "operation": "operation",
                        "sfiddesc": "sfiddesc",
                        "sfiddsn": "sfiddsn"
                    },
                    "operation": "operation",
                    "sfiddesc": "sfiddesc",
                    "sfiddsn": "sfiddsn"
                },
                "partner_group_id": "partnerGroupId"
            },
            "oftp_server_listen_options": {
                "oftp_listen_options": {
                    "gateway_partner_group": {
                        "default_partner_info": {
                            "client_ssl_alias": "clientSSLAlias",
                            "encrypting_certificate": "encrypting-certificate",
                            "session_challenge_certificate": "session-challenge-certificate",
                            "sfidsec_encrypt": True,
                            "sfidsec_sign": True,
                            "sfidsign": False,
                            "ssidcmpr": True,
                            "ssidcode": "ssidcode",
                            "ssidpswd": "ssidpswd",
                            "verifying_eerp_certificate": "verifying-eerp-certificate",
                            "verifying_signature_certificate": "verifying-signature-certificate"
                        },
                        "my_company_info": {
                            "decrypting_certificate": "decrypting-certificate",
                            "session_authentication_certificate": "session-authentication-certificate",
                            "signing_certificate": "signing-certificate",
                            "signing_eerp_certificate": "signing-eerp-certificate",
                            "ssidcode": "ssidcode",
                            "ssidpswd": "ssidpswd"
                        },
                        "my_partner_info": {
                            "client_ssl_alias": "clientSSLAlias",
                            "encrypting_certificate": "encrypting-certificate",
                            "session_challenge_certificate": "session-challenge-certificate",
                            "sfidsec_encrypt": True,
                            "sfidsec_sign": True,
                            "sfidsign": False,
                            "ssidcmpr": True,
                            "ssidcode": "ssidcode",
                            "ssidpswd": "ssidpswd",
                            "verifying_eerp_certificate": "verifying-eerp-certificate",
                            "verifying_signature_certificate": "verifying-signature-certificate"
                        }
                    },
                    "operation": "operation",
                    "use_gateway": False
                },
                "oftp_partner_group": {
                    "default_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    },
                    "my_company_info": {
                        "decrypting_certificate": "decrypting-certificate",
                        "session_authentication_certificate": "session-authentication-certificate",
                        "signing_certificate": "signing-certificate",
                        "signing_eerp_certificate": "signing-eerp-certificate",
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd"
                    },
                    "my_partner_info": {
                        "client_ssl_alias": "clientSSLAlias",
                        "encrypting_certificate": "encrypting-certificate",
                        "session_challenge_certificate": "session-challenge-certificate",
                        "sfidsec_encrypt": True,
                        "sfidsec_sign": True,
                        "sfidsign": False,
                        "ssidcmpr": True,
                        "ssidcode": "ssidcode",
                        "ssidpswd": "ssidpswd",
                        "verifying_eerp_certificate": "verifying-eerp-certificate",
                        "verifying_signature_certificate": "verifying-signature-certificate"
                    }
                },
                "partner_group_id": "partnerGroupId"
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        },
        "sftp_communication_options": {
            "communication_setting": "default",
            "sftp_get_options": {
                "file_to_move": "fileToMove",
                "ftp_action": "actionget",
                "max_file_count": 2,
                "move_to_directory": "moveToDirectory",
                "move_to_force_override": True,
                "remote_directory": "remoteDirectory",
                "use_default_get_options": True
            },
            "sftp_send_options": {
                "ftp_action": "actionputrename",
                "move_to_directory": "moveToDirectory",
                "move_to_force_override": True,
                "remote_directory": "remoteDirectory",
                "use_default_send_options": False
            },
            "sftp_settings": {
                "sftp_proxy_settings": {
                    "host": "host",
                    "password": "password",
                    "port": 5,
                    "proxy_enabled": True,
                    "type_": "ATOM",
                    "user": "user"
                },
                "sftpssh_options": {
                    "dh_key_size_max1024": False,
                    "known_host_entry": "knownHostEntry",
                    "sshkeyauth": False,
                    "sshkeypassword": "sshkeypassword",
                    "sshkeypath": "sshkeypath"
                },
                "host": "host",
                "password": "password",
                "port": 4,
                "use_default_settings": False,
                "user": "user"
            },
            "shared_communication_channel": {
                "component_id": "componentId"
            }
        }
    },
    partner_communication_types=[
        "PartnerCommunicationTypes"
    ],
    partner_document_types={
        "partner_document_type": [
            {
                "expect_ack_for_outbound": False,
                "invalid_document_routing": "documentsPath",
                "name": "name",
                "profile_id": "profileId",
                "qualifier_validation": True,
                "type_id": "typeId",
                "use999_ack": False,
                "use_ta1_ack": True,
                "validate_outbound_transaction_sets": True
            }
        ]
    },
    partner_info={
        "custom_partner_info": {},
        "edifact_partner_info": {
            "edifact_control_info": {
                "unb_control_info": {
                    "ack_request": False,
                    "app_reference": "appReference",
                    "comm_agreement": "commAgreement",
                    "interchange_address": "interchangeAddress",
                    "interchange_id": "interchangeId",
                    "interchange_id_qual": "EDIFACTIDQUAL_NA",
                    "interchange_sub_address": "interchangeSubAddress",
                    "priority": "NA",
                    "reference_password": "referencePassword",
                    "reference_password_qualifier": "NA",
                    "syntax_id": "UNOA",
                    "syntax_version": "EDIFACTSYNTAXVERSION_1",
                    "test_indicator": "EDIFACTTEST_NA"
                },
                "ung_control_info": {
                    "application_id": "applicationId",
                    "application_id_qual": "EDIFACTIDQUAL_NA",
                    "use_functional_groups": False
                },
                "unh_control_info": {
                    "assoc_assigned_code": "assocAssignedCode",
                    "common_access_ref": "commonAccessRef",
                    "controlling_agency": "AA",
                    "release": "EDIFACTRELEASE_1",
                    "version": "EDIFACTVERSION_1"
                }
            },
            "edifact_options": {
                "acknowledgementoption": "donotackitem",
                "composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "envelopeoption": "groupall",
                "filteracknowledgements": False,
                "include_una": True,
                "outbound_interchange_validation": False,
                "outbound_validation_option": "filterError",
                "reject_duplicate_unb": False,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                }
            }
        },
        "hl7_partner_info": {
            "hl7_control_info": {
                "msh_control_info": {
                    "application": {
                        "namespace_id": "namespaceId",
                        "universal_id": "universalId",
                        "universal_id_type": "universalIdType"
                    },
                    "facility": {
                        "namespace_id": "namespaceId",
                        "universal_id": "universalId",
                        "universal_id_type": "universalIdType"
                    },
                    "network_address": {
                        "namespace_id": "namespaceId",
                        "universal_id": "universalId",
                        "universal_id_type": "universalIdType"
                    },
                    "processing_id": {
                        "processing_id": "D",
                        "processing_mode": "A"
                    }
                }
            },
            "hl7_options": {
                "acceptackoption": "AL",
                "appackoption": "AL",
                "batchoption": "none",
                "composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "filteracknowledgements": True,
                "outbound_interchange_validation": True,
                "outbound_validation_option": "filterError",
                "reject_duplicates": False,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                },
                "sub_composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                }
            }
        },
        "odette_partner_info": {
            "odette_control_info": {
                "odette_unb_control_info": {
                    "ack_request": False,
                    "app_reference": "appReference",
                    "comm_agreement": "commAgreement",
                    "interchange_address": "interchangeAddress",
                    "interchange_id": "interchangeId",
                    "interchange_id_qual": "ODETTEIDQUAL_NA",
                    "interchange_sub_address": "interchangeSubAddress",
                    "priority": "NA",
                    "reference_password": "referencePassword",
                    "reference_password_qualifier": "NA",
                    "syntax_id": "UNOA",
                    "syntax_version": "ODETTESYNTAXVERSION_1",
                    "test_indicator": "ODETTETEST_NA"
                },
                "odette_unh_control_info": {
                    "assoc_assigned_code": "assocAssignedCode",
                    "common_access_ref": "commonAccessRef",
                    "controlling_agency": "AA",
                    "release": "ODETTERELEASE_1",
                    "version": "ODETTEVERSION_1"
                }
            },
            "odette_options": {
                "acknowledgementoption": "donotackitem",
                "composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "envelopeoption": "groupall",
                "filteracknowledgements": False,
                "include_una": True,
                "outbound_interchange_validation": False,
                "outbound_validation_option": "filterError",
                "reject_duplicate_unb": True,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                }
            }
        },
        "rosetta_net_partner_info": {
            "rosetta_net_control_info": {
                "encryption_public_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId"
                },
                "global_partner_classification_code": "globalPartnerClassificationCode",
                "global_usage_code": "Test",
                "partner_id": "partnerId",
                "partner_id_type": "DUNS",
                "partner_location": "partnerLocation",
                "signing_public_certificate": {
                    "alias": "alias",
                    "certificate": [
                        "certificate"
                    ],
                    "component_id": "componentId"
                },
                "supply_chain_code": "supplyChainCode"
            },
            "rosetta_net_message_options": {
                "attachment_cache": "attachmentCache",
                "compressed": False,
                "content_transfer_encoding": "binary",
                "encrypt_service_header": True,
                "encrypted": True,
                "encryption_algorithm": "na",
                "signature_digest_algorithm": "SHA1",
                "signed": True
            },
            "rosetta_net_options": {
                "filter_signals": True,
                "outbound_document_validation": False,
                "reject_duplicate_transactions": True,
                "version": "v11"
            }
        },
        "tradacoms_partner_info": {
            "tradacoms_control_info": {
                "stx_control_info": {
                    "interchange_id": "interchangeId",
                    "interchange_id_qualifier": "interchangeIdQualifier"
                }
            },
            "tradacoms_options": {
                "composite_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "filter_acknowledgements": True,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                },
                "use_reconciliation_message": True
            }
        },
        "x12_partner_info": {
            "x12_control_info": {
                "gs_control_info": {
                    "applicationcode": "applicationcode",
                    "gs_version": "gsVersion",
                    "respagencycode": "T"
                },
                "isa_control_info": {
                    "ackrequested": False,
                    "authorization_information": "authorizationInformation",
                    "authorization_information_qualifier": "X12AUTHQUAL_00",
                    "component_element_separator": "componentElementSeparator",
                    "interchange_id": "interchangeId",
                    "interchange_id_qualifier": "X12IDQUAL_01",
                    "security_information": "securityInformation",
                    "security_information_qualifier": "X12SECQUAL_00",
                    "standard_identification": "standardIdentification",
                    "testindicator": "P",
                    "version": "version"
                }
            },
            "x12_options": {
                "acknowledgementoption": "donotackitem",
                "element_delimiter": {
                    "delimiter_special": "delimiterSpecial",
                    "delimiter_value": "stardelimited"
                },
                "envelopeoption": "groupall",
                "filteracknowledgements": False,
                "outbound_interchange_validation": False,
                "outbound_validation_option": "filterError",
                "reject_duplicate_interchange": False,
                "segment_terminator": {
                    "segment_terminator_special": "segmentTerminatorSpecial",
                    "segment_terminator_value": "newline"
                }
            }
        }
    },
    classification="tradingpartner",
    component_id="12345678-9abc-def0-1234-56789abcdef0",
    component_name="Best Wholesaling",
    deleted=True,
    description="description",
    folder_id="11356",
    folder_name="Home:TPs",
    identifier="identifier",
    organization_id="organizationId",
    standard="x12"
)

result = sdk.trading_partner_component.update_trading_partner_component(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_trading_partner_component

The DELETE operation deletes the Trading Partner Component object with a specific component ID. A DELETE operation specifying the ID of a deleted Trading Partner component returns a false response.

- HTTP Method: `DELETE`
- Endpoint: `/TradingPartnerComponent/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.trading_partner_component.delete_trading_partner_component(id_="id")

print(result)
```

## bulk_trading_partner_component

The bulk GET operation returns multiple Trading Partner Component objects based on the supplied IDs, to a maximum of 100.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/bulk`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [TradingPartnerComponentBulkRequest](../models/TradingPartnerComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`TradingPartnerComponentBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.trading_partner_component.bulk_trading_partner_component(request_body=request_body)

print(result)
```

## query_trading_partner_component

The QUERY operation returns each Trading Partner component that meets the specified filtering criteria. - The name field in a QUERY filter represents the object’s componentName field. - Only the LIKE operator is allowed with a name filter. Likewise, you can only use the EQUALS operator with a classification, standard, identifier filter, or a communication method filter (as2, disk, ftp, http, mllp, sftp). Filtering on a communication method field requests Trading Partner components by defining the communication method. - If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator. The QUERY request does not support the logical OR operator. - The QUERY results omit the folderName field. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/query`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [TradingPartnerComponentQueryConfig](../models/TradingPartnerComponentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`TradingPartnerComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerComponentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerComponentQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "name"
        }
    }
)

result = sdk.trading_partner_component.query_trading_partner_component(request_body=request_body)

print(result)
```

## query_more_trading_partner_component

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`TradingPartnerComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "sint esse l"

result = sdk.trading_partner_component.query_more_trading_partner_component(request_body=request_body)

print(result)
```

