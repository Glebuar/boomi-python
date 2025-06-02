# MapExtensionsExtendedMappings

Represents the field mappings between profiles, functions or both. You can use the following attributes: - fromXPath - represents the source profile's field path or the function's output key from which you are mapping. - toXPath - represents the destination profile's field path or the function's input key to which you are mapping. - toFunction - represents the function ID from which you are mapping. - fromFunction - represents the function ID to which you are mapping. To properly define each of these attributes, see the section [How to configure ExtendedMappings](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension#how-to-configure-extendedmappings)

**Properties**

| Name    | Type                       | Required | Description |
| :------ | :------------------------- | :------- | :---------- |
| mapping | List[MapExtensionsMapping] | ❌       |             |

