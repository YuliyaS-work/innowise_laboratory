This is a FastAPI CRUD application for managing books.

---

## Installation

Install dependencies using Poetry:

poetry install

---

## Project Structure

The main application file is located inside the `book_api` package:

book_api/
    src/
        book_api/
            main.py
            api/        # routers
            core/       # settings, config
            db/         # database setup
            models/     # SQLAlchemy models
            schemas/    # Pydantic schemas
            services/   # business logic

---

## Running the Application

Run the application using:

uvicorn book_api.main:app --reload

---

## API Docs

http://127.0.0.1:8000/docs
___

## Main Endpoints

POST    /books            -Create a new book
GET     /books            - Get all books
PUT     /books/{book_id}  - Update book details
DELETE  /books/{book_id}  - Delete a book by ID
GET     /books/search/    - Search books by title, author, or year