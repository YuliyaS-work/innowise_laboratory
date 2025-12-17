"""
Business logic and CRUD operations for Book entity.

Provides functions to create, read, update, delete and search Book records
using SQLAlchemy sessions.
"""

from sqlalchemy.orm import Session

from book_api.models.book import Book
from book_api.schemas.book import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate) -> Book:
    """
    Create a new Book in the database.

    Args:
        db (Session): Active SQLAlchemy session.
        book (BookCreate): Data required to create a new book.
    Returns:
        Book: The new created Book instance with its assigned ID.
    """
    new_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def read_books(db: Session) -> list[Book]:
    """
    Return all Book records from the database.

    Args:
        db (Session): Active SQLAlchemy session.
    Returns:
        list[Book]: A list of all Book records in the database.
    """
    return db.query(Book).all()


def delete_book(db: Session, book_id: int) -> Book | None:
    """
    Delete a Book record by ID.

    Args:
        db (Session): Active SQLAlchemy session.
        book_id (int):ID of the book to delete.
    Returns:
        Book | None : The deleted Book instance if found, otherwise None.
    """
    db_book = db.query(Book).filter(Book.id == book_id).first()

    if not db_book:
        return None

    db.delete(db_book)
    db.commit()
    return db_book


def update_book(db: Session, book_id: int, book: BookUpdate) -> Book | None:
    """
    Update a Book record by ID.

    Args:
        db (Session): Active SQLAlchemy session.
        book_id (int):ID of the book to update.
        book (BookUpdate): Fields to update.
    Returns:
        Book | None: The updated Book instance if found, otherwise None.
    """
    db_book = db.query(Book).filter(Book.id == book_id).first()

    if not db_book:
        return None

    db_book.title = book.title
    db_book.author = book.author
    db_book.year = book.year

    db.commit()
    db.refresh(db_book)
    return db_book


def search_books(
        db: Session,
        book_title: str = None,
        book_author: str = None,
        book_year: int = None
) -> list[Book]:
    """
    Search a Book record by title, author or year.

        Args:
        db (Session): Database session.
        book_title (str | None): Filter by title (optional).
        book_author (str | None): Filter by author (optional).
        book_year (int | None): Filter by year (optional).
    Returns:
        list[Book]: A list of matching books, or an empty list if none found.
    """

    if not any([book_title, book_author, book_year]):
        return []

    query = db.query(Book)

    if book_title:
        query = query.filter(Book.title.ilike(f"%{book_title}%"))
    if book_author:
        query = query.filter(Book.author.ilike(f"%{book_author}%"))
    if book_year:
        query = query.filter(Book.year == book_year)

    return query.all()
