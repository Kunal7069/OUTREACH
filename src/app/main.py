
from fastapi import FastAPI
from .config.database.database import Base, engine
from src.app.routers import user,document

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Service API",
    version="1.0.0",
    description="API to manage users"
)

# Register routes
app.include_router(user.router)
app.include_router(document.router)