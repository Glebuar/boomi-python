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