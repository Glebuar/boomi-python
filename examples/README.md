# Boomi Python SDK Examples

This directory contains example scripts demonstrating how to use the Boomi Python SDK after the circular import fixes.

## Available Examples

### 1. `sample.py` - Basic Account Information
**Purpose**: Simple example showing SDK initialization and basic API calls.

**What it does**:
- Initializes the Boomi SDK with credentials
- Retrieves account information using the Account API
- Demonstrates basic error handling and response processing

**Usage**:
```bash
cd examples
PYTHONPATH=../src python sample.py
```

**Requirements**: Environment variables for Boomi credentials (see below)


### 2. Component Management Examples
**Location**: `component_management/` directory

**Available Scripts**:
- `get_component.py` - Retrieve component details and XML configuration
- `update_component.py` - Update component metadata and configuration
- `update_component_xml.py` - Update component XML with raw XML approach
- Various working examples for component operations

**Usage**:
```bash
cd examples/component_management
PYTHONPATH=../../src python get_component.py COMPONENT_ID
PYTHONPATH=../../src python update_component.py COMPONENT_ID
```

**Requirements**: Environment variables for Boomi credentials

### 3. Component Metadata Examples  
**Location**: `component_metadata/` directory

**Available Scripts**:
- `list_all_components.py` - List all components with metadata
- `query_process_components.py` - Query specific process components

**Usage**:
```bash
cd examples/component_metadata
PYTHONPATH=../../src python list_all_components.py
```

**Requirements**: Environment variables for Boomi credentials

---

## Setup Requirements

### Environment Variables
Create a `.env` file in the project root with your Boomi credentials:

```bash
BOOMI_ACCOUNT=your_account_id
BOOMI_USER=your_username  
BOOMI_SECRET=your_password_or_token
```

### Dependencies
```bash
pip install python-dotenv
```

## Running the Examples

1. **Set up credentials** in `.env` file
2. **Run from the examples directory** with `PYTHONPATH=../src`
3. **Check results** in your Boomi Build page for process creation examples

## Example Output

### Successful Run:
```
🚀 Boomi Python SDK - Sample Application
=============================================
✅ SDK initialized successfully!
📊 Available services: 114
🔍 Fetching account information for: your-account-id
✅ Account information retrieved successfully!
🎉 SUCCESS: Boomi SDK is working correctly!
```

### Component Management Success:
```
🚀 Boomi SDK Example: Get Component
✅ Component retrieved successfully!
📋 Component Metadata:
  Name: Sample Process
  Component ID: 112b4efe-b173-4258-9492-613ead7d52ce
  Type: process
  Version: 1
  Status: CURRENT
🎉 SUCCESS!
```

### Component Listing Success:
```
🚀 Boomi SDK Example: List All Components
🔍 Querying all components...
✅ Found 45 total components
📊 Component Summary:
  • Processes: 25
  • Connectors: 15
  • Maps: 5

📂 Components by Folder:
📁 Folder: Production
   1. Customer Data Sync Process (process)
   2. Order Integration Connector (connector)

📊 Summary Statistics:
  • Total components: 45
  • Active components: 42
  • Folders: 8
```