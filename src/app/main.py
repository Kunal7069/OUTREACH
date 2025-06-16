
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.database.database import Base, engine
from src.app.routers import user,document

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Service API",
    version="1.0.0",
    description="API to manage users"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(user.router)
app.include_router(document.router)