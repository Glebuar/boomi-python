from pydantic import BaseModel, Field
from typing import Optional

class Deployment(BaseModel):
    id: str = Field(..., alias="deploymentId")
    component_id: str = Field(..., alias="componentId")
    environment_id: str = Field(..., alias="environmentId")
    package_version: Optional[str] = Field(None, alias="packageVersion")
    status: Optional[str] = None