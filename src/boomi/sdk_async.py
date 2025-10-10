
from typing import Union
from .net.environment import Environment
from .sdk import Boomi
from .services.async_.as2_connector_record import As2ConnectorRecordServiceAsync
from .services.async_.account import AccountServiceAsync
from .services.async_.account_cloud_attachment_properties import (
    AccountCloudAttachmentPropertiesServiceAsync,
)
from .services.async_.account_cloud_attachment_quota import (
    AccountCloudAttachmentQuotaServiceAsync,
)
from .services.async_.account_group import AccountGroupServiceAsync
from .services.async_.account_group_account import AccountGroupAccountServiceAsync
from .services.async_.account_group_user_role import AccountGroupUserRoleServiceAsync
from .services.async_.account_sso_config import AccountSsoConfigServiceAsync
from .services.async_.account_user_federation import AccountUserFederationServiceAsync
from .services.async_.account_user_role import AccountUserRoleServiceAsync
from .services.async_.api_usage_count import ApiUsageCountServiceAsync
from .services.async_.atom import AtomServiceAsync
from .services.async_.atom_as2_artifacts import AtomAs2ArtifactsServiceAsync
from .services.async_.atom_connection_field_extension_summary import (
    AtomConnectionFieldExtensionSummaryServiceAsync,
)
from .services.async_.atom_connector_versions import AtomConnectorVersionsServiceAsync
from .services.async_.atom_counters import AtomCountersServiceAsync
from .services.async_.atom_log import AtomLogServiceAsync
from .services.async_.atom_purge import AtomPurgeServiceAsync
from .services.async_.atom_security_policies import AtomSecurityPoliciesServiceAsync
from .services.async_.atom_startup_properties import AtomStartupPropertiesServiceAsync
from .services.async_.atom_worker_log import AtomWorkerLogServiceAsync
from .services.async_.audit_log import AuditLogServiceAsync
from .services.async_.branch import BranchServiceAsync
from .services.async_.change_listener_status import ChangeListenerStatusServiceAsync
from .services.async_.clear_queue import ClearQueueServiceAsync
from .services.async_.cloud import CloudServiceAsync
from .services.async_.component import ComponentServiceAsync
from .services.async_.component_atom_attachment import (
    ComponentAtomAttachmentServiceAsync,
)
from .services.async_.component_diff_request import ComponentDiffRequestServiceAsync
from .services.async_.component_environment_attachment import (
    ComponentEnvironmentAttachmentServiceAsync,
)
from .services.async_.component_metadata import ComponentMetadataServiceAsync
from .services.async_.component_reference import ComponentReferenceServiceAsync
from .services.async_.connection_licensing_report import (
    ConnectionLicensingReportServiceAsync,
)
from .services.async_.connector import ConnectorServiceAsync
from .services.async_.connector_document import ConnectorDocumentServiceAsync
from .services.async_.custom_tracked_field import CustomTrackedFieldServiceAsync
from .services.async_.deployed_expired_certificate import (
    DeployedExpiredCertificateServiceAsync,
)
from .services.async_.deployed_package import DeployedPackageServiceAsync
from .services.async_.deployment import DeploymentServiceAsync
from .services.async_.document_count_account import DocumentCountAccountServiceAsync
from .services.async_.document_count_account_group import (
    DocumentCountAccountGroupServiceAsync,
)
from .services.async_.edifact_connector_record import EdifactConnectorRecordServiceAsync
from .services.async_.edi_custom_connector_record import (
    EdiCustomConnectorRecordServiceAsync,
)
from .services.async_.environment import EnvironmentServiceAsync
from .services.async_.environment_atom_attachment import (
    EnvironmentAtomAttachmentServiceAsync,
)
from .services.async_.environment_connection_field_extension_summary import (
    EnvironmentConnectionFieldExtensionSummaryServiceAsync,
)
from .services.async_.environment_extensions import EnvironmentExtensionsServiceAsync
from .services.async_.environment_map_extension import (
    EnvironmentMapExtensionServiceAsync,
)
from .services.async_.environment_map_extension_external_component import (
    EnvironmentMapExtensionExternalComponentServiceAsync,
)
from .services.async_.environment_map_extension_user_defined_function import (
    EnvironmentMapExtensionUserDefinedFunctionServiceAsync,
)
from .services.async_.environment_map_extension_user_defined_function_summary import (
    EnvironmentMapExtensionUserDefinedFunctionSummaryServiceAsync,
)
from .services.async_.environment_map_extensions_summary import (
    EnvironmentMapExtensionsSummaryServiceAsync,
)
from .services.async_.environment_role import EnvironmentRoleServiceAsync
from .services.async_.event import EventServiceAsync
from .services.async_.execution_artifacts import ExecutionArtifactsServiceAsync
from .services.async_.execution_connector import ExecutionConnectorServiceAsync
from .services.async_.execution_count_account import ExecutionCountAccountServiceAsync
from .services.async_.execution_count_account_group import (
    ExecutionCountAccountGroupServiceAsync,
)
from .services.async_.execution_record import ExecutionRecordServiceAsync
from .services.async_.execution_request import ExecutionRequestServiceAsync
from .services.async_.execution_summary_record import ExecutionSummaryRecordServiceAsync
from .services.async_.folder import FolderServiceAsync
from .services.async_.generic_connector_record import GenericConnectorRecordServiceAsync
from .services.async_.get_assignable_roles import GetAssignableRolesServiceAsync
from .services.async_.hl7_connector_record import Hl7ConnectorRecordServiceAsync
from .services.async_.installer_token import InstallerTokenServiceAsync
from .services.async_.integration_pack import IntegrationPackServiceAsync
from .services.async_.integration_pack_atom_attachment import (
    IntegrationPackAtomAttachmentServiceAsync,
)
from .services.async_.integration_pack_environment_attachment import (
    IntegrationPackEnvironmentAttachmentServiceAsync,
)
from .services.async_.integration_pack_instance import (
    IntegrationPackInstanceServiceAsync,
)
from .services.async_.java_rollback import JavaRollbackServiceAsync
from .services.async_.java_upgrade import JavaUpgradeServiceAsync
from .services.async_.merge_request import MergeRequestServiceAsync
from .services.async_.move_queue_request import MoveQueueRequestServiceAsync
from .services.async_.node_offboard import NodeOffboardServiceAsync
from .services.async_.odette_connector_record import OdetteConnectorRecordServiceAsync
from .services.async_.oftp2_connector_record import Oftp2ConnectorRecordServiceAsync
from .services.async_.packaged_component import PackagedComponentServiceAsync
from .services.async_.packaged_component_manifest import (
    PackagedComponentManifestServiceAsync,
)
from .services.async_.persisted_process_properties import (
    PersistedProcessPropertiesServiceAsync,
)
from .services.async_.process import ProcessServiceAsync
from .services.async_.process_atom_attachment import ProcessAtomAttachmentServiceAsync
from .services.async_.process_environment_attachment import (
    ProcessEnvironmentAttachmentServiceAsync,
)
from .services.async_.process_log import ProcessLogServiceAsync
from .services.async_.process_schedule_status import ProcessScheduleStatusServiceAsync
from .services.async_.process_schedules import ProcessSchedulesServiceAsync
from .services.async_.rerun_document import RerunDocumentServiceAsync
from .services.async_.role import RoleServiceAsync
from .services.async_.rosetta_net_connector_record import (
    RosettaNetConnectorRecordServiceAsync,
)
from .services.async_.runtime_release_schedule import RuntimeReleaseScheduleServiceAsync
from .services.async_.cancel_execution import CancelExecutionServiceAsync
from .services.async_.execute_process import ExecuteProcessServiceAsync
from .services.async_.worker import WorkerServiceAsync
from .services.async_.shared_web_server_log import SharedWebServerLogServiceAsync
from .services.async_.account_provision import AccountProvisionServiceAsync
from .services.async_.shared_server_information import (
    SharedServerInformationServiceAsync,
)
from .services.async_.shared_web_server import SharedWebServerServiceAsync
from .services.async_.throughput_account import ThroughputAccountServiceAsync
from .services.async_.throughput_account_group import ThroughputAccountGroupServiceAsync
from .services.async_.tradacoms_connector_record import (
    TradacomsConnectorRecordServiceAsync,
)
from .services.async_.trading_partner_component import (
    TradingPartnerComponentServiceAsync,
)
from .services.async_.trading_partner_processing_group import (
    TradingPartnerProcessingGroupServiceAsync,
)
from .services.async_.x12_connector_record import X12ConnectorRecordServiceAsync
from .services.async_.atom_disk_space import AtomDiskSpaceServiceAsync
from .services.async_.list_queues import ListQueuesServiceAsync
from .services.async_.listener_status import ListenerStatusServiceAsync
from .services.async_.organization_component import OrganizationComponentServiceAsync
from .services.async_.shared_communication_channel_component import (
    SharedCommunicationChannelComponentServiceAsync,
)
from .services.async_.account_group_integration_pack import (
    AccountGroupIntegrationPackServiceAsync,
)
from .services.async_.publisher_integration_pack import (
    PublisherIntegrationPackServiceAsync,
)
from .services.async_.release_integration_pack import ReleaseIntegrationPackServiceAsync
from .services.async_.release_integration_pack_status import (
    ReleaseIntegrationPackStatusServiceAsync,
)
from .services.async_.runtime_restart_request import RuntimeRestartRequestServiceAsync
from .services.async_.refresh_secrets_manager import RefreshSecretsManagerServiceAsync


