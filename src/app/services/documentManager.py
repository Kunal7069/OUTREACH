from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from fastapi import UploadFile

from src.app.models.user import User
from src.app.models.document import Document
from ..utils.dropbox_upload import upload_to_dropbox


class DocumentManager:
    def __init__(self, db: Session):
        self.db = db

    def save_document(self, name: str, linkedin_username: str, document_url: str, tag: Optional[str] = None) -> Optional[Document]:
        try:
            user = (
                self.db.query(User)
                .filter(User.name == name, User.linkedin_username == linkedin_username)
                .first()
            )
            if not user:
                print(f"[NotFound] No user found for name='{name}', linkedin_username='{linkedin_username}'")
                return None

            document = Document(
                user_id=user.id,
                document_url=document_url,
                tag=tag
            )

            self.db.add(document)
            self.db.commit()
            self.db.refresh(document)
            return document

        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"[SQLAlchemyError] Error saving document: {e}")
            return None
        except Exception as e:
            self.db.rollback()
            print(f"[Exception] Unexpected error: {e}")
            return None
        
        
    def save_document_from_upload(self, name: str, linkedin_username: str, file: UploadFile, tag: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Document]:
        try:
            user = (
                self.db.query(User)
                .filter(User.name == name, User.linkedin_username == linkedin_username)
                .first()
            )
            if not user:
                print(f"[NotFound] No user found for name='{name}', linkedin_username='{linkedin_username}'")
                return None

            # Upload to Dropbox
            document_url = upload_to_dropbox(user.id,file, tag or "untagged")

            # Save to DB
            document = Document(
                user_id=user.id,
                document_url=document_url,
                tag=tag,
                title = title,
                description=description
            )

            self.db.add(document)
            self.db.commit()
            self.db.refresh(document)
            return document

        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"[SQLAlchemyError] Error saving document: {e}")
            return None
        except Exception as e:
            self.db.rollback()
            print(f"[Exception] Unexpected error: {e}")
            return None
        

    def get_documents_by_user(self, name: str, linkedin_username: str) -> List[Document]:
        try:
            user = (
                self.db.query(User)
                .filter(User.name == name, User.linkedin_username == linkedin_username)
                .first()
            )
            if not user:
                print(f"[NotFound] No user found for name='{name}', linkedin_username='{linkedin_username}'")
                return []
            print(user.documents)
            return user.documents

        except SQLAlchemyError as e:
            print(f"[SQLAlchemyError] Error retrieving documents: {e}")
            return []
        except Exception as e:
            print(f"[Exception] Unexpected error: {e}")
            return []
