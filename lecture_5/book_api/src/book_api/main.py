"""
Main FastAPI application entry point.

Initializes the FastAPI app and registers all API routers.
"""

from fastapi import FastAPI

from book_api.api.router import  book_router

app = FastAPI()

app.include_router(book_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}