from typing import List
from fastapi import FastAPI, Query, Path

from schemas import Book


app = FastAPI()


@app.get('/')
def home():
    return {"key": "hello"}


@app.post('/book')
def create_book(item: Book):
    return item


@app.get('/book')
def get_book(q: List[str] = Query(["qwe", "asd"], description="Search book", deprecated=True)):
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {"pk": pk, "pages": pages}
