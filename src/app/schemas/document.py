
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class DocumentCreate(BaseModel):
    name: str
    linkedin_username: str
    tag: Optional[str] = None

class DocumentResponse(BaseModel):
    id: UUID
    user_id: UUID
    document_url: str
    tag: Optional[str]
    title: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True
    