"""Simple hello-world FastAPI app"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    """Return {"Hello": "World"}."""
    return {"Hello": "World"}
