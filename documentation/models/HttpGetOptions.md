# HttpGetOptions

**Properties**

| Name                    | Type                              | Required | Description |
| :---------------------- | :-------------------------------- | :------- | :---------- |
| path_elements           | HttpPathElements                  | ✅       |             |
| request_headers         | HttpRequestHeaders                | ✅       |             |
| response_header_mapping | HttpResponseHeaderMapping         | ✅       |             |
| data_content_type       | str                               | ❌       |             |
| follow_redirects        | bool                              | ❌       |             |
| method_type             | HttpGetOptionsMethodType          | ❌       |             |
| reflect_headers         | HttpReflectHeaders                | ❌       |             |
| request_profile         | str                               | ❌       |             |
| request_profile_type    | HttpGetOptionsRequestProfileType  | ❌       |             |
| response_profile        | str                               | ❌       |             |
| response_profile_type   | HttpGetOptionsResponseProfileType | ❌       |             |
| return_errors           | bool                              | ❌       |             |
| use_default_options     | bool                              | ❌       |             |

# HttpGetOptionsMethodType

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| GET    | str  | ✅       | "GET"       |
| POST   | str  | ✅       | "POST"      |
| PUT    | str  | ✅       | "PUT"       |
| DELETE | str  | ✅       | "DELETE"    |

# HttpGetOptionsRequestProfileType

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NONE | str  | ✅       | "NONE"      |
| XML  | str  | ✅       | "XML"       |
| JSON | str  | ✅       | "JSON"      |

# HttpGetOptionsResponseProfileType

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| NONE | str  | ✅       | "NONE"      |
| XML  | str  | ✅       | "XML"       |
| JSON | str  | ✅       | "JSON"      |

