"""
Main FastAPI application entry point.
"""

from fastapi import FastAPI

from book_api.api.router import  book_router

app = FastAPI()

app.include_router(book_router)