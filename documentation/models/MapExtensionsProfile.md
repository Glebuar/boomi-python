# MapExtensionsProfile

Represents the fields in a source or destination profile of the given map, and specifies the section of the map in which to extend. \>**Note:** You cannot add or create new fields in the object's request body. You must add new fields in the user interface of the underlying Map component or from a dynamic reimport. See the Customizing profiles section later in this topic. The following SourceProfile attributes define fields in the source profile: - componentId - represents the object definition extension ID. A GET request returns this value. - name - the user-defined field label(s) found in the source profile. - xpath - represents the field location in the source profile hierarchy.

**Properties**

| Name         | Type                    | Required | Description |
| :----------- | :---------------------- | :------- | :---------- |
| node         | List[MapExtensionsNode] | ❌       |             |
| component_id | str                     | ❌       |             |
| type\_       | str                     | ❌       |             |

