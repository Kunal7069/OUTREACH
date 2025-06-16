from pydantic import BaseModel
from uuid import UUID

class UserCreate(BaseModel):
    name: str
    linkedin_username: str
    password: str  # NEW

class UserResponse(BaseModel):
    id: UUID
    name: str
    linkedin_username: str

    class Config:
        orm_mode = True