"""
Database configuration and session management.

Defines SQLAlchemy engine, session factory, and dependency for FastAPI.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import Settings
from src.models.book import Book
from src.models.base import Base

engine = create_engine(Settings.DB_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base.metadata.create_all(bind=engine)


def get_session():
    """Provide a database session for FastAPI dependency injection."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()