class BoomiAsync(Boomi):
    """
    BoomiAsync is the asynchronous version of the Boomi SDK Client.
    """

    def __init__(
        self,
        access_token: str = None,
        username: str = None,
        password: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
        account_id: str = "platform_account_ID",
    ):
        super().__init__(
            access_token=access_token,
            username=username,
            password=password,
            base_url=base_url,
            timeout=timeout,
            account_id=account_id,
        )

        self.as2_connector_record = As2ConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.account = AccountServiceAsync(base_url=self._base_url)
        self.account_cloud_attachment_properties = (
            AccountCloudAttachmentPropertiesServiceAsync(base_url=self._base_url)
        )
        self.account_cloud_attachment_quota = AccountCloudAttachmentQuotaServiceAsync(
            base_url=self._base_url
        )
        self.account_group = AccountGroupServiceAsync(base_url=self._base_url)
        self.account_group_account = AccountGroupAccountServiceAsync(
            base_url=self._base_url
        )
        self.account_group_user_role = AccountGroupUserRoleServiceAsync(
            base_url=self._base_url
        )
        self.account_sso_config = AccountSsoConfigServiceAsync(base_url=self._base_url)
        self.account_user_federation = AccountUserFederationServiceAsync(
            base_url=self._base_url
        )
        self.account_user_role = AccountUserRoleServiceAsync(base_url=self._base_url)
        self.api_usage_count = ApiUsageCountServiceAsync(base_url=self._base_url)
        self.atom = AtomServiceAsync(base_url=self._base_url)
        self.atom_as2_artifacts = AtomAs2ArtifactsServiceAsync(base_url=self._base_url)
        self.atom_connection_field_extension_summary = (
            AtomConnectionFieldExtensionSummaryServiceAsync(base_url=self._base_url)
        )
        self.atom_connector_versions = AtomConnectorVersionsServiceAsync(
            base_url=self._base_url
        )
        self.atom_counters = AtomCountersServiceAsync(base_url=self._base_url)
        self.atom_log = AtomLogServiceAsync(base_url=self._base_url)
        self.atom_purge = AtomPurgeServiceAsync(base_url=self._base_url)
        self.atom_security_policies = AtomSecurityPoliciesServiceAsync(
            base_url=self._base_url
        )
        self.atom_startup_properties = AtomStartupPropertiesServiceAsync(
            base_url=self._base_url
        )
        self.atom_worker_log = AtomWorkerLogServiceAsync(base_url=self._base_url)
        self.audit_log = AuditLogServiceAsync(base_url=self._base_url)
        self.branch = BranchServiceAsync(base_url=self._base_url)
        self.change_listener_status = ChangeListenerStatusServiceAsync(
            base_url=self._base_url
        )
        self.clear_queue = ClearQueueServiceAsync(base_url=self._base_url)
        self.cloud = CloudServiceAsync(base_url=self._base_url)
        self.component = ComponentServiceAsync(base_url=self._base_url)
        self.component_atom_attachment = ComponentAtomAttachmentServiceAsync(
            base_url=self._base_url
        )
        self.component_diff_request = ComponentDiffRequestServiceAsync(
            base_url=self._base_url
        )
        self.component_environment_attachment = (
            ComponentEnvironmentAttachmentServiceAsync(base_url=self._base_url)
        )
        self.component_metadata = ComponentMetadataServiceAsync(base_url=self._base_url)
        self.component_reference = ComponentReferenceServiceAsync(
            base_url=self._base_url
        )
        self.connection_licensing_report = ConnectionLicensingReportServiceAsync(
            base_url=self._base_url
        )
        self.connector = ConnectorServiceAsync(base_url=self._base_url)
        self.connector_document = ConnectorDocumentServiceAsync(base_url=self._base_url)
        self.custom_tracked_field = CustomTrackedFieldServiceAsync(
            base_url=self._base_url
        )
        self.deployed_expired_certificate = DeployedExpiredCertificateServiceAsync(
            base_url=self._base_url
        )
        self.deployed_package = DeployedPackageServiceAsync(base_url=self._base_url)
        self.deployment = DeploymentServiceAsync(base_url=self._base_url)
        self.document_count_account = DocumentCountAccountServiceAsync(
            base_url=self._base_url
        )
        self.document_count_account_group = DocumentCountAccountGroupServiceAsync(
            base_url=self._base_url
        )
        self.edifact_connector_record = EdifactConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.edi_custom_connector_record = EdiCustomConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.environment = EnvironmentServiceAsync(base_url=self._base_url)
        self.environment_atom_attachment = EnvironmentAtomAttachmentServiceAsync(
            base_url=self._base_url
        )
        self.environment_connection_field_extension_summary = (
            EnvironmentConnectionFieldExtensionSummaryServiceAsync(
                base_url=self._base_url
            )
        )
        self.environment_extensions = EnvironmentExtensionsServiceAsync(
            base_url=self._base_url
        )
        self.environment_map_extension = EnvironmentMapExtensionServiceAsync(
            base_url=self._base_url
        )
        self.environment_map_extension_external_component = (
            EnvironmentMapExtensionExternalComponentServiceAsync(
                base_url=self._base_url
            )
        )
        self.environment_map_extension_user_defined_function = (
            EnvironmentMapExtensionUserDefinedFunctionServiceAsync(
                base_url=self._base_url
            )
        )
        self.environment_map_extension_user_defined_function_summary = (
            EnvironmentMapExtensionUserDefinedFunctionSummaryServiceAsync(
                base_url=self._base_url
            )
        )
        self.environment_map_extensions_summary = (
            EnvironmentMapExtensionsSummaryServiceAsync(base_url=self._base_url)
        )
        self.environment_role = EnvironmentRoleServiceAsync(base_url=self._base_url)
        self.event = EventServiceAsync(base_url=self._base_url)
        self.execution_artifacts = ExecutionArtifactsServiceAsync(
            base_url=self._base_url
        )
        self.execution_connector = ExecutionConnectorServiceAsync(
            base_url=self._base_url
        )
        self.execution_count_account = ExecutionCountAccountServiceAsync(
            base_url=self._base_url
        )
        self.execution_count_account_group = ExecutionCountAccountGroupServiceAsync(
            base_url=self._base_url
        )
        self.execution_record = ExecutionRecordServiceAsync(base_url=self._base_url)
        self.execution_request = ExecutionRequestServiceAsync(base_url=self._base_url)
        self.execution_summary_record = ExecutionSummaryRecordServiceAsync(
            base_url=self._base_url
        )
        self.folder = FolderServiceAsync(base_url=self._base_url)
        self.generic_connector_record = GenericConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.get_assignable_roles = GetAssignableRolesServiceAsync(
            base_url=self._base_url
        )
        self.hl7_connector_record = Hl7ConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.installer_token = InstallerTokenServiceAsync(base_url=self._base_url)
        self.integration_pack = IntegrationPackServiceAsync(base_url=self._base_url)
        self.integration_pack_atom_attachment = (
            IntegrationPackAtomAttachmentServiceAsync(base_url=self._base_url)
        )
        self.integration_pack_environment_attachment = (
            IntegrationPackEnvironmentAttachmentServiceAsync(base_url=self._base_url)
        )
        self.integration_pack_instance = IntegrationPackInstanceServiceAsync(
            base_url=self._base_url
        )
        self.java_rollback = JavaRollbackServiceAsync(base_url=self._base_url)
        self.java_upgrade = JavaUpgradeServiceAsync(base_url=self._base_url)
        self.merge_request = MergeRequestServiceAsync(base_url=self._base_url)
        self.move_queue_request = MoveQueueRequestServiceAsync(base_url=self._base_url)
        self.node_offboard = NodeOffboardServiceAsync(base_url=self._base_url)
        self.odette_connector_record = OdetteConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.oftp2_connector_record = Oftp2ConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.packaged_component = PackagedComponentServiceAsync(base_url=self._base_url)
        self.packaged_component_manifest = PackagedComponentManifestServiceAsync(
            base_url=self._base_url
        )
        self.persisted_process_properties = PersistedProcessPropertiesServiceAsync(
            base_url=self._base_url
        )
        self.process = ProcessServiceAsync(base_url=self._base_url)
        self.process_atom_attachment = ProcessAtomAttachmentServiceAsync(
            base_url=self._base_url
        )
        self.process_environment_attachment = ProcessEnvironmentAttachmentServiceAsync(
            base_url=self._base_url
        )
        self.process_log = ProcessLogServiceAsync(base_url=self._base_url)
        self.process_schedule_status = ProcessScheduleStatusServiceAsync(
            base_url=self._base_url
        )
        self.process_schedules = ProcessSchedulesServiceAsync(base_url=self._base_url)
        self.rerun_document = RerunDocumentServiceAsync(base_url=self._base_url)
        self.role = RoleServiceAsync(base_url=self._base_url)
        self.rosetta_net_connector_record = RosettaNetConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.runtime_release_schedule = RuntimeReleaseScheduleServiceAsync(
            base_url=self._base_url
        )
        self.cancel_execution = CancelExecutionServiceAsync(base_url=self._base_url)
        self.execute_process = ExecuteProcessServiceAsync(base_url=self._base_url)
        self.worker = WorkerServiceAsync(base_url=self._base_url)
        self.shared_web_server_log = SharedWebServerLogServiceAsync(
            base_url=self._base_url
        )
        self.account_provision = AccountProvisionServiceAsync(base_url=self._base_url)
        self.shared_server_information = SharedServerInformationServiceAsync(
            base_url=self._base_url
        )
        self.shared_web_server = SharedWebServerServiceAsync(base_url=self._base_url)
        self.throughput_account = ThroughputAccountServiceAsync(base_url=self._base_url)
        self.throughput_account_group = ThroughputAccountGroupServiceAsync(
            base_url=self._base_url
        )
        self.tradacoms_connector_record = TradacomsConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.trading_partner_component = TradingPartnerComponentServiceAsync(
            base_url=self._base_url
        )
        self.trading_partner_processing_group = (
            TradingPartnerProcessingGroupServiceAsync(base_url=self._base_url)
        )
        self.x12_connector_record = X12ConnectorRecordServiceAsync(
            base_url=self._base_url
        )
        self.atom_disk_space = AtomDiskSpaceServiceAsync(base_url=self._base_url)
        self.list_queues = ListQueuesServiceAsync(base_url=self._base_url)
        self.listener_status = ListenerStatusServiceAsync(base_url=self._base_url)
        self.organization_component = OrganizationComponentServiceAsync(
            base_url=self._base_url
        )
        self.shared_communication_channel_component = (
            SharedCommunicationChannelComponentServiceAsync(base_url=self._base_url)
        )
        self.account_group_integration_pack = AccountGroupIntegrationPackServiceAsync(
            base_url=self._base_url
        )
        self.publisher_integration_pack = PublisherIntegrationPackServiceAsync(
            base_url=self._base_url
        )
        self.release_integration_pack = ReleaseIntegrationPackServiceAsync(
            base_url=self._base_url
        )
        self.release_integration_pack_status = ReleaseIntegrationPackStatusServiceAsync(
            base_url=self._base_url
        )
        self.runtime_restart_request = RuntimeRestartRequestServiceAsync(
            base_url=self._base_url
        )
        self.refresh_secrets_manager = RefreshSecretsManagerServiceAsync(
            base_url=self._base_url
        )
