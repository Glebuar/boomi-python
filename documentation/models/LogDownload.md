# LogDownload

**Properties**

| Name        | Type | Required | Description                                                                                                                          |
| :---------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| status_code | str  | ❌       | The status code as one of the following: - 202 — status message: Beginning download. - 504 — status message: Runtime is unavailable. |
| message     | str  | ❌       | The status message.                                                                                                                  |
| url         | str  | ❌       | (statusCode 202 only) The URL for the download.                                                                                      |

