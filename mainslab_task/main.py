#!/usr/bin/env python

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

import data_handler as dh


app = FastAPI()


@app.get("/")
async def root():
    response = HTMLResponse("""
        <a href="/upload"><b>UPLOAD</b></a>
        <br><br>
        <a href="/test">TEST</a>
    """)
    return response


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    data = dh.parse_csv(file.file)
    file.file.close()
    return data


@app.get("/test")
async def root():
    response = HTMLResponse("test")
    return response