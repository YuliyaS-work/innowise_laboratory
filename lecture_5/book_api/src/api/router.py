"""
API routers for Book entity.

Defines FastAPI endpoints for managing books.
"""

from typing import Optional

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from src.db.session import get_session
from src.services.book_service import (
    create_book,
    read_book,
    read_books,
    delete_book,
    update_book,
    search_books,
)
from src.schemas.book import BookCreate, BookResponse, BookUpdate

book_router = APIRouter()

@book_router.post("/books/", response_model=BookResponse)
def create_book_item(book: BookCreate, db: Session = Depends(get_session)):
    """Create a new book and return BookResponse."""
    return create_book(db, book)


@book_router.get("/books/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_session)):
    """Return all books."""
    return read_books(db)


@book_router.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_session)):
    """Return a book by its ID or raise 404 if not found."""
    book = read_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.delete("/books/{book_id}", response_model=BookResponse)
def delete_book_item(book_id: int, db: Session = Depends(get_session)):
    """Delete a book by its ID or raise 404 if not found."""
    book = delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.put("/books/{book_id}", response_model=BookResponse)
def update_book_item(book_id: int, book: BookUpdate, db: Session = Depends(get_session)):
    """Update a book by its ID or create a new book if ID isn't found."""
    return update_book(db, book_id, book)


@book_router.get("/books/search/", response_model=list[BookResponse])
def get_book_search(
        book_title: Optional[str] = None,
        book_author: Optional[str] = None,
        book_year: Optional[int] = None,
        db: Session = Depends(get_session)
):
    """Search books by title, author or year. Returns [] if not found."""
    return search_books(db, book_title, book_author, book_year)