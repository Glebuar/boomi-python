# AttachmentInfo

**Properties**

| Name                    | Type                        | Required | Description |
| :---------------------- | :-------------------------- | :------- | :---------- |
| attachment_cache        | str                         | ❌       |             |
| attachment_content_type | List[AttachmentContentType] | ❌       |             |
| multiple_attachments    | bool                        | ❌       |             |

# AttachmentContentType

**Properties**

| Name              | Type | Required | Description          |
| :---------------- | :--- | :------- | :------------------- |
| APPLICATIONXML    | str  | ✅       | "application/xml"    |
| APPLICATIONPDF    | str  | ✅       | "application/pdf"    |
| APPLICATIONMSWORD | str  | ✅       | "application/msword" |
| IMAGETIFF         | str  | ✅       | "image/tiff"         |
| IMAGEJPEG         | str  | ✅       | "image/jpeg"         |
| TEXTPLAIN         | str  | ✅       | "text/plain"         |

