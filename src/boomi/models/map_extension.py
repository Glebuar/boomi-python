
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .map_extension_browse_settings import MapExtensionBrowseSettings
from .map_extensions_profile import MapExtensionsProfile
from .map_extension_extend_profile import MapExtensionExtendProfile
from .map_extensions_functions import MapExtensionsFunctions
from .map_extensions_extended_mappings import MapExtensionsExtendedMappings


@JsonMap(
    {
        "browse_settings": "BrowseSettings",
        "destination_profile": "DestinationProfile",
        "destination_profile_extensions": "DestinationProfileExtensions",
        "extended_functions": "ExtendedFunctions",
        "extended_mappings": "ExtendedMappings",
        "source_profile": "SourceProfile",
        "source_profile_extensions": "SourceProfileExtensions",
    }
)
class MapExtension(BaseModel):
    """MapExtension

    :param browse_settings: Represents the Connection information and is used to re-import newly-appended profile fields. This attribute is only applicable for certain application Connectors. To perform a re-import, the client must use the EXECUTE operation. For more information, see the Customizing profiles section later in this topic.  **Note:** `containerId` is a required field when using BrowseSettings.
    :type browse_settings: MapExtensionBrowseSettings
    :param destination_profile: Represents the fields in a source or destination profile of the given map, and specifies the section of the map in which to extend.   \>**Note:** You cannot add or create new fields in the object's request body. You must add new fields in the user interface of the underlying Map component or from a dynamic reimport. See the Customizing profiles section later in this topic. The following SourceProfile attributes define fields in the source profile: - componentId - represents the object definition extension ID. A GET request returns this value. - name - the user-defined field label(s) found in the source profile. - xpath - represents the field location in the source profile hierarchy.
    :type destination_profile: MapExtensionsProfile
    :param destination_profile_extensions: Contains the user-defined custom fields for the source or destination profile. Applicable only to Flat File profiles. Represents the field and value configuration settings manually specified in the source or destination profile's Data Element tab. For more information, refer to [Customizing Profiles](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension).
    :type destination_profile_extensions: MapExtensionExtendProfile
    :param extended_functions: The definition of Map function steps used in the Map component. For detailed information about how to define Map functions in a request or response, see the topic [Environment Map Extension functions](/docs/APIs/PlatformAPI/Environment_Map_Extension_functions). You can use the Extended Functions attribute to define the following extensible map functions (supports standard and user-defined function types): - User Defined - Connector - Lookup - Date - Numeric - String - Custom Scripting - Property
    :type extended_functions: MapExtensionsFunctions
    :param extended_mappings: Represents the field mappings between profiles, functions or both. You can use the following attributes: - fromXPath - represents the source profile's field path or the function's output key from which you are mapping. - toXPath - represents the destination profile's field path or the function's input key to which you are mapping. - toFunction - represents the function ID from which you are mapping. - fromFunction - represents the function ID to which you are mapping. To properly define each of these attributes, see the section [How to configure ExtendedMappings](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension#how-to-configure-extendedmappings)
    :type extended_mappings: MapExtensionsExtendedMappings
    :param source_profile: Represents the fields in a source or destination profile of the given map, and specifies the section of the map in which to extend.   \>**Note:** You cannot add or create new fields in the object's request body. You must add new fields in the user interface of the underlying Map component or from a dynamic reimport. See the Customizing profiles section later in this topic. The following SourceProfile attributes define fields in the source profile: - componentId - represents the object definition extension ID. A GET request returns this value. - name - the user-defined field label(s) found in the source profile. - xpath - represents the field location in the source profile hierarchy.
    :type source_profile: MapExtensionsProfile
    :param source_profile_extensions: Contains the user-defined custom fields for the source or destination profile. Applicable only to Flat File profiles. Represents the field and value configuration settings manually specified in the source or destination profile's Data Element tab. For more information, refer to [Customizing Profiles](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension).
    :type source_profile_extensions: MapExtensionExtendProfile
    """

    def __init__(
        self,
        browse_settings: MapExtensionBrowseSettings,
        destination_profile: MapExtensionsProfile,
        destination_profile_extensions: MapExtensionExtendProfile,
        extended_functions: MapExtensionsFunctions,
        extended_mappings: MapExtensionsExtendedMappings,
        source_profile: MapExtensionsProfile,
        source_profile_extensions: MapExtensionExtendProfile,
        **kwargs,
    ):
        """MapExtension

        :param browse_settings: Represents the Connection information and is used to re-import newly-appended profile fields. This attribute is only applicable for certain application Connectors. To perform a re-import, the client must use the EXECUTE operation. For more information, see the Customizing profiles section later in this topic.  **Note:** `containerId` is a required field when using BrowseSettings.
        :type browse_settings: MapExtensionBrowseSettings
        :param destination_profile: Represents the fields in a source or destination profile of the given map, and specifies the section of the map in which to extend.   \>**Note:** You cannot add or create new fields in the object's request body. You must add new fields in the user interface of the underlying Map component or from a dynamic reimport. See the Customizing profiles section later in this topic. The following SourceProfile attributes define fields in the source profile: - componentId - represents the object definition extension ID. A GET request returns this value. - name - the user-defined field label(s) found in the source profile. - xpath - represents the field location in the source profile hierarchy.
        :type destination_profile: MapExtensionsProfile
        :param destination_profile_extensions: Contains the user-defined custom fields for the source or destination profile. Applicable only to Flat File profiles. Represents the field and value configuration settings manually specified in the source or destination profile's Data Element tab. For more information, refer to [Customizing Profiles](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension).
        :type destination_profile_extensions: MapExtensionExtendProfile
        :param extended_functions: The definition of Map function steps used in the Map component. For detailed information about how to define Map functions in a request or response, see the topic [Environment Map Extension functions](/docs/APIs/PlatformAPI/Environment_Map_Extension_functions). You can use the Extended Functions attribute to define the following extensible map functions (supports standard and user-defined function types): - User Defined - Connector - Lookup - Date - Numeric - String - Custom Scripting - Property
        :type extended_functions: MapExtensionsFunctions
        :param extended_mappings: Represents the field mappings between profiles, functions or both. You can use the following attributes: - fromXPath - represents the source profile's field path or the function's output key from which you are mapping. - toXPath - represents the destination profile's field path or the function's input key to which you are mapping. - toFunction - represents the function ID from which you are mapping. - fromFunction - represents the function ID to which you are mapping. To properly define each of these attributes, see the section [How to configure ExtendedMappings](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension#how-to-configure-extendedmappings)
        :type extended_mappings: MapExtensionsExtendedMappings
        :param source_profile: Represents the fields in a source or destination profile of the given map, and specifies the section of the map in which to extend.   \>**Note:** You cannot add or create new fields in the object's request body. You must add new fields in the user interface of the underlying Map component or from a dynamic reimport. See the Customizing profiles section later in this topic. The following SourceProfile attributes define fields in the source profile: - componentId - represents the object definition extension ID. A GET request returns this value. - name - the user-defined field label(s) found in the source profile. - xpath - represents the field location in the source profile hierarchy.
        :type source_profile: MapExtensionsProfile
        :param source_profile_extensions: Contains the user-defined custom fields for the source or destination profile. Applicable only to Flat File profiles. Represents the field and value configuration settings manually specified in the source or destination profile's Data Element tab. For more information, refer to [Customizing Profiles](/docs/APIs/PlatformAPI/Customizing_profiles_environment_map_extension).
        :type source_profile_extensions: MapExtensionExtendProfile
        """
        self.browse_settings = self._define_object(
            browse_settings, MapExtensionBrowseSettings
        )
        self.destination_profile = self._define_object(
            destination_profile, MapExtensionsProfile
        )
        self.destination_profile_extensions = self._define_object(
            destination_profile_extensions, MapExtensionExtendProfile
        )
        self.extended_functions = self._define_object(
            extended_functions, MapExtensionsFunctions
        )
        self.extended_mappings = self._define_object(
            extended_mappings, MapExtensionsExtendedMappings
        )
        self.source_profile = self._define_object(source_profile, MapExtensionsProfile)
        self.source_profile_extensions = self._define_object(
            source_profile_extensions, MapExtensionExtendProfile
        )
        self._kwargs = kwargs
