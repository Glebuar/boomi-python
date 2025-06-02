# SharedCommunicationChannelComponentService

A list of all methods in the `SharedCommunicationChannelComponentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_shared_communication_channel_component](#create_shared_communication_channel_component)         | The sample request creates a Shared Communication Component named `Disk Comms Channel`.                                                                                                                                                                                                                                                                                                                                                                                         |
| [get_shared_communication_channel_component](#get_shared_communication_channel_component)               | Send an HTTP GET request where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the component being retrieved.                                                                                                                                                                                                                                                                                                            |
| [update_shared_communication_channel_component](#update_shared_communication_channel_component)         | The sample request updates the component named `Disk Comms Channel`.                                                                                                                                                                                                                                                                                                                                                                                                            |
| [delete_shared_communication_channel_component](#delete_shared_communication_channel_component)         | If the Shared Communication Channel component is deleted successfully, the response is `true`.                                                                                                                                                                                                                                                                                                                                                                                  |
| [bulk_shared_communication_channel_component](#bulk_shared_communication_channel_component)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                          |
| [query_shared_communication_channel_component](#query_shared_communication_channel_component)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). The sample request query returns the Shared Communication Channel components using the AS2 standard for the authenticating account. \>**Note:** The name field in a QUERY filter represents the object's `componentName` field. |
| [query_more_shared_communication_channel_component](#query_more_shared_communication_channel_component) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                  |

## create_shared_communication_channel_component

The sample request creates a Shared Communication Component named `Disk Comms Channel`.

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent`

**Parameters**

| Name         | Type                                                                                    | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [SharedCommunicationChannelComponent](../models/SharedCommunicationChannelComponent.md) | ❌       | The request body. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedCommunicationChannelComponent

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedCommunicationChannelComponent(
    partner_archiving={
        "enable_archiving": False,
        "inbound_directory": "inboundDirectory",
        "outbound_directory": "outboundDirectory"
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
    communication_type="AS2",
    component_id="0cfe0d5a-0d33-48f8-825a-1d67667e0cd5",
    component_name="Shared AS2 API",
    deleted=True,
    description="description",
    folder_id=921,
    folder_name="Boomi/SampleFolder"
)

result = sdk.shared_communication_channel_component.create_shared_communication_channel_component(request_body=request_body)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## get_shared_communication_channel_component

Send an HTTP GET request where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the component being retrieved.

- HTTP Method: `GET`
- Endpoint: `/SharedCommunicationChannelComponent/{id}`

**Parameters**

| Name | Type | Required | Description                          |
| :--- | :--- | :------- | :----------------------------------- |
| id\_ | str  | ✅       | ID of the component being retrieved. |

**Return Type**

`SharedCommunicationChannelComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.shared_communication_channel_component.get_shared_communication_channel_component(id_="id")

print(result)
```

## update_shared_communication_channel_component

The sample request updates the component named `Disk Comms Channel`.

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/{id}`

**Parameters**

| Name         | Type                                                                                    | Required | Description                              |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :--------------------------------------- |
| request_body | [SharedCommunicationChannelComponent](../models/SharedCommunicationChannelComponent.md) | ❌       | The request body.                        |
| id\_         | str                                                                                     | ✅       | ID of the component that needs updating. |

**Return Type**

`SharedCommunicationChannelComponent`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedCommunicationChannelComponent

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedCommunicationChannelComponent(
    partner_archiving={
        "enable_archiving": False,
        "inbound_directory": "inboundDirectory",
        "outbound_directory": "outboundDirectory"
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
    communication_type="AS2",
    component_id="0cfe0d5a-0d33-48f8-825a-1d67667e0cd5",
    component_name="Shared AS2 API",
    deleted=True,
    description="description",
    folder_id=921,
    folder_name="Boomi/SampleFolder"
)

result = sdk.shared_communication_channel_component.update_shared_communication_channel_component(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_shared_communication_channel_component

If the Shared Communication Channel component is deleted successfully, the response is `true`.

- HTTP Method: `DELETE`
- Endpoint: `/SharedCommunicationChannelComponent/{id}`

**Parameters**

| Name | Type | Required | Description                                  |
| :--- | :--- | :------- | :------------------------------------------- |
| id\_ | str  | ✅       | ID of the component that you want to delete. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.shared_communication_channel_component.delete_shared_communication_channel_component(id_="id")

print(result)
```

## bulk_shared_communication_channel_component

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/bulk`

**Parameters**

| Name         | Type                                                                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SharedCommunicationChannelComponentBulkRequest](../models/SharedCommunicationChannelComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`SharedCommunicationChannelComponentBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedCommunicationChannelComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedCommunicationChannelComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.shared_communication_channel_component.bulk_shared_communication_channel_component(request_body=request_body)

print(result)
```

## query_shared_communication_channel_component

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). The sample request query returns the Shared Communication Channel components using the AS2 standard for the authenticating account. \>**Note:** The name field in a QUERY filter represents the object's `componentName` field.

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/query`

**Parameters**

| Name         | Type                                                                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SharedCommunicationChannelComponentQueryConfig](../models/SharedCommunicationChannelComponentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`SharedCommunicationChannelComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedCommunicationChannelComponentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedCommunicationChannelComponentQueryConfig(
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

result = sdk.shared_communication_channel_component.query_shared_communication_channel_component(request_body=request_body)

print(result)
```

## query_more_shared_communication_channel_component

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`SharedCommunicationChannelComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ea repre"

result = sdk.shared_communication_channel_component.query_more_shared_communication_channel_component(request_body=request_body)

print(result)
```

