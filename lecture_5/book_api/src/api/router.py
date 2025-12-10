from typing import List, Optional

from fastapi import Depends, APIRouter, HTTPException
from src.db.session import get_session
from src.services.book_service import *
from src.schemas.book import BookCreate, BookResponse

book_router = APIRouter()

@book_router.post("/books/", response_model=BookResponse)
def create_book_item(book: BookCreate, db: Session = Depends(get_session)):
    return create_book(db, book)

@book_router.get("/books/", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_session)):
    return read_books(db)

@book_router.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_session)):
    book = read_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@book_router.delete("/books/{book_id}", response_model=BookResponse)
def delete_book_item(book_id: int, db: Session = Depends(get_session)):
    book = delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@book_router.put("/books/{book_id}", response_model=BookResponse)
def update_book_item(book_id: int, book: BookUpdate, db: Session = Depends(get_session)):
    book = update_book(db, book_id, book)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@book_router.get("/books/search/", response_model=List[BookResponse])
def get_book_search(
        book_title: Optional[str] = None,
        book_author: Optional[str] = None,
        book_year: Optional[int] = None,
        db: Session = Depends(get_session)
):
    return read_book_search(db, book_title, book_author, book_year)