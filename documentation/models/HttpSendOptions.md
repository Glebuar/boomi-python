# HttpSendOptions

**Properties**

| Name                    | Type                               | Required | Description |
| :---------------------- | :--------------------------------- | :------- | :---------- |
| path_elements           | HttpPathElements                   | ✅       |             |
| request_headers         | HttpRequestHeaders                 | ✅       |             |
| response_header_mapping | HttpResponseHeaderMapping          | ✅       |             |
| data_content_type       | str                                | ❌       |             |
| follow_redirects        | bool                               | ❌       |             |
| method_type             | HttpSendOptionsMethodType          | ❌       |             |
| reflect_headers         | HttpReflectHeaders                 | ❌       |             |
| request_profile         | str                                | ❌       |             |
| request_profile_type    | HttpSendOptionsRequestProfileType  | ❌       |             |
| response_profile        | str                                | ❌       |             |
| response_profile_type   | HttpSendOptionsResponseProfileType | ❌       |             |
| return_errors           | bool                               | ❌       |             |
| return_responses        | bool                               | ❌       |             |
| use_default_options     | bool                               | ❌       |             |

# HttpSendOptionsMethodType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| GET    | str  | ✅       | "GET"       |
| POST   | str  | ✅       | "POST"      |
| PUT    | str  | ✅       | "PUT"       |
| DELETE | str  | ✅       | "DELETE"    |

# HttpSendOptionsRequestProfileType

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NONE | str  | ✅       | "NONE"      |
| XML  | str  | ✅       | "XML"       |
| JSON | str  | ✅       | "JSON"      |

# HttpSendOptionsResponseProfileType

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NONE | str  | ✅       | "NONE"      |
| XML  | str  | ✅       | "XML"       |
| JSON | str  | ✅       | "JSON"      |

