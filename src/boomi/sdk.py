
from typing import Union
from .services.as2_connector_record import As2ConnectorRecordService
from .services.account import AccountService
from .services.account_cloud_attachment_properties import (
    AccountCloudAttachmentPropertiesService,
)
from .services.account_cloud_attachment_quota import AccountCloudAttachmentQuotaService
from .services.account_group import AccountGroupService
from .services.account_group_account import AccountGroupAccountService
from .services.account_group_user_role import AccountGroupUserRoleService
from .services.account_sso_config import AccountSsoConfigService
from .services.account_user_federation import AccountUserFederationService
from .services.account_user_role import AccountUserRoleService
from .services.api_usage_count import ApiUsageCountService
from .services.atom import AtomService
from .services.atom_as2_artifacts import AtomAs2ArtifactsService
from .services.atom_connection_field_extension_summary import (
    AtomConnectionFieldExtensionSummaryService,
)
from .services.atom_connector_versions import AtomConnectorVersionsService
from .services.atom_counters import AtomCountersService
from .services.atom_log import AtomLogService
from .services.atom_purge import AtomPurgeService
from .services.atom_security_policies import AtomSecurityPoliciesService
from .services.atom_startup_properties import AtomStartupPropertiesService
from .services.atom_worker_log import AtomWorkerLogService
from .services.audit_log import AuditLogService
from .services.branch import BranchService
from .services.change_listener_status import ChangeListenerStatusService
from .services.clear_queue import ClearQueueService
from .services.cloud import CloudService
from .services.component import ComponentService
from .services.component_atom_attachment import ComponentAtomAttachmentService
from .services.component_diff_request import ComponentDiffRequestService
from .services.component_environment_attachment import (
    ComponentEnvironmentAttachmentService,
)
from .services.component_metadata import ComponentMetadataService
from .services.component_reference import ComponentReferenceService
from .services.connection_licensing_report import ConnectionLicensingReportService
from .services.connector import ConnectorService
from .services.connector_document import ConnectorDocumentService
from .services.custom_tracked_field import CustomTrackedFieldService
from .services.deployed_expired_certificate import DeployedExpiredCertificateService
from .services.deployed_package import DeployedPackageService
from .services.deployment import DeploymentService
from .services.document_count_account import DocumentCountAccountService
from .services.document_count_account_group import DocumentCountAccountGroupService
from .services.edifact_connector_record import EdifactConnectorRecordService
from .services.edi_custom_connector_record import EdiCustomConnectorRecordService
from .services.environment import EnvironmentService
from .services.environment_atom_attachment import EnvironmentAtomAttachmentService
from .services.environment_connection_field_extension_summary import (
    EnvironmentConnectionFieldExtensionSummaryService,
)
from .services.environment_extensions import EnvironmentExtensionsService
from .services.environment_map_extension import EnvironmentMapExtensionService
from .services.environment_map_extension_external_component import (
    EnvironmentMapExtensionExternalComponentService,
)
from .services.environment_map_extension_user_defined_function import (
    EnvironmentMapExtensionUserDefinedFunctionService,
)
from .services.environment_map_extension_user_defined_function_summary import (
    EnvironmentMapExtensionUserDefinedFunctionSummaryService,
)
from .services.environment_map_extensions_summary import (
    EnvironmentMapExtensionsSummaryService,
)
from .services.environment_role import EnvironmentRoleService
from .services.event import EventService
from .services.execution_artifacts import ExecutionArtifactsService
from .services.execution_connector import ExecutionConnectorService
from .services.execution_count_account import ExecutionCountAccountService
from .services.execution_count_account_group import ExecutionCountAccountGroupService
from .services.execution_record import ExecutionRecordService
from .services.execution_request import ExecutionRequestService
from .services.execution_summary_record import ExecutionSummaryRecordService
from .services.folder import FolderService
from .services.generic_connector_record import GenericConnectorRecordService
from .services.get_assignable_roles import GetAssignableRolesService
from .services.hl7_connector_record import Hl7ConnectorRecordService
from .services.installer_token import InstallerTokenService
from .services.integration_pack import IntegrationPackService
from .services.integration_pack_atom_attachment import (
    IntegrationPackAtomAttachmentService,
)
from .services.integration_pack_environment_attachment import (
    IntegrationPackEnvironmentAttachmentService,
)
from .services.integration_pack_instance import IntegrationPackInstanceService
from .services.java_rollback import JavaRollbackService
from .services.java_upgrade import JavaUpgradeService
from .services.merge_request import MergeRequestService
from .services.move_queue_request import MoveQueueRequestService
from .services.node_offboard import NodeOffboardService
from .services.odette_connector_record import OdetteConnectorRecordService
from .services.oftp2_connector_record import Oftp2ConnectorRecordService
from .services.packaged_component import PackagedComponentService
from .services.packaged_component_manifest import PackagedComponentManifestService
from .services.persisted_process_properties import PersistedProcessPropertiesService
from .services.process import ProcessService
from .services.process_atom_attachment import ProcessAtomAttachmentService
from .services.process_environment_attachment import ProcessEnvironmentAttachmentService
from .services.process_log import ProcessLogService
from .services.process_schedule_status import ProcessScheduleStatusService
from .services.process_schedules import ProcessSchedulesService
from .services.rerun_document import RerunDocumentService
from .services.role import RoleService
from .services.rosetta_net_connector_record import RosettaNetConnectorRecordService
from .services.runtime_release_schedule import RuntimeReleaseScheduleService
from .services.cancel_execution import CancelExecutionService
from .services.execute_process import ExecuteProcessService
from .services.worker import WorkerService
from .services.shared_web_server_log import SharedWebServerLogService
from .services.account_provision import AccountProvisionService
from .services.shared_server_information import SharedServerInformationService
from .services.shared_web_server import SharedWebServerService
from .services.throughput_account import ThroughputAccountService
from .services.throughput_account_group import ThroughputAccountGroupService
from .services.tradacoms_connector_record import TradacomsConnectorRecordService
from .services.trading_partner_component import TradingPartnerComponentService
from .services.trading_partner_processing_group import (
    TradingPartnerProcessingGroupService,
)
from .services.x12_connector_record import X12ConnectorRecordService
from .services.atom_disk_space import AtomDiskSpaceService
from .services.list_queues import ListQueuesService
from .services.listener_status import ListenerStatusService
from .services.organization_component import OrganizationComponentService
from .services.shared_communication_channel_component import (
    SharedCommunicationChannelComponentService,
)
from .services.account_group_integration_pack import AccountGroupIntegrationPackService
from .services.publisher_integration_pack import PublisherIntegrationPackService
from .services.release_integration_pack import ReleaseIntegrationPackService
from .services.release_integration_pack_status import (
    ReleaseIntegrationPackStatusService,
)
from .services.runtime_restart_request import RuntimeRestartRequestService
from .services.refresh_secrets_manager import RefreshSecretsManagerService
from .net.environment import Environment


