from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://neondb_owner:npg_2bRfcszH4LtV@ep-small-sea-a8kr1a7g-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"

    class Config:
        env_file = ".env"

settings = Settings()