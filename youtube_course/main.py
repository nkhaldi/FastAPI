from typing import List
from fastapi import FastAPI, Query, Path, Body

from schemas import Book, Author, BookOut


app = FastAPI()


@app.get('/')
def home():
    return {"key": "hello"}


@app.get('/book')
def get_book(
    q: List[str] = Query(
        ["qwe", "asd"],
        description="Search book", deprecated=True
    )
):
    return q


@app.get('/book/{pk}')
def get_single_book(
    pk: int = Path(..., gt=1, le=20),
    pages: int = Query(None, gt=10, le=500)
):
    return {"pk": pk, "pages": pages}


@app.post(
    '/book',
    response_model=Book,
    response_model_exclude={"pages", "date"},
    response_model_exclude_unset=True
)
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return item
    # return {"item": item, "author": author, "quantity": quantity}


@app.post('/bookout', response_model=BookOut)
def create_bookout(item: Book):
    return BookOut(**item.dict(), id=3)


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}
