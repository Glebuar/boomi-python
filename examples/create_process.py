from pathlib import Path
from boomi import Boomi

# 1. Instantiate the client from env-vars
boomi = Boomi.from_env()

# 2. Create the component
xml_file = Path("examples/hello_process.xml")
process  = boomi.components.create(xml_file)

print(f"✓ Created process '{process.name}' (id={process.id})")
