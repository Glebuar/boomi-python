from pydantic import BaseModel, Field
from typing import Optional

class Folder(BaseModel):
    id: str = Field(..., alias="folderId")
    name: str
    parent_id: Optional[str] = Field(None, alias="parentId")