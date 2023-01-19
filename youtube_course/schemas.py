from typing import List
from datetime import date
from pydantic import BaseModel, Field, validator


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(
        ..., ge=15, le=90,
        description="Author's age must be in [15; 90]"
    )

    # The same validator
    @validator('age')
    def check_age(cls, val):
        if 15 > val or val > 90:
            raise ValueError("Author's age must be in [15; 90]")
        return val


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int


class BookOut(Book):
    id: int
