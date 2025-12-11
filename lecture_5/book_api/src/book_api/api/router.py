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
    """
    Create a new book.

    Args:
        book (BookCreate): Data required to create a new book.
        db (Session): Database session.
    Returns:
        BookResponse: The created book with its assigned ID.
    """
    return create_book(db, book)


@book_router.get("/", response_model=list[BookResponse])
def get_books(
        db: Session = Depends(get_session)
) -> list[BookResponse]:
    """
    Return all books.

    Args:
        db (Session): Database session.
    Returns:
        list[BookResponse]: A list of all books in the database.
    """
    return read_books(db)


@book_router.delete("/{book_id}", response_model=BookResponse, status_code=200)
def delete_book_item(
        book_id: int,
        db: Session = Depends(get_session)
) -> BookResponse:
    """
    Delete a book by its ID or raise 404 if not found.

    Args:
        book_id (int): ID of the book to delete.
        db (Session): Database session.
    Returns:
        BookResponse: The deleted book.
    Raises:
        HTTPException: If the book with the given ID doesn't exist.
    """
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
    """
    Update a book by its ID or raise 404 if not found.

    Args:
        book_id (int): ID of the book to update.
        book (BookUpdate): Fields to update.
        db (Session): Database session.
    Returns:
        BookResponse: The updated book.
    Raises:
        HTTPException: If the book with the given ID doesn't exist.
    """
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
    """
    Search books by title, author or year. Returns [] if not found.

    Args:
        book_title (str | None): Filter by title (optional).
        book_author (str | None): Filter by author (optional).
        book_year (int | None): Filter by year (optional).
        db (Session): Database session.
    Returns:
        list[BookResponse]: Matching books or an empty list if none found.
    """
    return search_books(db, book_title, book_author, book_year)