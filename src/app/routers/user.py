from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserResponse
from ..services.userManager import UserManager
from ..config.database.database import SessionLocal
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/user", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    manager = UserManager(db)
    return manager.save_user(user)

@router.get("/auth", response_model=UserResponse)
def authenticate_user(linkedin_username: str, password: str, db: Session = Depends(get_db)):
    manager = UserManager(db)
    user = manager.get_user_by_linkedin_and_password(linkedin_username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
