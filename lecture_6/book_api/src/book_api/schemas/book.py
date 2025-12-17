"""
Pydantic schemas for the Book entity.

Defines request and response models used in API endpoints.
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookBase(BaseModel):
    """Base schema for book data used in create operation."""
    title: str = Field(..., max_length=255)
    author: str = Field(..., max_length=255)
    year: Optional[int] = Field(None, ge = 0)


class BookCreate(BookBase):
    """Schema for creating a new book."""
    pass


class BookUpdate(BaseModel):
    """Schema for PUT (updating an existing book)."""
    title: str = Field(..., max_length=255)
    author: str = Field(..., max_length=255)
    year: Optional[int] = Field(..., ge=0)


class BookResponse(BaseModel):
    """Schema for returning book data in API responses."""
    id: int
    title: str
    author: str
    year: Optional[int] = None

    class Config:
        from_attributes = True