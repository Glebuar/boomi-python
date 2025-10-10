
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "cacerts_path": "cacertsPath",
        "external_jdk_path": "externalJDKPath",
        "migrate_certificate": "migrateCertificate",
        "pref_jre_location": "prefJreLocation",
    }
)
class JavaUpgradeOptions(BaseModel):
    """JavaUpgradeOptions

    :param cacerts_path: (Optional) If specified, defines the directory file path from which to migrate custom certificates.If you include this optional attribute in your request, the directory file path in your local drive must contain either of the following folder patterns jre/lib/security/cacerts, or lib/security/cacerts , wherecacerts is the name of the certificates file.\<br /\>**Note:** You must title the certificate file as cacerts.\<br /\> \<br /\> Because the Upgrade Java API operationautomatically appends the lib/security and jre/lib/security part of the file path to search for the cacerts file name, you need only to supply the root directory OR the root directory and JRE folder in the cacerts value of your request. For example, if your certificates file is located at /boomi_atom/jre/lib/security/cacerts, you need to specify either /boomi_atom/jre or /boomi_atom in the attribute's value.\<br /\> \<br /\>If you omit this attribute from the request or it does not populate its value, it uses the default JVM directory. The migrateCertificates value must be set to true for the override to take place.
    :type cacerts_path: str
    :param external_jdk_path: (Required if you set `prefJreLocation` to `external`) Defines the directory file path to find the custom JDK your container uses after the upgrade. Include this attribute in the request when you want to use a custom JDK rather than one provided by [Boomi](lib-Boomi_Keywords_0346af2b-13d7-491e-bec9-18c5d89225bf.md#BOOMI_DELL). If you do not specify this attribute, the upgrader automatically installs a new [Boomi](lib-Boomi_Keywords_0346af2b-13d7-491e-bec9-18c5d89225bf.md#BOOMI_DELL)-provided JRE to your local directory with the latest supported version of Java.
    :type external_jdk_path: str
    :param migrate_certificate: (Optional) If set to true in the request body, custom certificate migration occurs automatically to the new version of Java. It places certificates in a new JVM of the same directory where you originally installed the container.If set to false in the request body, custom certificates do not migrate.\<br /\>**Note:** If you include `JavaUpgradeOptions` but omit `migrateCertificate` from the request, the response automatically sets the `migrateCertificate` field to false., defaults to None
    :type migrate_certificate: bool, optional
    :param pref_jre_location: Determines how the installation's JRE is updated or whether to use an external JDK. The following values are possible:-   Switch the preferred JRE to the installation's JRE directory \<br /\>- internal\<br /\> -   Do not make changes to the preferred JRE - current\<br /\>- Use external JDK for preferred JRE - external\<br /\>If you set `prefJreLocation` to external you must also specify `externalJDKPath`.\<br /\>If you do not specify a value or omit the parameter, the default value is current.
    :type pref_jre_location: str
    """

    def __init__(
        self,
        cacerts_path: str,
        external_jdk_path: str,
        pref_jre_location: str,
        migrate_certificate: bool = SENTINEL,
        **kwargs
    ):
        """JavaUpgradeOptions

        :param cacerts_path: (Optional) If specified, defines the directory file path from which to migrate custom certificates.If you include this optional attribute in your request, the directory file path in your local drive must contain either of the following folder patterns jre/lib/security/cacerts, or lib/security/cacerts , wherecacerts is the name of the certificates file.\<br /\>**Note:** You must title the certificate file as cacerts.\<br /\> \<br /\> Because the Upgrade Java API operationautomatically appends the lib/security and jre/lib/security part of the file path to search for the cacerts file name, you need only to supply the root directory OR the root directory and JRE folder in the cacerts value of your request. For example, if your certificates file is located at /boomi_atom/jre/lib/security/cacerts, you need to specify either /boomi_atom/jre or /boomi_atom in the attribute's value.\<br /\> \<br /\>If you omit this attribute from the request or it does not populate its value, it uses the default JVM directory. The migrateCertificates value must be set to true for the override to take place.
        :type cacerts_path: str
        :param external_jdk_path: (Required if you set `prefJreLocation` to `external`) Defines the directory file path to find the custom JDK your container uses after the upgrade. Include this attribute in the request when you want to use a custom JDK rather than one provided by [Boomi](lib-Boomi_Keywords_0346af2b-13d7-491e-bec9-18c5d89225bf.md#BOOMI_DELL). If you do not specify this attribute, the upgrader automatically installs a new [Boomi](lib-Boomi_Keywords_0346af2b-13d7-491e-bec9-18c5d89225bf.md#BOOMI_DELL)-provided JRE to your local directory with the latest supported version of Java.
        :type external_jdk_path: str
        :param migrate_certificate: (Optional) If set to true in the request body, custom certificate migration occurs automatically to the new version of Java. It places certificates in a new JVM of the same directory where you originally installed the container.If set to false in the request body, custom certificates do not migrate.\<br /\>**Note:** If you include `JavaUpgradeOptions` but omit `migrateCertificate` from the request, the response automatically sets the `migrateCertificate` field to false., defaults to None
        :type migrate_certificate: bool, optional
        :param pref_jre_location: Determines how the installation's JRE is updated or whether to use an external JDK. The following values are possible:-   Switch the preferred JRE to the installation's JRE directory \<br /\>- internal\<br /\> -   Do not make changes to the preferred JRE - current\<br /\>- Use external JDK for preferred JRE - external\<br /\>If you set `prefJreLocation` to external you must also specify `externalJDKPath`.\<br /\>If you do not specify a value or omit the parameter, the default value is current.
        :type pref_jre_location: str
        """
        self.cacerts_path = cacerts_path
        self.external_jdk_path = external_jdk_path
        if migrate_certificate is not SENTINEL:
            self.migrate_certificate = migrate_certificate
        self.pref_jre_location = pref_jre_location
        self._kwargs = kwargs
