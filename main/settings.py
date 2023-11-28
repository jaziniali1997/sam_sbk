from pydantic_settings import BaseSettings, SettingsConfigDict
from datetime import datetime


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
    SECRET_KEY: str
    START_DATE: datetime
    END_DATE: datetime

    model_config = SettingsConfigDict(env_file=".env")
