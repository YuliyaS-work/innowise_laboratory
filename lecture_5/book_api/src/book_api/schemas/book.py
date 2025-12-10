"""
Pydantic schemas for the Book entity.

Defines request and response models used in API endpoints.
"""

from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookCreate(BookBase):
    """Schema for creating a new book."""
    pass


class BookUpdate(BookBase):
    """Schema for PUT (updating an existing book or creating a new one)."""
    pass


class BookResponse(BaseModel):
    """Schema for returning book data in API responses."""

    id: int
    title: str
    author: str
    year: Optional[int] = None

    class Config:
        from_attributes = True