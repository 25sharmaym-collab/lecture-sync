from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "LectureSync"
    app_env: str = "development"
    secret_key: str = "change-this-in-production"
    access_token_minutes: int = 30
    refresh_token_days: int = 7
    verification_token_hours: int = 24
    password_reset_hours: int = 1
    database_url: str = "postgresql+psycopg://lecturesync:change-me@localhost:5432/lecturesync"
    redis_url: str = "redis://localhost:6379/0"
    frontend_url: str = "http://localhost:3000"
    cors_origins: str = "http://localhost:3000"
    sendgrid_api_key: str | None = None
    sendgrid_from_email: str = "noreply@example.com"
    max_upload_mb: int = 1024
    storage_dir: str = "./data"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    @property
    def cors_origin_list(self) -> list[str]:
        return [x.strip() for x in self.cors_origins.split(",") if x.strip()]
@lru_cache
def get_settings() -> Settings:
    return Settings()