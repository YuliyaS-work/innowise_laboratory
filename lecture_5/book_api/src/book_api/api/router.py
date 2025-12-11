"""
API routers for Book entity.

Defines FastAPI endpoints for managing books.
"""

from typing import Optional

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from book_api.db.session import get_session
from book_api.services.book_service import (
    create_book,
    read_books,
    delete_book,
    update_book,
    search_books,
)
from book_api.schemas.book import BookCreate, BookResponse, BookUpdate

book_router = APIRouter(prefix="/books")

@book_router.post("/", response_model=BookResponse, status_code=201)
def create_book_item(
        book: BookCreate,
        db: Session = Depends(get_session)
) -> BookResponse:
    """Create a new book and return BookResponse."""
    return create_book(db, book)


@book_router.get("/", response_model=list[BookResponse])
def get_books(
        db: Session = Depends(get_session)
) -> list[BookResponse]:
    """Return all books."""
    return read_books(db)


@book_router.delete("/{book_id}", response_model=BookResponse, status_code=200)
def delete_book_item(
        book_id: int,
        db: Session = Depends(get_session)
) -> BookResponse:
    """Delete a book by its ID or raise 404 if not found."""
    book = delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.put("/{book_id}", response_model=BookResponse)
def update_book_item(
        book_id: int,
        book: BookUpdate,
        db: Session = Depends(get_session)
) -> BookResponse:
    """Update a book by its ID or raise 404 if not found."""
    book = update_book(db, book_id, book)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.get("/search/", response_model=list[BookResponse])
def get_book_search(
        book_title: Optional[str] = None,
        book_author: Optional[str] = None,
        book_year: Optional[int] = None,
        db: Session = Depends(get_session)
) -> list[BookResponse]:
    """Search books by title, author or year. Returns [] if not found."""
    return search_books(db, book_title, book_author, book_year)