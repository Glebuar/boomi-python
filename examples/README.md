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


### 2. `list_process_components.py` - List Process Components (Build View)
**Purpose**: Displays all process components in your Boomi account from the Build/development perspective.

**What it does**:
- Queries all process components using ComponentMetadata API
- Shows Build view of processes (not deployment/execution status)
- Organizes results by folder structure with detailed metadata
- Filters to current active versions by default, option to show all
- Provides comprehensive statistics and component information

**Usage**:
```bash
cd examples
PYTHONPATH=../src python list_process_components.py [--all]
```

**Options**:
- `--all`: Show all versions including deleted and non-current versions

**Requirements**: Environment variables for Boomi credentials

### 3. `create_process.py` - Standalone Process Creation
**Purpose**: Self-contained example that creates a process with inline XML (no external files needed).

**What it does**:
- Defines process XML inline within the script
- Creates a demo process: Start → Message → Stop
- Demonstrates complete component creation workflow
- Perfect for distribution and testing

**Usage**:
```bash
cd examples
PYTHONPATH=../src python create_process.py
```

**Requirements**: Only needs environment variables (no external files)

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

### Process Creation Success:
```
🚀 Boomi Python SDK - Process Creation Demo  
✅ SDK initialized successfully!
🔄 Creating process via Component API...
✅ Process creation successful!
🎉 SUCCESS!
📍 Check your Boomi Build page to see the new process
```

### Process Components Listing:
```
🚀 Boomi SDK Example: List Process Components
🔍 Mode: Showing CURRENT ACTIVE process components only
🏢 Account: your-account-id
👤 User: your-username
📋 Mode: current active versions only

🔍 Querying process components...
✅ Found 33 total process component version(s)
📊 Showing 19 current active component versions
💡 14 historical/deleted versions hidden (use --all to show)

📂 Process Components by Folder:
📁 Folder: Production
   1. Customer Data Sync Process
      Component ID: abc123-def456-ghi789
      Version: 3
      Status: CURRENT
      Created: 2025-01-15 by developer@company.com
      Modified: 2025-01-20 by developer@company.com

📊 Summary Statistics:
  • Total component versions shown: 19
  • Unique components: 19
  • Folders with processes: 5
```