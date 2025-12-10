"""
SQLAlchemy models for the Book entity.

Contains the Book class mapped to the books table.
"""

from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

from book_api.models.base import Base


class Book(Base):
    """SQLAlchemy model for the books table."""

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    author: Mapped[str] = mapped_column(String(255), index=True)
    year: Mapped[Optional[int]] = mapped_column(Integer, index=True, nullable=True)

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title={self.title}, author={self.author}, year={self.year})"

