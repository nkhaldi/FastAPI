import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from models import Author as ModelAuthor
from models import Book as ModelBook
from schema import Author as SchemaAuthor
from schema import Book as SchemaBook

load_dotenv(".env")


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.post("/book/", response_model=SchemaBook)
async def book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating, author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.get("/book")
async def book():
    book = db.session.query(ModelBook).all()
    return book


@app.get("/author")
async def author():
    author = db.session.query(ModelAuthor).all()
    return author


@app.post("/author", response_model=SchemaAuthor)
async def author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author


# To run locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
