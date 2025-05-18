# Installation

This guide will help you install and set up the Boomi Python SDK.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Installation Methods

### Using pip

The recommended way to install the SDK is using pip:

```bash
pip install boomi
```

### From Source

To install from source:

1. Clone the repository:
```bash
git clone https://github.com/Glebuar/boomi-python.git
cd boomi-python
```

2. Install the package:
```bash
pip install -e .
```

## Dependencies

The SDK automatically installs the following dependencies:

- requests>=2.32.0
- pydantic>=2.7.0,<3.0.0
- xmltodict>=0.13.0

## Development Dependencies

If you're developing the SDK, you'll need additional dependencies:

```bash
pip install -e ".[dev]"
```

This will install development dependencies including:
- pytest
- black
- isort
- mypy
- flake8

## Next Steps

- Check out the [Quick Start Guide](quickstart.md) to begin using the SDK
- Review the [Client Configuration](client.md) for setup options 
