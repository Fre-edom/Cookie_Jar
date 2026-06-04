from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str 
    class Config:
        env_file = ".env"

setting = Settings()
engine = create_engine(setting.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)