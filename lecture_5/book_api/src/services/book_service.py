from sqlalchemy.orm import Session

from src.models.book import Book
from src.schemas.book import BookCreate, BookUpdate

def create_book(db: Session, book: BookCreate):
    new_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def read_books(db: Session):
    return db.query(Book).all()

def read_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        return None
    book_data = db_book
    db.delete(db_book)
    db.commit()
    return book_data

def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        return None

    if book.title is not None:
        db_book.title = book.title
    if book.author is not None:
        db_book.author = book.author
    if book.year is not None:
        db_book.year = book.year
    db.commit()
    db.refresh(db_book)
    return db_book

def read_book_search(db: Session, book_title: str = None, book_author: str = None, book_year: int = None):

    if not any([book_title, book_author, book_year]):
        return []

    query = db.query(Book)

    if book_title:
        query = query.filter(Book.title == book_title)
    if book_author:
        query = query.filter(Book.author == book_author)
    if book_year:
        query = query.filter(Book.year == book_year)
    return query.all()
