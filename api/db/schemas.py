from enum import Enum
from typing import OrderedDict
from pydantic import BaseModel

class Genre(str, Enum):
    SCI_FI = "Science Fiction"
    FANTASY = "Fantasy"
    HORROR = "Horror"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    THRILLER = "Thriller"

class Book(BaseModel):
    """Book schema

    Args:
        BaseModel (BaseModel): Pydantic base model.
    """
    id: int
    title: str
    author: str
    publication_year: int
    genre: Genre

class InMemoryDB:
    def __init__(self):
        self.books: OrderedDict[int, Book] = {}

    def get_books(self) -> list[Book]:
        return self.books
    
    def add_book(self, book: Book) -> Book:
        self.books.update({book.id: book})

    def get_book(self, book_id: int) -> Book:
        return self.books.get(book_id)
            

    books = [
        {
            "id": 1,
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "publication_year": 1937,
            "genre": Genre.SCI_FI
        },
        {
            "id": 2,
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "publication_year": 1954,
            "genre": Genre.FANTASY
        },
        {
            "id": 3,
            "title": "The Return of the King",
            "author": "J.R.R. Tolkien",
            "publication_year": 1955,
            "genre": Genre.FANTASY
        }
    ]
