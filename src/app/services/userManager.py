
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from typing import Optional
from src.app.models.user import User
from src.app.schemas.user import UserCreate


class UserManager:
    def __init__(self, db: Session):
        self.db = db

    def save_user(self, user_data: UserCreate) -> Optional[User]:
        try:
            user = User(
                name=user_data.name,
                linkedin_username=user_data.linkedin_username,
                password=user_data.password  # ⚠️ Hash in production!
            )
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            self.db.rollback()
            print(f"[IntegrityError] User with this LinkedIn username already exists: {e}")
            return None
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"[SQLAlchemyError] Failed to save user: {e}")
            return None
        except Exception as e:
            self.db.rollback()
            print(f"[Exception] Unexpected error occurred: {e}")
            return None

    def get_user_by_linkedin_and_password(self, linkedin_username: str, password: str) -> Optional[User]:
        try:
            user = (
                self.db.query(User)
                .filter(
                    User.linkedin_username == linkedin_username,
                    User.password == password
                )
                .first()
            )
            return user
        except SQLAlchemyError as e:
            print(f"[SQLAlchemyError] Failed to fetch user: {e}")
            return None
        except Exception as e:
            print(f"[Exception] Unexpected error occurred: {e}")
            return None
