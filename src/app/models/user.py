import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..config.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    name = Column(String, nullable=False)
    linkedin_username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    
    documents = relationship("Document", back_populates="user", cascade="all, delete")