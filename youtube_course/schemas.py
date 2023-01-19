from typing import List
from datetime import date
from pydantic import BaseModel, Field, validator


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(
        ..., gt=15, lt=90,
        description="Author's age must be more than 15 and less than 90"
    )

'''
    @validator('age')
    def check_age(cls, v):
        if 15 < v < 90:
            raise ValueError("Author's age must be more than 15 and less than 90")
        return v
'''


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