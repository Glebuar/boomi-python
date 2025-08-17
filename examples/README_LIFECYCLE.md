# 🚀 Boomi CI/CD Lifecycle Examples

This directory contains examples organized by the complete integration development lifecycle.

## 📁 Folder Structure

### **01_discover_analyze/** - Find & Analyze Components
- ✅ `list_all_components.py` - List all components with metadata
- ✅ `query_process_components.py` - Query specific component types  
- ✅ `find_where_used.py` - Find who uses a component
- ✅ `find_what_uses.py` - Find what a component uses
- ✅ `folder_structure.py` - Analyze folder structure
- 🚧 `search_components_by_name.py` - **TODO: Search by name pattern**
- 🚧 `get_component_history.py` - **TODO: Get version history**

### **02_create_components/** - Create & Modify Components
- ✅ `create_process_component.py` - Create new process
- ✅ `get_component.py` - Retrieve component details
- ✅ `update_component.py` - Update existing component
- ✅ `update_component_xml.py` - Update with raw XML
- 🚧 `delete_component.py` - **TODO: Delete component safely**
- 🚧 `clone_component.py` - **TODO: Clone existing component**

### **03_build_integration/** - Assemble Integrations
- ✅ `bulk_get_components.py` - Retrieve multiple components
- ✅ `update_components.py` - Bulk update components
- ✅ `update_final_working.py` - Update working components
- ✅ `update_working_components.py` - Working component updates

### **04_environment_setup/** - Environment Management
- ✅ `create_environment.py` - Create new environment
- ✅ `get_environment.py` - Get environment details
- ✅ `update_environment.py` - Update environment settings
- ✅ `delete_environment.py` - Delete environment
- ✅ `list_environments.py` - List all environments

### **05_runtime_setup/** - Runtime Management
- ✅ `create_installer_token.py` - Create runtime installer
- ✅ `delete_runtime.py` - Delete runtime
- ✅ `get_runtime.py` - Get runtime details
- ✅ `get_runtime_status.py` - Check runtime status
- ✅ `list_runtimes.py` - List all runtimes
- ✅ `update_runtime.py` - Update runtime settings
- ✅ `attach_runtime_to_environment.py` - Attach runtime to env
- ✅ `detach_runtime_from_environment.py` - Detach runtime
- ✅ `query_environment_runtime_attachments.py` - Query attachments

### **06_package_deploy/** - 🚨 Package & Deploy (CRITICAL)
- ✅ `attach_component_to_environment.py` - Basic component attachment
- ✅ `attach_component_to_atom.py` - Attach to specific runtime
- ✅ `query_component_attachments.py` - Query attachments
- 🚨 `create_packaged_component.py` - **CRITICAL TODO: Create packages**
- 🚨 `get_packaged_component.py` - **CRITICAL TODO: Get package details**  
- 🚨 `create_deployed_package.py` - **CRITICAL TODO: Deploy packages**
- 🚨 `promote_package_to_environment.py` - **CRITICAL TODO: Promote packages**
- 🚧 `query_packaged_components.py` - **TODO: List packages**
- 🚧 `query_deployed_packages.py` - **TODO: List deployments**

### **07_configure_deployment/** - Post-Deploy Configuration
- ✅ `get_environment_extensions.py` - Get environment config
- ✅ `update_environment_extensions.py` - Update environment config
- ✅ `query_environment_extensions.py` - Query environment settings
- ✅ `get_environment_simple.py` - Simple environment access

### **08_execute_test/** - 🚨 Execute & Test (CRITICAL)
- ✅ `execution_records.py` - Query execution records
- 🚨 `execute_process.py` - **CRITICAL TODO: Execute processes**
- 🚨 `execute_process_with_payload.py` - **CRITICAL TODO: Execute with data**
- 🚧 `cancel_execution.py` - **TODO: Cancel executions**

### **09_monitor_validate/** - 🚨 Monitor & Validate (CRITICAL)
- 🚨 `poll_execution_status.py` - **CRITICAL TODO: Monitor execution**
- 🚨 `download_process_log.py` - **CRITICAL TODO: Download logs**
- 🚨 `download_execution_artifacts.py` - **CRITICAL TODO: Download outputs**
- 🚧 `get_execution_summary.py` - **TODO: Get execution metrics**
- 🚧 `query_audit_logs.py` - **TODO: Query audit logs**

### **10_version_compare/** - Version & Change Management
- ✅ `compare_component_versions.py` - Compare component versions

### **11_troubleshoot_fix/** - Debug & Fix Issues
- 🚧 `get_error_details.py` - **TODO: Analyze errors**
- 🚧 `retry_failed_execution.py` - **TODO: Retry failures**

### **12_utilities/** - Helper Utilities
- Common functions and utilities

## 🚨 Critical Implementation Gaps

### **Pipeline Blockers (Must Implement First):**
1. **Package Creation** - `create_packaged_component.py`
2. **Package Deployment** - `create_deployed_package.py`
3. **Process Execution** - `execute_process.py`
4. **Execution Monitoring** - `poll_execution_status.py`
5. **Log Collection** - `download_process_log.py`

### **Current Pipeline Status:**
```
Discover → Create → Build → Package → Deploy → Configure → Execute → Monitor → Fix
   ✅       ✅       ⚠️       ❌        ❌         ✅         ❌        ❌       ❌
```

**Overall Completion: ~35%**

## 🎯 Implementation Priority

### **Phase 1 (Critical Path):**
- Implement 5 pipeline blocker examples
- Enable basic CI/CD pipeline functionality

### **Phase 2 (Production Ready):**
- Complete remaining package/deploy examples
- Add monitoring and validation features

### **Phase 3 (Advanced Features):**
- Add troubleshooting and error handling
- Implement advanced workflow features

## 📚 Usage

Each folder contains working examples and TODO placeholders. Start with implementing the critical examples marked with 🚨 to enable the complete CI/CD pipeline.

Legend:
- ✅ = Implemented and working
- 🚨 = Critical TODO (pipeline blocker)
- 🚧 = TODO (important but not blocking)