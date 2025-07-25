# MapExtensionBrowseSettings

Represents the Connection information and is used to re-import newly-appended profile fields. This attribute is only applicable for certain application Connectors. To perform a re-import, the client must use the EXECUTE operation. For more information, see the Customizing profiles section later in this topic. **Note:** `containerId` is a required field when using BrowseSettings.

**Properties**

| Name               | Type               | Required | Description |
| :----------------- | :----------------- | :------- | :---------- |
| destination_browse | MapExtensionBrowse | ✅       |             |
| source_browse      | MapExtensionBrowse | ✅       |             |
| container_id       | str                | ❌       |             |