class Boomi:
    def __init__(
        self,
        access_token: str = None,
        username: str = None,
        password: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
        account_id: str = "platform_account_ID",
    ):
        """
        Initializes Boomi the SDK class.
        """

        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self.as2_connector_record = As2ConnectorRecordService(base_url=self._base_url)
        self.account = AccountService(base_url=self._base_url)
        self.account_cloud_attachment_properties = (
            AccountCloudAttachmentPropertiesService(base_url=self._base_url)
        )
        self.account_cloud_attachment_quota = AccountCloudAttachmentQuotaService(
            base_url=self._base_url
        )
        self.account_group = AccountGroupService(base_url=self._base_url)
        self.account_group_account = AccountGroupAccountService(base_url=self._base_url)
        self.account_group_user_role = AccountGroupUserRoleService(
            base_url=self._base_url
        )
        self.account_sso_config = AccountSsoConfigService(base_url=self._base_url)
        self.account_user_federation = AccountUserFederationService(
            base_url=self._base_url
        )
        self.account_user_role = AccountUserRoleService(base_url=self._base_url)
        self.api_usage_count = ApiUsageCountService(base_url=self._base_url)
        self.atom = AtomService(base_url=self._base_url)
        self.atom_as2_artifacts = AtomAs2ArtifactsService(base_url=self._base_url)
        self.atom_connection_field_extension_summary = (
            AtomConnectionFieldExtensionSummaryService(base_url=self._base_url)
        )
        self.atom_connector_versions = AtomConnectorVersionsService(
            base_url=self._base_url
        )
        self.atom_counters = AtomCountersService(base_url=self._base_url)
        self.atom_log = AtomLogService(base_url=self._base_url)
        self.atom_purge = AtomPurgeService(base_url=self._base_url)
        self.atom_security_policies = AtomSecurityPoliciesService(
            base_url=self._base_url
        )
        self.atom_startup_properties = AtomStartupPropertiesService(
            base_url=self._base_url
        )
        self.atom_worker_log = AtomWorkerLogService(base_url=self._base_url)
        self.audit_log = AuditLogService(base_url=self._base_url)
        self.branch = BranchService(base_url=self._base_url)
        self.change_listener_status = ChangeListenerStatusService(
            base_url=self._base_url
        )
        self.clear_queue = ClearQueueService(base_url=self._base_url)
        self.cloud = CloudService(base_url=self._base_url)
        self.component = ComponentService(base_url=self._base_url)
        self.component_atom_attachment = ComponentAtomAttachmentService(
            base_url=self._base_url
        )
        self.component_diff_request = ComponentDiffRequestService(
            base_url=self._base_url
        )
        self.component_environment_attachment = ComponentEnvironmentAttachmentService(
            base_url=self._base_url
        )
        self.component_metadata = ComponentMetadataService(base_url=self._base_url)
        self.component_reference = ComponentReferenceService(base_url=self._base_url)
        self.connection_licensing_report = ConnectionLicensingReportService(
            base_url=self._base_url
        )
        self.connector = ConnectorService(base_url=self._base_url)
        self.connector_document = ConnectorDocumentService(base_url=self._base_url)
        self.custom_tracked_field = CustomTrackedFieldService(base_url=self._base_url)
        self.deployed_expired_certificate = DeployedExpiredCertificateService(
            base_url=self._base_url
        )
        self.deployed_package = DeployedPackageService(base_url=self._base_url)
        self.deployment = DeploymentService(base_url=self._base_url)
        self.document_count_account = DocumentCountAccountService(
            base_url=self._base_url
        )
        self.document_count_account_group = DocumentCountAccountGroupService(
            base_url=self._base_url
        )
        self.edifact_connector_record = EdifactConnectorRecordService(
            base_url=self._base_url
        )
        self.edi_custom_connector_record = EdiCustomConnectorRecordService(
            base_url=self._base_url
        )
        self.environment = EnvironmentService(base_url=self._base_url)
        self.environment_atom_attachment = EnvironmentAtomAttachmentService(
            base_url=self._base_url
        )
        self.environment_connection_field_extension_summary = (
            EnvironmentConnectionFieldExtensionSummaryService(base_url=self._base_url)
        )
        self.environment_extensions = EnvironmentExtensionsService(
            base_url=self._base_url
        )
        self.environment_map_extension = EnvironmentMapExtensionService(
            base_url=self._base_url
        )
        self.environment_map_extension_external_component = (
            EnvironmentMapExtensionExternalComponentService(base_url=self._base_url)
        )
        self.environment_map_extension_user_defined_function = (
            EnvironmentMapExtensionUserDefinedFunctionService(base_url=self._base_url)
        )
        self.environment_map_extension_user_defined_function_summary = (
            EnvironmentMapExtensionUserDefinedFunctionSummaryService(
                base_url=self._base_url
            )
        )
        self.environment_map_extensions_summary = (
            EnvironmentMapExtensionsSummaryService(base_url=self._base_url)
        )
        self.environment_role = EnvironmentRoleService(base_url=self._base_url)
        self.event = EventService(base_url=self._base_url)
        self.execution_artifacts = ExecutionArtifactsService(base_url=self._base_url)
        self.execution_connector = ExecutionConnectorService(base_url=self._base_url)
        self.execution_count_account = ExecutionCountAccountService(
            base_url=self._base_url
        )
        self.execution_count_account_group = ExecutionCountAccountGroupService(
            base_url=self._base_url
        )
        self.execution_record = ExecutionRecordService(base_url=self._base_url)
        self.execution_request = ExecutionRequestService(base_url=self._base_url)
        self.execution_summary_record = ExecutionSummaryRecordService(
            base_url=self._base_url
        )
        self.folder = FolderService(base_url=self._base_url)
        self.generic_connector_record = GenericConnectorRecordService(
            base_url=self._base_url
        )
        self.get_assignable_roles = GetAssignableRolesService(base_url=self._base_url)
        self.hl7_connector_record = Hl7ConnectorRecordService(base_url=self._base_url)
        self.installer_token = InstallerTokenService(base_url=self._base_url)
        self.integration_pack = IntegrationPackService(base_url=self._base_url)
        self.integration_pack_atom_attachment = IntegrationPackAtomAttachmentService(
            base_url=self._base_url
        )
        self.integration_pack_environment_attachment = (
            IntegrationPackEnvironmentAttachmentService(base_url=self._base_url)
        )
        self.integration_pack_instance = IntegrationPackInstanceService(
            base_url=self._base_url
        )
        self.java_rollback = JavaRollbackService(base_url=self._base_url)
        self.java_upgrade = JavaUpgradeService(base_url=self._base_url)
        self.merge_request = MergeRequestService(base_url=self._base_url)
        self.move_queue_request = MoveQueueRequestService(base_url=self._base_url)
        self.node_offboard = NodeOffboardService(base_url=self._base_url)
        self.odette_connector_record = OdetteConnectorRecordService(
            base_url=self._base_url
        )
        self.oftp2_connector_record = Oftp2ConnectorRecordService(
            base_url=self._base_url
        )
        self.packaged_component = PackagedComponentService(base_url=self._base_url)
        self.packaged_component_manifest = PackagedComponentManifestService(
            base_url=self._base_url
        )
        self.persisted_process_properties = PersistedProcessPropertiesService(
            base_url=self._base_url
        )
        self.process = ProcessService(base_url=self._base_url)
        self.process_atom_attachment = ProcessAtomAttachmentService(
            base_url=self._base_url
        )
        self.process_environment_attachment = ProcessEnvironmentAttachmentService(
            base_url=self._base_url
        )
        self.process_log = ProcessLogService(base_url=self._base_url)
        self.process_schedule_status = ProcessScheduleStatusService(
            base_url=self._base_url
        )
        self.process_schedules = ProcessSchedulesService(base_url=self._base_url)
        self.rerun_document = RerunDocumentService(base_url=self._base_url)
        self.role = RoleService(base_url=self._base_url)
        self.rosetta_net_connector_record = RosettaNetConnectorRecordService(
            base_url=self._base_url
        )
        self.runtime_release_schedule = RuntimeReleaseScheduleService(
            base_url=self._base_url
        )
        self.cancel_execution = CancelExecutionService(base_url=self._base_url)
        self.execute_process = ExecuteProcessService(base_url=self._base_url)
        self.worker = WorkerService(base_url=self._base_url)
        self.shared_web_server_log = SharedWebServerLogService(base_url=self._base_url)
        self.account_provision = AccountProvisionService(base_url=self._base_url)
        self.shared_server_information = SharedServerInformationService(
            base_url=self._base_url
        )
        self.shared_web_server = SharedWebServerService(base_url=self._base_url)
        self.throughput_account = ThroughputAccountService(base_url=self._base_url)
        self.throughput_account_group = ThroughputAccountGroupService(
            base_url=self._base_url
        )
        self.tradacoms_connector_record = TradacomsConnectorRecordService(
            base_url=self._base_url
        )
        self.trading_partner_component = TradingPartnerComponentService(
            base_url=self._base_url
        )
        self.trading_partner_processing_group = TradingPartnerProcessingGroupService(
            base_url=self._base_url
        )
        self.x12_connector_record = X12ConnectorRecordService(base_url=self._base_url)
        self.atom_disk_space = AtomDiskSpaceService(base_url=self._base_url)
        self.list_queues = ListQueuesService(base_url=self._base_url)
        self.listener_status = ListenerStatusService(base_url=self._base_url)
        self.organization_component = OrganizationComponentService(
            base_url=self._base_url
        )
        self.shared_communication_channel_component = (
            SharedCommunicationChannelComponentService(base_url=self._base_url)
        )
        self.account_group_integration_pack = AccountGroupIntegrationPackService(
            base_url=self._base_url
        )
        self.publisher_integration_pack = PublisherIntegrationPackService(
            base_url=self._base_url
        )
        self.release_integration_pack = ReleaseIntegrationPackService(
            base_url=self._base_url
        )
        self.release_integration_pack_status = ReleaseIntegrationPackStatusService(
            base_url=self._base_url
        )
        self.runtime_restart_request = RuntimeRestartRequestService(
            base_url=self._base_url
        )
        self.refresh_secrets_manager = RefreshSecretsManagerService(
            base_url=self._base_url
        )
        self.set_access_token(access_token)
        self.set_basic_auth(username=username, password=password)
        self._base_url_account_id = account_id
        self.set_base_url(self._base_url)
        self.set_timeout(timeout)

    def set_base_url(self, base_url: Union[Environment, str]):
        """
        Sets the base URL for the entire SDK.

        :param Union[Environment, str] base_url: The base URL to be set.
        :return: The SDK instance.
        """
        self._base_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        formatted_url = (self._base_url or Environment.DEFAULT.url).format(
            accountId=self._base_url_account_id
        )

        self.as2_connector_record.set_base_url(formatted_url)
        self.account.set_base_url(formatted_url)
        self.account_cloud_attachment_properties.set_base_url(formatted_url)
        self.account_cloud_attachment_quota.set_base_url(formatted_url)
        self.account_group.set_base_url(formatted_url)
        self.account_group_account.set_base_url(formatted_url)
        self.account_group_user_role.set_base_url(formatted_url)
        self.account_sso_config.set_base_url(formatted_url)
        self.account_user_federation.set_base_url(formatted_url)
        self.account_user_role.set_base_url(formatted_url)
        self.api_usage_count.set_base_url(formatted_url)
        self.atom.set_base_url(formatted_url)
        self.atom_as2_artifacts.set_base_url(formatted_url)
        self.atom_connection_field_extension_summary.set_base_url(formatted_url)
        self.atom_connector_versions.set_base_url(formatted_url)
        self.atom_counters.set_base_url(formatted_url)
        self.atom_log.set_base_url(formatted_url)
        self.atom_purge.set_base_url(formatted_url)
        self.atom_security_policies.set_base_url(formatted_url)
        self.atom_startup_properties.set_base_url(formatted_url)
        self.atom_worker_log.set_base_url(formatted_url)
        self.audit_log.set_base_url(formatted_url)
        self.branch.set_base_url(formatted_url)
        self.change_listener_status.set_base_url(formatted_url)
        self.clear_queue.set_base_url(formatted_url)
        self.cloud.set_base_url(formatted_url)
        self.component.set_base_url(formatted_url)
        self.component_atom_attachment.set_base_url(formatted_url)
        self.component_diff_request.set_base_url(formatted_url)
        self.component_environment_attachment.set_base_url(formatted_url)
        self.component_metadata.set_base_url(formatted_url)
        self.component_reference.set_base_url(formatted_url)
        self.connection_licensing_report.set_base_url(formatted_url)
        self.connector.set_base_url(formatted_url)
        self.connector_document.set_base_url(formatted_url)
        self.custom_tracked_field.set_base_url(formatted_url)
        self.deployed_expired_certificate.set_base_url(formatted_url)
        self.deployed_package.set_base_url(formatted_url)
        self.deployment.set_base_url(formatted_url)
        self.document_count_account.set_base_url(formatted_url)
        self.document_count_account_group.set_base_url(formatted_url)
        self.edifact_connector_record.set_base_url(formatted_url)
        self.edi_custom_connector_record.set_base_url(formatted_url)
        self.environment.set_base_url(formatted_url)
        self.environment_atom_attachment.set_base_url(formatted_url)
        self.environment_connection_field_extension_summary.set_base_url(formatted_url)
        self.environment_extensions.set_base_url(formatted_url)
        self.environment_map_extension.set_base_url(formatted_url)
        self.environment_map_extension_external_component.set_base_url(formatted_url)
        self.environment_map_extension_user_defined_function.set_base_url(formatted_url)
        self.environment_map_extension_user_defined_function_summary.set_base_url(
            formatted_url
        )
        self.environment_map_extensions_summary.set_base_url(formatted_url)
        self.environment_role.set_base_url(formatted_url)
        self.event.set_base_url(formatted_url)
        self.execution_artifacts.set_base_url(formatted_url)
        self.execution_connector.set_base_url(formatted_url)
        self.execution_count_account.set_base_url(formatted_url)
        self.execution_count_account_group.set_base_url(formatted_url)
        self.execution_record.set_base_url(formatted_url)
        self.execution_request.set_base_url(formatted_url)
        self.execution_summary_record.set_base_url(formatted_url)
        self.folder.set_base_url(formatted_url)
        self.generic_connector_record.set_base_url(formatted_url)
        self.get_assignable_roles.set_base_url(formatted_url)
        self.hl7_connector_record.set_base_url(formatted_url)
        self.installer_token.set_base_url(formatted_url)
        self.integration_pack.set_base_url(formatted_url)
        self.integration_pack_atom_attachment.set_base_url(formatted_url)
        self.integration_pack_environment_attachment.set_base_url(formatted_url)
        self.integration_pack_instance.set_base_url(formatted_url)
        self.java_rollback.set_base_url(formatted_url)
        self.java_upgrade.set_base_url(formatted_url)
        self.merge_request.set_base_url(formatted_url)
        self.move_queue_request.set_base_url(formatted_url)
        self.node_offboard.set_base_url(formatted_url)
        self.odette_connector_record.set_base_url(formatted_url)
        self.oftp2_connector_record.set_base_url(formatted_url)
        self.packaged_component.set_base_url(formatted_url)
        self.packaged_component_manifest.set_base_url(formatted_url)
        self.persisted_process_properties.set_base_url(formatted_url)
        self.process.set_base_url(formatted_url)
        self.process_atom_attachment.set_base_url(formatted_url)
        self.process_environment_attachment.set_base_url(formatted_url)
        self.process_log.set_base_url(formatted_url)
        self.process_schedule_status.set_base_url(formatted_url)
        self.process_schedules.set_base_url(formatted_url)
        self.rerun_document.set_base_url(formatted_url)
        self.role.set_base_url(formatted_url)
        self.rosetta_net_connector_record.set_base_url(formatted_url)
        self.runtime_release_schedule.set_base_url(formatted_url)
        self.cancel_execution.set_base_url(formatted_url)
        self.execute_process.set_base_url(formatted_url)
        self.worker.set_base_url(formatted_url)
        self.shared_web_server_log.set_base_url(formatted_url)
        self.account_provision.set_base_url(formatted_url)
        self.shared_server_information.set_base_url(formatted_url)
        self.shared_web_server.set_base_url(formatted_url)
        self.throughput_account.set_base_url(formatted_url)
        self.throughput_account_group.set_base_url(formatted_url)
        self.tradacoms_connector_record.set_base_url(formatted_url)
        self.trading_partner_component.set_base_url(formatted_url)
        self.trading_partner_processing_group.set_base_url(formatted_url)
        self.x12_connector_record.set_base_url(formatted_url)
        self.atom_disk_space.set_base_url(formatted_url)
        self.list_queues.set_base_url(formatted_url)
        self.listener_status.set_base_url(formatted_url)
        self.organization_component.set_base_url(formatted_url)
        self.shared_communication_channel_component.set_base_url(formatted_url)
        self.account_group_integration_pack.set_base_url(formatted_url)
        self.publisher_integration_pack.set_base_url(formatted_url)
        self.release_integration_pack.set_base_url(formatted_url)
        self.release_integration_pack_status.set_base_url(formatted_url)
        self.runtime_restart_request.set_base_url(formatted_url)
        self.refresh_secrets_manager.set_base_url(formatted_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.as2_connector_record.set_access_token(access_token)
        self.account.set_access_token(access_token)
        self.account_cloud_attachment_properties.set_access_token(access_token)
        self.account_cloud_attachment_quota.set_access_token(access_token)
        self.account_group.set_access_token(access_token)
        self.account_group_account.set_access_token(access_token)
        self.account_group_user_role.set_access_token(access_token)
        self.account_sso_config.set_access_token(access_token)
        self.account_user_federation.set_access_token(access_token)
        self.account_user_role.set_access_token(access_token)
        self.api_usage_count.set_access_token(access_token)
        self.atom.set_access_token(access_token)
        self.atom_as2_artifacts.set_access_token(access_token)
        self.atom_connection_field_extension_summary.set_access_token(access_token)
        self.atom_connector_versions.set_access_token(access_token)
        self.atom_counters.set_access_token(access_token)
        self.atom_log.set_access_token(access_token)
        self.atom_purge.set_access_token(access_token)
        self.atom_security_policies.set_access_token(access_token)
        self.atom_startup_properties.set_access_token(access_token)
        self.atom_worker_log.set_access_token(access_token)
        self.audit_log.set_access_token(access_token)
        self.branch.set_access_token(access_token)
        self.change_listener_status.set_access_token(access_token)
        self.clear_queue.set_access_token(access_token)
        self.cloud.set_access_token(access_token)
        self.component.set_access_token(access_token)
        self.component_atom_attachment.set_access_token(access_token)
        self.component_diff_request.set_access_token(access_token)
        self.component_environment_attachment.set_access_token(access_token)
        self.component_metadata.set_access_token(access_token)
        self.component_reference.set_access_token(access_token)
        self.connection_licensing_report.set_access_token(access_token)
        self.connector.set_access_token(access_token)
        self.connector_document.set_access_token(access_token)
        self.custom_tracked_field.set_access_token(access_token)
        self.deployed_expired_certificate.set_access_token(access_token)
        self.deployed_package.set_access_token(access_token)
        self.deployment.set_access_token(access_token)
        self.document_count_account.set_access_token(access_token)
        self.document_count_account_group.set_access_token(access_token)
        self.edifact_connector_record.set_access_token(access_token)
        self.edi_custom_connector_record.set_access_token(access_token)
        self.environment.set_access_token(access_token)
        self.environment_atom_attachment.set_access_token(access_token)
        self.environment_connection_field_extension_summary.set_access_token(
            access_token
        )
        self.environment_extensions.set_access_token(access_token)
        self.environment_map_extension.set_access_token(access_token)
        self.environment_map_extension_external_component.set_access_token(access_token)
        self.environment_map_extension_user_defined_function.set_access_token(
            access_token
        )
        self.environment_map_extension_user_defined_function_summary.set_access_token(
            access_token
        )
        self.environment_map_extensions_summary.set_access_token(access_token)
        self.environment_role.set_access_token(access_token)
        self.event.set_access_token(access_token)
        self.execution_artifacts.set_access_token(access_token)
        self.execution_connector.set_access_token(access_token)
        self.execution_count_account.set_access_token(access_token)
        self.execution_count_account_group.set_access_token(access_token)
        self.execution_record.set_access_token(access_token)
        self.execution_request.set_access_token(access_token)
        self.execution_summary_record.set_access_token(access_token)
        self.folder.set_access_token(access_token)
        self.generic_connector_record.set_access_token(access_token)
        self.get_assignable_roles.set_access_token(access_token)
        self.hl7_connector_record.set_access_token(access_token)
        self.installer_token.set_access_token(access_token)
        self.integration_pack.set_access_token(access_token)
        self.integration_pack_atom_attachment.set_access_token(access_token)
        self.integration_pack_environment_attachment.set_access_token(access_token)
        self.integration_pack_instance.set_access_token(access_token)
        self.java_rollback.set_access_token(access_token)
        self.java_upgrade.set_access_token(access_token)
        self.merge_request.set_access_token(access_token)
        self.move_queue_request.set_access_token(access_token)
        self.node_offboard.set_access_token(access_token)
        self.odette_connector_record.set_access_token(access_token)
        self.oftp2_connector_record.set_access_token(access_token)
        self.packaged_component.set_access_token(access_token)
        self.packaged_component_manifest.set_access_token(access_token)
        self.persisted_process_properties.set_access_token(access_token)
        self.process.set_access_token(access_token)
        self.process_atom_attachment.set_access_token(access_token)
        self.process_environment_attachment.set_access_token(access_token)
        self.process_log.set_access_token(access_token)
        self.process_schedule_status.set_access_token(access_token)
        self.process_schedules.set_access_token(access_token)
        self.rerun_document.set_access_token(access_token)
        self.role.set_access_token(access_token)
        self.rosetta_net_connector_record.set_access_token(access_token)
        self.runtime_release_schedule.set_access_token(access_token)
        self.cancel_execution.set_access_token(access_token)
        self.execute_process.set_access_token(access_token)
        self.worker.set_access_token(access_token)
        self.shared_web_server_log.set_access_token(access_token)
        self.account_provision.set_access_token(access_token)
        self.shared_server_information.set_access_token(access_token)
        self.shared_web_server.set_access_token(access_token)
        self.throughput_account.set_access_token(access_token)
        self.throughput_account_group.set_access_token(access_token)
        self.tradacoms_connector_record.set_access_token(access_token)
        self.trading_partner_component.set_access_token(access_token)
        self.trading_partner_processing_group.set_access_token(access_token)
        self.x12_connector_record.set_access_token(access_token)
        self.atom_disk_space.set_access_token(access_token)
        self.list_queues.set_access_token(access_token)
        self.listener_status.set_access_token(access_token)
        self.organization_component.set_access_token(access_token)
        self.shared_communication_channel_component.set_access_token(access_token)
        self.account_group_integration_pack.set_access_token(access_token)
        self.publisher_integration_pack.set_access_token(access_token)
        self.release_integration_pack.set_access_token(access_token)
        self.release_integration_pack_status.set_access_token(access_token)
        self.runtime_restart_request.set_access_token(access_token)
        self.refresh_secrets_manager.set_access_token(access_token)

        return self

    def set_basic_auth(self, username: str, password: str):
        """
        Sets the username and password for the entire SDK.
        """
        self.as2_connector_record.set_basic_auth(username=username, password=password)
        self.account.set_basic_auth(username=username, password=password)
        self.account_cloud_attachment_properties.set_basic_auth(
            username=username, password=password
        )
        self.account_cloud_attachment_quota.set_basic_auth(
            username=username, password=password
        )
        self.account_group.set_basic_auth(username=username, password=password)
        self.account_group_account.set_basic_auth(username=username, password=password)
        self.account_group_user_role.set_basic_auth(
            username=username, password=password
        )
        self.account_sso_config.set_basic_auth(username=username, password=password)
        self.account_user_federation.set_basic_auth(
            username=username, password=password
        )
        self.account_user_role.set_basic_auth(username=username, password=password)
        self.api_usage_count.set_basic_auth(username=username, password=password)
        self.atom.set_basic_auth(username=username, password=password)
        self.atom_as2_artifacts.set_basic_auth(username=username, password=password)
        self.atom_connection_field_extension_summary.set_basic_auth(
            username=username, password=password
        )
        self.atom_connector_versions.set_basic_auth(
            username=username, password=password
        )
        self.atom_counters.set_basic_auth(username=username, password=password)
        self.atom_log.set_basic_auth(username=username, password=password)
        self.atom_purge.set_basic_auth(username=username, password=password)
        self.atom_security_policies.set_basic_auth(username=username, password=password)
        self.atom_startup_properties.set_basic_auth(
            username=username, password=password
        )
        self.atom_worker_log.set_basic_auth(username=username, password=password)
        self.audit_log.set_basic_auth(username=username, password=password)
        self.branch.set_basic_auth(username=username, password=password)
        self.change_listener_status.set_basic_auth(username=username, password=password)
        self.clear_queue.set_basic_auth(username=username, password=password)
        self.cloud.set_basic_auth(username=username, password=password)
        self.component.set_basic_auth(username=username, password=password)
        self.component_atom_attachment.set_basic_auth(
            username=username, password=password
        )
        self.component_diff_request.set_basic_auth(username=username, password=password)
        self.component_environment_attachment.set_basic_auth(
            username=username, password=password
        )
        self.component_metadata.set_basic_auth(username=username, password=password)
        self.component_reference.set_basic_auth(username=username, password=password)
        self.connection_licensing_report.set_basic_auth(
            username=username, password=password
        )
        self.connector.set_basic_auth(username=username, password=password)
        self.connector_document.set_basic_auth(username=username, password=password)
        self.custom_tracked_field.set_basic_auth(username=username, password=password)
        self.deployed_expired_certificate.set_basic_auth(
            username=username, password=password
        )
        self.deployed_package.set_basic_auth(username=username, password=password)
        self.deployment.set_basic_auth(username=username, password=password)
        self.document_count_account.set_basic_auth(username=username, password=password)
        self.document_count_account_group.set_basic_auth(
            username=username, password=password
        )
        self.edifact_connector_record.set_basic_auth(
            username=username, password=password
        )
        self.edi_custom_connector_record.set_basic_auth(
            username=username, password=password
        )
        self.environment.set_basic_auth(username=username, password=password)
        self.environment_atom_attachment.set_basic_auth(
            username=username, password=password
        )
        self.environment_connection_field_extension_summary.set_basic_auth(
            username=username, password=password
        )
        self.environment_extensions.set_basic_auth(username=username, password=password)
        self.environment_map_extension.set_basic_auth(
            username=username, password=password
        )
        self.environment_map_extension_external_component.set_basic_auth(
            username=username, password=password
        )
        self.environment_map_extension_user_defined_function.set_basic_auth(
            username=username, password=password
        )
        self.environment_map_extension_user_defined_function_summary.set_basic_auth(
            username=username, password=password
        )
        self.environment_map_extensions_summary.set_basic_auth(
            username=username, password=password
        )
        self.environment_role.set_basic_auth(username=username, password=password)
        self.event.set_basic_auth(username=username, password=password)
        self.execution_artifacts.set_basic_auth(username=username, password=password)
        self.execution_connector.set_basic_auth(username=username, password=password)
        self.execution_count_account.set_basic_auth(
            username=username, password=password
        )
        self.execution_count_account_group.set_basic_auth(
            username=username, password=password
        )
        self.execution_record.set_basic_auth(username=username, password=password)
        self.execution_request.set_basic_auth(username=username, password=password)
        self.execution_summary_record.set_basic_auth(
            username=username, password=password
        )
        self.folder.set_basic_auth(username=username, password=password)
        self.generic_connector_record.set_basic_auth(
            username=username, password=password
        )
        self.get_assignable_roles.set_basic_auth(username=username, password=password)
        self.hl7_connector_record.set_basic_auth(username=username, password=password)
        self.installer_token.set_basic_auth(username=username, password=password)
        self.integration_pack.set_basic_auth(username=username, password=password)
        self.integration_pack_atom_attachment.set_basic_auth(
            username=username, password=password
        )
        self.integration_pack_environment_attachment.set_basic_auth(
            username=username, password=password
        )
        self.integration_pack_instance.set_basic_auth(
            username=username, password=password
        )
        self.java_rollback.set_basic_auth(username=username, password=password)
        self.java_upgrade.set_basic_auth(username=username, password=password)
        self.merge_request.set_basic_auth(username=username, password=password)
        self.move_queue_request.set_basic_auth(username=username, password=password)
        self.node_offboard.set_basic_auth(username=username, password=password)
        self.odette_connector_record.set_basic_auth(
            username=username, password=password
        )
        self.oftp2_connector_record.set_basic_auth(username=username, password=password)
        self.packaged_component.set_basic_auth(username=username, password=password)
        self.packaged_component_manifest.set_basic_auth(
            username=username, password=password
        )
        self.persisted_process_properties.set_basic_auth(
            username=username, password=password
        )
        self.process.set_basic_auth(username=username, password=password)
        self.process_atom_attachment.set_basic_auth(
            username=username, password=password
        )
        self.process_environment_attachment.set_basic_auth(
            username=username, password=password
        )
        self.process_log.set_basic_auth(username=username, password=password)
        self.process_schedule_status.set_basic_auth(
            username=username, password=password
        )
        self.process_schedules.set_basic_auth(username=username, password=password)
        self.rerun_document.set_basic_auth(username=username, password=password)
        self.role.set_basic_auth(username=username, password=password)
        self.rosetta_net_connector_record.set_basic_auth(
            username=username, password=password
        )
        self.runtime_release_schedule.set_basic_auth(
            username=username, password=password
        )
        self.cancel_execution.set_basic_auth(username=username, password=password)
        self.execute_process.set_basic_auth(username=username, password=password)
        self.worker.set_basic_auth(username=username, password=password)
        self.shared_web_server_log.set_basic_auth(username=username, password=password)
        self.account_provision.set_basic_auth(username=username, password=password)
        self.shared_server_information.set_basic_auth(
            username=username, password=password
        )
        self.shared_web_server.set_basic_auth(username=username, password=password)
        self.throughput_account.set_basic_auth(username=username, password=password)
        self.throughput_account_group.set_basic_auth(
            username=username, password=password
        )
        self.tradacoms_connector_record.set_basic_auth(
            username=username, password=password
        )
        self.trading_partner_component.set_basic_auth(
            username=username, password=password
        )
        self.trading_partner_processing_group.set_basic_auth(
            username=username, password=password
        )
        self.x12_connector_record.set_basic_auth(username=username, password=password)
        self.atom_disk_space.set_basic_auth(username=username, password=password)
        self.list_queues.set_basic_auth(username=username, password=password)
        self.listener_status.set_basic_auth(username=username, password=password)
        self.organization_component.set_basic_auth(username=username, password=password)
        self.shared_communication_channel_component.set_basic_auth(
            username=username, password=password
        )
        self.account_group_integration_pack.set_basic_auth(
            username=username, password=password
        )
        self.publisher_integration_pack.set_basic_auth(
            username=username, password=password
        )
        self.release_integration_pack.set_basic_auth(
            username=username, password=password
        )
        self.release_integration_pack_status.set_basic_auth(
            username=username, password=password
        )
        self.runtime_restart_request.set_basic_auth(
            username=username, password=password
        )
        self.refresh_secrets_manager.set_basic_auth(
            username=username, password=password
        )

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.as2_connector_record.set_timeout(timeout)
        self.account.set_timeout(timeout)
        self.account_cloud_attachment_properties.set_timeout(timeout)
        self.account_cloud_attachment_quota.set_timeout(timeout)
        self.account_group.set_timeout(timeout)
        self.account_group_account.set_timeout(timeout)
        self.account_group_user_role.set_timeout(timeout)
        self.account_sso_config.set_timeout(timeout)
        self.account_user_federation.set_timeout(timeout)
        self.account_user_role.set_timeout(timeout)
        self.api_usage_count.set_timeout(timeout)
        self.atom.set_timeout(timeout)
        self.atom_as2_artifacts.set_timeout(timeout)
        self.atom_connection_field_extension_summary.set_timeout(timeout)
        self.atom_connector_versions.set_timeout(timeout)
        self.atom_counters.set_timeout(timeout)
        self.atom_log.set_timeout(timeout)
        self.atom_purge.set_timeout(timeout)
        self.atom_security_policies.set_timeout(timeout)
        self.atom_startup_properties.set_timeout(timeout)
        self.atom_worker_log.set_timeout(timeout)
        self.audit_log.set_timeout(timeout)
        self.branch.set_timeout(timeout)
        self.change_listener_status.set_timeout(timeout)
        self.clear_queue.set_timeout(timeout)
        self.cloud.set_timeout(timeout)
        self.component.set_timeout(timeout)
        self.component_atom_attachment.set_timeout(timeout)
        self.component_diff_request.set_timeout(timeout)
        self.component_environment_attachment.set_timeout(timeout)
        self.component_metadata.set_timeout(timeout)
        self.component_reference.set_timeout(timeout)
        self.connection_licensing_report.set_timeout(timeout)
        self.connector.set_timeout(timeout)
        self.connector_document.set_timeout(timeout)
        self.custom_tracked_field.set_timeout(timeout)
        self.deployed_expired_certificate.set_timeout(timeout)
        self.deployed_package.set_timeout(timeout)
        self.deployment.set_timeout(timeout)
        self.document_count_account.set_timeout(timeout)
        self.document_count_account_group.set_timeout(timeout)
        self.edifact_connector_record.set_timeout(timeout)
        self.edi_custom_connector_record.set_timeout(timeout)
        self.environment.set_timeout(timeout)
        self.environment_atom_attachment.set_timeout(timeout)
        self.environment_connection_field_extension_summary.set_timeout(timeout)
        self.environment_extensions.set_timeout(timeout)
        self.environment_map_extension.set_timeout(timeout)
        self.environment_map_extension_external_component.set_timeout(timeout)
        self.environment_map_extension_user_defined_function.set_timeout(timeout)
        self.environment_map_extension_user_defined_function_summary.set_timeout(
            timeout
        )
        self.environment_map_extensions_summary.set_timeout(timeout)
        self.environment_role.set_timeout(timeout)
        self.event.set_timeout(timeout)
        self.execution_artifacts.set_timeout(timeout)
        self.execution_connector.set_timeout(timeout)
        self.execution_count_account.set_timeout(timeout)
        self.execution_count_account_group.set_timeout(timeout)
        self.execution_record.set_timeout(timeout)
        self.execution_request.set_timeout(timeout)
        self.execution_summary_record.set_timeout(timeout)
        self.folder.set_timeout(timeout)
        self.generic_connector_record.set_timeout(timeout)
        self.get_assignable_roles.set_timeout(timeout)
        self.hl7_connector_record.set_timeout(timeout)
        self.installer_token.set_timeout(timeout)
        self.integration_pack.set_timeout(timeout)
        self.integration_pack_atom_attachment.set_timeout(timeout)
        self.integration_pack_environment_attachment.set_timeout(timeout)
        self.integration_pack_instance.set_timeout(timeout)
        self.java_rollback.set_timeout(timeout)
        self.java_upgrade.set_timeout(timeout)
        self.merge_request.set_timeout(timeout)
        self.move_queue_request.set_timeout(timeout)
        self.node_offboard.set_timeout(timeout)
        self.odette_connector_record.set_timeout(timeout)
        self.oftp2_connector_record.set_timeout(timeout)
        self.packaged_component.set_timeout(timeout)
        self.packaged_component_manifest.set_timeout(timeout)
        self.persisted_process_properties.set_timeout(timeout)
        self.process.set_timeout(timeout)
        self.process_atom_attachment.set_timeout(timeout)
        self.process_environment_attachment.set_timeout(timeout)
        self.process_log.set_timeout(timeout)
        self.process_schedule_status.set_timeout(timeout)
        self.process_schedules.set_timeout(timeout)
        self.rerun_document.set_timeout(timeout)
        self.role.set_timeout(timeout)
        self.rosetta_net_connector_record.set_timeout(timeout)
        self.runtime_release_schedule.set_timeout(timeout)
        self.cancel_execution.set_timeout(timeout)
        self.execute_process.set_timeout(timeout)
        self.worker.set_timeout(timeout)
        self.shared_web_server_log.set_timeout(timeout)
        self.account_provision.set_timeout(timeout)
        self.shared_server_information.set_timeout(timeout)
        self.shared_web_server.set_timeout(timeout)
        self.throughput_account.set_timeout(timeout)
        self.throughput_account_group.set_timeout(timeout)
        self.tradacoms_connector_record.set_timeout(timeout)
        self.trading_partner_component.set_timeout(timeout)
        self.trading_partner_processing_group.set_timeout(timeout)
        self.x12_connector_record.set_timeout(timeout)
        self.atom_disk_space.set_timeout(timeout)
        self.list_queues.set_timeout(timeout)
        self.listener_status.set_timeout(timeout)
        self.organization_component.set_timeout(timeout)
        self.shared_communication_channel_component.set_timeout(timeout)
        self.account_group_integration_pack.set_timeout(timeout)
        self.publisher_integration_pack.set_timeout(timeout)
        self.release_integration_pack.set_timeout(timeout)
        self.release_integration_pack_status.set_timeout(timeout)
        self.runtime_restart_request.set_timeout(timeout)
        self.refresh_secrets_manager.set_timeout(timeout)

        return self

    def set_account_id(self, account_id: str):
        """
        Sets the account_id server variable for the entire SDK.

        :param str account_id: The account_id to be set.
        :return: The SDK instance.
        """
        self._base_url_account_id = account_id
        self.set_base_url(self._base_url)
        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
