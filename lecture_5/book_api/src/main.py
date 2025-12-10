from fastapi import FastAPI

from src.api.router import  book_router

app = FastAPI()
app.include_router(book_router)