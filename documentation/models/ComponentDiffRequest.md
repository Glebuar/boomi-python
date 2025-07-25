# ComponentDiffRequest

**Properties**

| Name             | Type           | Required | Description                                                         |
| :--------------- | :------------- | :------- | :------------------------------------------------------------------ |
| component_id     | str            | ✅       | The ID of the component for which you want to compare versions.     |
| source_version   | int            | ✅       | The source version of the component.                                |
| target_version   | int            | ✅       | The target version which you want to compare to the source version. |
| comp_diff_config | CompDiffConfig | ❌       |                                                                     |

