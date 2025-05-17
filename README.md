<div align="center">

# Boomi Python SDK &nbsp;🚀

</div>

Light-weight, idiomatic wrapper around the **Boomi Platform API** and Partner API. It converts raw XML/JSON endpoints into a clean, developer-friendly Python client:

```python
from boomi import Boomi

boomi = Boomi.from_env()               # creds via env vars
proc   = boomi.components.create("hello.xml")
pkg    = boomi.packages.create(proc.id, notes="CI build")
boomi.deployments.deploy("DEV_ENV", pkg["packageId"])
```

| Feature | Status |
|---------|--------|
| Python 3.9+ | ✅ |
| Pydantic models for core objects | ✅ Component / Folder / Deployment / ExecutionRecord |
| Automatic retry on HTTP 429 | ✅ exponential back-off |
| JSON **and** XML parsing | ✅ falls back seamlessly |
| Minimal deps (`requests`, `pydantic`, `xmltodict`) | ✅ |
| Typed resource facade (`boomi.components`, `boomi.schedules`, …) | ✅ |
| CI wheel build & PyPI publish | ✅ `publish.yml` |

---

## Installation

```bash
# stable
pip install boomi

# or live editable clone
git clone git@github.com:Glebuar/boomi-python.git
cd boomi-python
pip install -e .
```

### Authentication

```bash
export BOOMI_ACCOUNT="ACCT-123456"
export BOOMI_USER="BOOMI_TOKEN.jane@acme.com"
export BOOMI_SECRET="abcd1234-…"
```

The user string **must** start with `BOOMI_TOKEN.` when you use an API token.

---

## Quick-start

```python
from boomi import Boomi
from pathlib import Path

boomi = Boomi.from_env()

# 1 — create a Process from XML
proc = boomi.components.create(Path("hello_process.xml"))
print("Component ID:", proc.id)

# 2 — package + deploy
pkg = boomi.packages.create(proc.id, notes="nightly build")
boomi.deployments.deploy(environment_id="DEV_ENV", package_id=pkg["packageId"])

# 3 — trigger run and grab log
run = boomi.execute.run({"atomId": "DEV_ATOM", "processId": proc.id})
log = boomi.runs.log(run["executionId"])
print(log[:500])
```

---

## Project layout

```
boomi/
├─ __init__.py          # re-exports Boomi client + models + exceptions
├─ client.py            # wires all resources
├─ _http.py             # retry logic, JSON↔︎XML helper
├─ exceptions.py
├─ models/              # Component, Folder, Deployment, ExecutionRecord
└─ resources/           # components, packages, deployments, schedules, …
docs/                   # MkDocs-ready markdown docs
examples/               # hello-process demo
.github/workflows/      # publish.yml → TestPyPI / PyPI
```

---

## Documentation

Full API docs live in [`docs/`](docs/) and can be served locally:

```bash
pip install mkdocs-material
mkdocs serve
```

---

## Contributing

1. Fork & clone  
2. `pip install -e ".[dev]"`  
3. Run `pytest` (tests are mocked with **responses**)  
4. Open a PR — CI will build wheels and run unit tests.

---

## License

MIT © 2025 Gleb Bochkarov
