# DiskGetOptions

**Properties**

| Name                    | Type            | Required | Description |
| :---------------------- | :-------------- | :------- | :---------- |
| file_filter             | str             | ✅       |             |
| get_directory           | str             | ✅       |             |
| delete_after_read       | bool            | ❌       |             |
| filter_match_type       | FilterMatchType | ❌       |             |
| max_file_count          | int             | ❌       |             |
| use_default_get_options | bool            | ❌       |             |

# FilterMatchType

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| WILDCARD | str  | ✅       | "wildcard"  |
| REGEX    | str  | ✅       | "regex"     |

