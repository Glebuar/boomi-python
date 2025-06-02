# PartnerDocumentType

**Properties**

| Name                               | Type                   | Required | Description |
| :--------------------------------- | :--------------------- | :------- | :---------- |
| expect_ack_for_outbound            | bool                   | ❌       |             |
| invalid_document_routing           | InvalidDocumentRouting | ❌       |             |
| name                               | str                    | ❌       |             |
| profile_id                         | str                    | ❌       |             |
| qualifier_validation               | bool                   | ❌       |             |
| type_id                            | str                    | ❌       |             |
| use999_ack                         | bool                   | ❌       |             |
| use_ta1_ack                        | bool                   | ❌       |             |
| validate_outbound_transaction_sets | bool                   | ❌       |             |

# InvalidDocumentRouting

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| DOCUMENTSPATH | str  | ✅       | "documentsPath" |
| ERRORSPATH    | str  | ✅       | "errorsPath"    |

