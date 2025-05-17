from pydantic import BaseModel, Field

class ExecutionRecord(BaseModel):
    id: str = Field(..., alias="executionId")
    status: str
    started_at: str