from pydantic import BaseModel, Field
from typing import Optional

class Component(BaseModel):
    id: str = Field(..., alias="componentId")
    name: str
    type: str
    folder_id: Optional[str] = Field(None, alias="folderId")