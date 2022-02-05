from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import db_config

SQLALCHEMY_DATABASE_URL = f"postgresql://" \
                          f"{db_config.username}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
