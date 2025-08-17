# Boomi Python SDK Examples

This directory contains comprehensive examples demonstrating the Boomi Python SDK organized by CI/CD lifecycle stages.

## 🚀 Quick Start

```bash
# Set up environment
export BOOMI_ACCOUNT="your-account-id"
export BOOMI_USER="your-username" 
export BOOMI_SECRET="your-password"

# Run a basic example
cd examples/12_utilities
PYTHONPATH=../../src python sample.py
```

## 📁 CI/CD Lifecycle Organization

Examples are organized by integration development lifecycle stages:

### **01_discover_analyze/** - Find & Analyze Components
- `list_all_components.py` - List all components with metadata ✅
- `query_process_components.py` - Query specific component types ✅  
- `find_where_used.py` - Find components that use a specific component ✅
- `find_what_uses.py` - Find what a component uses ✅
- `folder_structure.py` - Analyze folder structure ✅
- `manage_folders.py` - Organize components with folders 🚧

### **02_create_components/** - Create & Modify Components
- `create_process_component.py` - Create new processes ✅
- `get_component.py` - Retrieve component details ✅
- `update_component.py` - Update existing components ✅
- `update_component_xml.py` - Update with raw XML ✅
- `clone_component.py` - Clone/copy components 🚧
- `delete_component.py` - Safe component deletion 🚧

### **03_build_integration/** - Build Integration from Components
- `bulk_get_components.py` - Retrieve multiple components ✅
- `update_components.py` - Batch update components ✅
- `update_working_components.py` - Update specific component sets ✅
- `update_final_working.py` - Finalize component updates ✅

### **04_environment_setup/** - Environment Configuration
- `create_environment.py` - Create new environments ✅
- `get_environment.py` - Retrieve environment details ✅
- `list_environments.py` - List all environments ✅
- `update_environment.py` - Update environment settings ✅
- `delete_environment.py` - Delete environments ✅
- `query_environments.py` - Query environments with filters ✅
- `manage_roles.py` - Manage user roles and permissions 🚧

### **05_runtime_setup/** - Runtime (Atom) Management
- `list_runtimes.py` - List available runtimes ✅
- `get_runtime.py` - Get runtime details ✅
- `get_runtime_status.py` - Check runtime status ✅
- `update_runtime.py` - Update runtime configuration ✅
- `delete_runtime.py` - Delete runtimes ✅
- `create_installer_token.py` - Generate installer tokens ✅
- `create_environment_atom_attachment.py` - Attach runtime to environment ✅
- `query_environment_atom_attachments.py` - Query runtime attachments ✅
- `detach_runtime_from_environment.py` - Detach runtime from environment ✅

### **06_package_deploy/** - Package & Deploy Components
- `attach_component_to_environment.py` - Attach components to environments ✅
- `attach_component_to_atom.py` - Attach components to runtimes ✅
- `query_component_attachments.py` - Query component attachments ✅
- `create_packaged_component.py` - Package components for deployment 🚨
- `create_deployed_package.py` - Deploy packages 🚨
- `get_packaged_component.py` - Get package details 🚧
- `query_packaged_components.py` - Query packages 🚧
- `query_deployed_packages.py` - Query deployments 🚧
- `promote_package_to_environment.py` - Promote between environments 🚧
- `create_deployment.py` - Create deployment objects 🚧
- `manage_integration_packs.py` - Manage integration packs 🚧

### **07_configure_deployment/** - Configure Deployment Settings
- `get_environment_extensions.py` - Get environment extensions ✅
- `query_environment_extensions.py` - Query extensions ✅
- `update_environment_extensions.py` - Update extensions ✅
- `get_environment_simple.py` - Get basic environment info ✅
- `manage_process_schedules.py` - Configure process schedules 🚧

### **08_execute_test/** - Execute & Test Processes
- `execution_records.py` - Query execution records ✅
- `execute_process.py` - Execute processes 🚨
- `execute_process_with_payload.py` - Execute with data payload 🚨
- `cancel_execution.py` - Cancel running executions 🚧

### **09_monitor_validate/** - Monitor & Validate Execution
- `download_execution_artifacts.py` - Download execution outputs 🚨
- `download_process_log.py` - Download execution logs 🚨
- `poll_execution_status.py` - Monitor execution progress 🚨
- `get_execution_summary.py` - Get execution summaries 🚧
- `query_audit_logs.py` - Query audit logs 🚧
- `query_events.py` - Query system events 🚧

### **10_version_compare/** - Version Control & Comparison
- `compare_component_versions.py` - Compare component versions ✅

### **11_troubleshoot_fix/** - Troubleshoot & Fix Issues
- `get_error_details.py` - Analyze errors 🚧
- `retry_failed_execution.py` - Retry failed executions 🚧
- `manage_queues.py` - Manage execution queues 🚧

### **12_utilities/** - Helper Utilities
- `sample.py` - Basic SDK demonstration ✅
- `install.sh` / `install.cmd` - SDK installation scripts ✅
- `async_operations.py` - Handle async operations 🚧
- `manage_connectors.py` - Manage connector configurations 🚧

## 📊 Status Legend

- ✅ **Implemented** - Working example with real SDK calls
- 🚨 **Critical TODO** - Must implement (pipeline blocker)
- 🚧 **TODO** - Planned for implementation
- 📋 **Documentation** - Usage guides and references

## 🔧 Usage Patterns

### Running Examples
```bash
# Set Python path to include SDK
export PYTHONPATH=/path/to/boomi-python/src

# Run specific example
python examples/02_create_components/get_component.py COMPONENT_ID
```

### Environment Variables
```bash
export BOOMI_ACCOUNT="your-account-id"
export BOOMI_USER="your-username"
export BOOMI_SECRET="your-password"
```

### Common Options
Most examples support standard options:
- Component ID arguments for component-specific operations
- Environment ID arguments for environment operations
- `--help` for usage information

## 🏗️ Architecture

- **One Endpoint Per File**: Each example focuses on a single SDK endpoint
- **Lifecycle Organization**: Examples follow CI/CD integration development stages
- **Self-Contained**: Each example is independently runnable
- **Error Handling**: Comprehensive error handling and user feedback

## 📚 Additional Documentation

- `README_LIFECYCLE.md` - Detailed lifecycle documentation with implementation status
- Individual file docstrings - Specific usage and requirements
- CLAUDE.md - Development guidelines and testing requirements

## 🎯 Getting Started

1. **Setup**: Install SDK and set environment variables
2. **Explore**: Start with `12_utilities/sample.py` for basic functionality
3. **Discover**: Use `01_discover_analyze/` examples to explore your account
4. **Build**: Follow the lifecycle stages for complete integration development

For detailed implementation status and priorities, see `README_LIFECYCLE.md`.