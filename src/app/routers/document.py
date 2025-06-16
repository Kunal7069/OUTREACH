from fastapi import APIRouter, Depends, UploadFile, Form, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from ..services.documentManager import DocumentManager
from src.app.schemas.document import DocumentCreate, DocumentResponse
from ..config.database.database import get_db

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/", response_model=DocumentResponse)
def create_document(
    name: str = Form(...),
    linkedin_username: str = Form(...),
    tag: str = Form(None),
    title: str = Form(None),
    description: str = Form(None),
    file: UploadFile = Form(...),
    db: Session = Depends(get_db)
):
    manager = DocumentManager(db)
    document = manager.save_document_from_upload(name, linkedin_username, file, tag,title,description)
    if not document:
        raise HTTPException(status_code=400, detail="Document could not be created. Check if the user exists.")
    return document


@router.get("/", response_model=List[DocumentResponse])
def get_documents(name: str, linkedin_username: str, db: Session = Depends(get_db)):
    manager = DocumentManager(db)
    documents = manager.get_documents_by_user(name, linkedin_username)
    return documents