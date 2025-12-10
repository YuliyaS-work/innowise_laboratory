from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.book import Base
from src.core.config import Settings


engine = create_engine(Settings.DB_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base.metadata.create_all(bind=engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()