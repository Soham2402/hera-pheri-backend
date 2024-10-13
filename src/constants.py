import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_name: str = os.getenv("DB_NAME")
    mongo_uri: str = os.getenv("MONGO_URI")


settings = Settings()
