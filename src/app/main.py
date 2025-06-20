
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.database.database import Base, engine
from src.app.routers import user,document
import requests
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

@app.get("/login-cookies")
def login_and_get_cookies():
    url = "https://api.prod.kiwiq.ai/api/v1/auth/login?keep_me_logged_in=true"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "grant_type": "password",
        "username": "raunak@kiwiq.ai",
        "password": "L3gP0yWZ8dK6jH4g"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            cookies = response.cookies
            return  {
                    "refresh_token": cookies.get("refresh_token"),
                    "access_token": cookies.get("access_token"),
                    "XSRF-TOKEN": cookies.get("XSRF-TOKEN")
                }
            
        else:
            return {
                "status": "failed",
                "status_code": response.status_code,
                "message": response.text
            }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
        