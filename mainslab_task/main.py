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


# Принимает cvs-файл, валидирует значения и возвращает его в формате json
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    data = dh.get_data(file.file)
    file.file.close()
    dh.save_data(data)

    return data


# Отображает информацию по счёту
@app.get("/get_service")
async def root():
    response = HTMLResponse("test")
    return response