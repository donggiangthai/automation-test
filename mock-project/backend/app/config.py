"""
Application configuration
"""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/mockdb"
    
    # Google OAuth
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    
    # App
    SECRET_KEY: str = "your-secret-key-change-in-production"
    FRONTEND_URL: str = "http://localhost:3000"
    
    # Development
    BYPASS_AUTH: bool = True
    TEST_USER_EMAIL: str = "test@example.com"
    
    # JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
